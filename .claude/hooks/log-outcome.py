#!/usr/bin/env python3
"""Hook Stop: rellena el «Qué salió» de la entrada correspondiente en prompts.md.

Es el compañero de log-prompt.py (UserPromptSubmit), que crea la entrada con esa línea vacía
porque en ese momento aún no ha pasado nada. Aquí sí hay transcript: de él sale un resumen del
turno (prompt, herramientas y respuesta final) que se le pasa a `claude -p` con Haiku para que
lo condense en una línea al estilo del cuaderno. El modelo cuesta unos segundos, así que el hook
está declarado `async` en settings.json y no retrasa el turno.

Dos cosas que hay que tener en cuenta del transcript:

- La respuesta final del asistente se escribe en el fichero un poco DESPUÉS de que salte Stop,
  así que hay que esperarla (wait_for_reply) o el resumen sale vacío.
- Como el hook es asíncrono, el usuario puede haber lanzado ya el siguiente prompt cuando
  terminamos. Por eso se busca la entrada cuyo prompt coincide, no la última sin más.

Silencioso y no bloqueante: ante cualquier error sale con 0 sin tocar nada.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import time

EDIT_TOOLS = {"Edit", "Write", "NotebookEdit", "MultiEdit"}
MODEL = "haiku"
# Mensajes que entran como turno de usuario sin haberlos escrito nadie (ver log-prompt.py).
NOT_TYPED = ("<agent-message", "<task-notification")
WAIT_REPLY_SECONDS = 20
CLAUDE_TIMEOUT = 90
MAX_LINE = 240

INSTRUCCIONES = """\
Eres el cronista de un cuaderno de prompts de un curso. Te paso un turno de una sesión de Claude
Code: el prompt que lanzó el alumno, las herramientas que usó el asistente y su respuesta final.

Escribe UNA sola línea en español que resuma QUÉ SALIÓ del turno: qué hizo o contestó el
asistente, y si funcionó, se quedó a medias o se equivocó. En pasado, sin markdown salvo
`backticks` para nombres de fichero, sin comillas alrededor, máximo 220 caracteres.

Ejemplos del tono que se espera:
- una guía de todas las piezas de golpe, con preguntas; demasiado texto de una vez.
- verificó las claves en la documentación y creó `.claude/settings.local.json`; los agentes admiten `model` y `effort` en su frontmatter.
- me corrigió (AGENTS.md es un estándar entre herramientas, no de Anthropic) y propuso un experimento para comprobar qué leen los subagentes.
- respuesta a medias; las reglas de proceso van en `CLAUDE.md` porque nombran piezas que solo existen en Claude Code.

