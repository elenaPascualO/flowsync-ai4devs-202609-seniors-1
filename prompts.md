# Prompts

Aquí van **todos los prompts que lanzaste** para hacer el ejercicio, en el orden en que los
lanzaste, con el modelo y la herramienta de cada uno.

Esto no es papeleo. Lo que se revisa es **cómo pediste las cosas**, no solo lo que salió: un
resultado flojo con un prompt bueno y un resultado flojo con un prompt vago necesitan feedback
distinto, y sin este archivo no se distinguen.

## Cómo rellenarlo

- Un apartado `## Prompt N` por cada prompt.
- **Pega el prompt tal cual lo lanzaste**, dentro del bloque de código, aunque ocupe diez líneas
  y aunque tenga faltas. No lo reescribas para que quede bien: el que arreglaste mentalmente
  después no es el que lanzaste.
- Incluye también los que **no funcionaron**. Suelen ser los más útiles de leer.
- `Modelo` y `Herramienta` en todos. Si cambiaste de una a otra a mitad, se nota aquí.

Borra el ejemplo de abajo cuando escribas el primero.

---

## Prompt 1

**Modelo:** Opus 1M xHigh
**Herramienta:** Claude Code

```
Este es el ejemplo. Bórralo.

El prompt va aquí dentro, entero y con sus saltos de línea,
para que se sepa dónde empieza y dónde acaba.
```

**Qué salió:** (opcional, una línea) funcionó a la primera / tuve que insistir / me inventó una ruta que no existe.

## Prompt 2

**Modelo:** desconocido
**Herramienta:** Claude Code

```
ese hook debe de estar solo disponible para este repo
```

## Prompt 3

**Modelo:** desconocido
**Herramienta:** Claude Code

```
solo mio
```

## Prompt 4

**Modelo:** desconocido
**Herramienta:** Claude Code

```
si, trae statusline.sh
```

## Prompt 5

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
en el hook de log-prompts falta anadir la lineq de abajo "que salio". fijate en el primer log de ejemplo del archivo prompts.md
```

## Prompt 6

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
prueba de log de prompt
```

**Qué salió:**

## Prompt 7

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
quiero que lo rellenes tu en el hook, no yo a mano
```

**Qué salió:** creó hook `Stop` que rellena automáticamente Qué salió leyendo el transcript; testeó 5 casos y lo registró en settings.local.json. (13 herramientas)

## Prompt 8

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
olvidate de settings.local, vuelve a meter todo en settings.json para tenerlo en origin y poder hacer pull desde otro ordenador de la misma configuracion
```

**Qué salió:** fusionó `settings.local.json` en `settings.json` versionado pero advirtió sobre rutas absolutas no portables y aprobación MCP automática; quedó a medias esperando confirmación antes de commitear. (3 herramientas)

## Prompt 9

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
el que salio de los prompts no trae resumen, solo un dato muy escueto sin detallem fijae en el archivo prompts de la rama s1/start para que te hagas una idea de lo que se espera en a seccion "que salio"
```

**Qué salió:** reparó dos problemas del hook: lectura prematura del transcript (espera 20s) y síntesis sin criterio (modelo con ejemplos de tono); regeneró dos entradas. (11 herramientas)

## Prompt 10

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
por que quieres quitqr las rutas absoultas?
```

**Qué salió:** se retractó de quitar rutas absolutas tras análisis más profundo, reconoció que el argumento de privacidad era débil, y propuso eliminar en cambio `enabledMcpjsonServers` que aplica sin consentimiento a quien clona el repo. (0 herramientas)

## Prompt 11

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
/commit
```

**Qué salió:** commiteó exitosamente en `chore/prompt-log-hooks` los ficheros de configuración y hooks (limpiando `.pyc` del índice), pero quedó a medias: falta el `gh pr create` con el adversarial-reviewer que marca CLAUDE.md. (5 herramientas)

## Prompt 12

**Modelo:** Opus 5 1M High
**Herramienta:** Claude Code

```
me ayudas a entender el ejercicio de este modulo? esta en el README
```

**Qué salió:** leyó archivos (README y template) con bash pero respondió incompleto; solo prometió explicar sin hacerlo. (2 herramientas)
