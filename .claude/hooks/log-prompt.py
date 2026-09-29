#!/usr/bin/env python3
"""Hook UserPromptSubmit: añade cada prompt al final de prompts.md, tal cual se envió.

Tiene que ser silencioso: en este evento, lo que se imprime por la salida estándar se añade al
contexto del modelo. Nunca bloquea el prompt: ante cualquier error sale con 0 sin escribir nada.

El evento no trae modelo ni esfuerzo, así que los lee del último JSON que guardó la statusline
(.claude/statusline.sh). Son los del turno anterior: tras un /model o /effort, el primer prompt
puede quedar con los valores de antes. La columna «Qué salió» se rellena a mano.
"""
import json
import os
import re
import sys

STATUSLINE_JSON = "/tmp/claude-statusline-last.json"

# UserPromptSubmit también salta con mensajes que no escribe la persona: informes de subagentes
# y avisos de tareas en segundo plano. Llegan envueltos en estas etiquetas.
NOT_TYPED = ("<agent-message", "<task-notification")


def model_label():
    try:
        with open(STATUSLINE_JSON) as f:
            data = json.load(f)
    except (OSError, ValueError):
        return "desconocido"
    name = (data.get("model") or {}).get("display_name") or "desconocido"
    name = re.sub(r"\s*\((\S+) context\)", r" \1", name)
    effort = (data.get("effort") or {}).get("level")
    return "%s %s" % (name, effort.capitalize()) if effort else name


def main():
    prompt = json.load(sys.stdin).get("prompt", "")
    if not prompt.strip() or prompt.lstrip().startswith(NOT_TYPED):
        return

    path = os.path.join(os.environ["CLAUDE_PROJECT_DIR"], "prompts.md")
    with open(path) as f:
        content = f.read()

    numbers = [int(n) for n in re.findall(r"^## Prompt (\d+)$", content, re.MULTILINE)]
    number = max(numbers, default=0) + 1

    # La valla del bloque tiene que ser más larga que cualquier tirada de backticks del prompt.
    longest = max((len(run) for run in re.findall(r"`+", prompt)), default=0)
    fence = "`" * max(3, longest + 1)

    entry = (
        "\n## Prompt %d\n\n**Modelo:** %s\n**Herramienta:** Claude Code\n\n%s\n%s\n%s\n\n**Qué salió:**\n"
        % (
            number,
            model_label(),
            fence,
            prompt.rstrip("\n"),
            fence,
        )
    )
    with open(path, "a") as f:
        f.write(entry)


try:
    main()
except Exception:
    pass
sys.exit(0)