Responde únicamente con esa línea.
"""


def blocks(row):
    content = (row.get("message") or {}).get("content")
    return content if isinstance(content, list) else []


def text_of(row):
    content = (row.get("message") or {}).get("content")
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") for b in blocks(row) if b.get("type") == "text")


def is_prompt(row):
    """Mensaje de usuario escrito por la persona, no un tool_result ni un meta del sistema."""
    if row.get("type") != "user" or row.get("isSidechain") or row.get("isMeta"):
        return False
    text = text_of(row).strip()
    return bool(text) and not text.startswith(NOT_TYPED)


def read_transcript(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                pass
    return [r for r in rows if not r.get("isSidechain")]


def split_turn(rows):
    start = max((i for i, r in enumerate(rows) if is_prompt(r)), default=None)
    if start is None:
        return None, []
    return text_of(rows[start]), rows[start + 1 :]


def has_reply(turn):
    return any(text_of(r).strip() for r in turn if r.get("type") == "assistant")


def wait_for_reply(path):
    """La respuesta final aparece en el transcript después de que salte Stop; la esperamos."""
    deadline = time.time() + WAIT_REPLY_SECONDS
    while True:
        rows = read_transcript(path)
        prompt, turn = split_turn(rows)
        if prompt is None or has_reply(turn) or time.time() > deadline:
            return prompt, turn
        time.sleep(0.5)


def tool_label(block):
    name = block.get("name") or "?"
    args = block.get("input") or {}
    detail = (
        args.get("description")
        or args.get("file_path")
        or args.get("notebook_path")
        or args.get("pattern")
        or args.get("url")
        or ""
    )
    return "%s: %s" % (name, str(detail)[:100]) if detail else name


def digest(prompt, turn):
    tools, files, replies = [], [], []
    for row in turn:
        if row.get("type") != "assistant":
            continue
        for block in blocks(row):
            if block.get("type") == "tool_use":
                tools.append(tool_label(block))
                if block.get("name") in EDIT_TOOLS:
                    path = (block.get("input") or {}).get("file_path") or (
                        block.get("input") or {}
                    ).get("notebook_path")
                    if path and path not in files:
                        files.append(path)
            elif block.get("type") == "text" and block.get("text", "").strip():
                replies.append(block["text"])

    partes = [
        "### Prompt del alumno\n%s" % prompt[:2000],
        "### Herramientas usadas (%d)\n%s" % (len(tools), "\n".join(tools[:40]) or "(ninguna)"),
        "### Respuesta final del asistente\n%s" % ("\n\n".join(replies)[-4000:] or "(sin texto)"),
    ]
    return "\n\n".join(partes), len(tools), files


def ask_claude(body):
    """Un `claude -p` aparte: sin hooks (si no, se registraría a sí mismo), sin MCP y sin sesión.

    Se lanza desde /tmp para que no arrastre el CLAUDE.md del proyecto como contexto.
    """
    out = subprocess.run(
        [
            "claude", "-p",
            "--model", MODEL,
            "--no-session-persistence",
            "--strict-mcp-config",
            "--settings", '{"disableAllHooks":true}',
        ],
        input=INSTRUCCIONES + "\n" + body,
        capture_output=True,
        text=True,
        timeout=CLAUDE_TIMEOUT,
        cwd=tempfile.gettempdir(),
    )
    if out.returncode != 0:
        return ""
    return destacar(" ".join(out.stdout.split())[:MAX_LINE].rstrip())


def destacar(linea):
    """El cuaderno escribe estas líneas en minúscula; respeta siglas y nombres propios."""
    primera = linea.split(" ", 1)[0].strip("`")
    if primera[:1].isupper() and primera[1:].islower():
        return linea[0].lower() + linea[1:]
    return linea


def fallback(turn):
    """Si el modelo no contesta, al menos el primer párrafo de la respuesta."""
    for row in reversed(turn):
        texto = text_of(row).strip() if row.get("type") == "assistant" else ""
        if texto:
            return " ".join(texto.split("\n\n")[0].split())[:MAX_LINE]
    return ""


def outcome_line(prompt, turn):
    body, tools, files = digest(prompt, turn)
    resumen = ask_claude(body) or fallback(turn)
    stats = "%d herramienta%s" % (tools, "" if tools == 1 else "s")
    if files:
        stats += ", %d fichero%s editado%s" % (
            len(files), "" if len(files) == 1 else "s", "" if len(files) == 1 else "s"
        )
    return "%s (%s)" % (resumen, stats) if resumen else "(%s)" % stats


def same_prompt(entry, prompt):
    """Los slash commands llegan al transcript envueltos en <command-name>, de ahí el 'in'."""
    a = "".join(entry.split())
    b = "".join(prompt.split())
    return bool(a) and (a in b or b in a)


def patch(path, prompt, line):
    """Rellena la entrada cuyo prompt coincide: con el hook en async puede no ser la última."""
    with open(path) as f:
        content = f.read()

    starts = [m.start() for m in re.finditer(r"^## Prompt \d+$", content, re.MULTILINE)]
    for i in reversed(range(len(starts))):
        head = content[: starts[i]]
        entry = content[starts[i] : starts[i + 1]] if i + 1 < len(starts) else content[starts[i] :]
        tail = content[starts[i + 1] :] if i + 1 < len(starts) else ""

        fenced = re.search(r"^(`{3,})\n(.*?)\n\1$", entry, re.MULTILINE | re.DOTALL)
        if not fenced or not same_prompt(fenced.group(2), prompt):
            continue

        line = "**Qué salió:** " + line
        entry, replaced = re.subn(
            r"^\*\*Qué salió:\*\*.*$", lambda _: line, entry, count=1, flags=re.MULTILINE
        )
        if not replaced:
            entry = entry.rstrip("\n") + "\n\n" + line + "\n"
        with open(path, "w") as f:
            f.write(head + entry + tail)
        return


def main():
    payload = json.load(sys.stdin)
    prompt, turn = wait_for_reply(payload["transcript_path"])
    if not prompt or not turn:
        return
    patch(os.path.join(os.environ["CLAUDE_PROJECT_DIR"], "prompts.md"), prompt, outcome_line(prompt, turn))


try:
    main()
except Exception:
    pass
sys.exit(0)
