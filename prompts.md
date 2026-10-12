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

---

## Prompt 1

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
lee el ejercicio de esta rama conetenido en ./README.md. Solo lee para qe tengas el contexto
```

**Qué salió:** leyó el enunciado y avisó de que commitear los hooks en la rama de entrega metería ficheros de más en el PR.

## Prompt 2

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
crea una tabla con las 5 reglas de proceso escritas en CLAUDE.md al final como filas y 5 columnas: Que pide la regla, Que se reviso para comprobarla, veredicto, Evidencia, que harias con ella. Solo la estructura de la tabla, el contenido despues, creala an auditoria/epo.md
```

**Qué salió:** creó la tabla vacía en `docs/auditoria/epo.md`, pero se cambió por su cuenta a una rama `auditoria-epo` sin preguntar.

## Prompt 3

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
perdon, 6 columnas, adande una primera columna con el titulo "regla"
```

**Qué salió:** añadió la columna «Regla» con R1-R5 como identificador de cada fila.

## Prompt 4

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vamos a rellenar la columna 1:
- R1: Crea rama nueva por unidad de trabajo antes de tocar codigo si estas en main o sN/*. Si no estas en esas ramas, continua en la que estas y nunca commitees en main ni sN/*.
- R2: Comitea con skill /commit al terminar unidad de trabajo
- R3: Si la unidad de trabajo es sobre rutas, controladores, validadores o transformers de una capability, actualiza openapi y README de esa capability y anade esos cambios al commit tambien.
- R4: crear PR con gh pr create con cada commit incliyendo una descripcion completa de los cambios en el cuerpo del PR y lanza el agente adversarial-review al final.
- R5: Al abrir PR rsepone solo con la url del mismo, el resto va en la propia PR.
```

**Qué salió:** rellenó «Qué pide la regla» con mis frases y señaló que en R2 y R4 tenía intercambiados petición y unidad de trabajo.

## Prompt 5

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
- R2: una undad de trabajo incluye varios cambios de codigo o solo uno? el fin de una unidad de trabajo lo establece el usuario no? y ahi es cuando hay que crear el commit. COmo sabe el agente cuando la unidad de trabajo esta terminada? 
- R4: hay incoherencias entre unidad de trabajo, cambios y commits, no entiendo las reglas
```

**Qué salió:** explicó la diferencia: petición = un commit, unidad de trabajo = una rama y un PR; y que nada define cuándo termina una unidad.

## Prompt 6

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
entonces una unida de trabajo puede contener varios cambios con sus commits
```

**Qué salió:** lo confirmó con un esquema de una rama con tres commits y un PR al final.

## Prompt 7

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
entonces, rehago la descripcion de las reglas 2 y 4:
- R2: Haz un commit despues de terminar cada peticion.
- R4: Crear PR con "gh pr create" que contea una descripcion de todos los cambios en su cuerpo, y lanza el agente adversarial-reivew al final. Haz esto al final de cada unidad de trabajo.

Duda: como sabe el agente que la unidad de trabajo esta terminada?
```

**Qué salió:** actualizó R2 y R4; avisó de que R2 ya no mencionaba `/commit` y de que el agente no puede saber cuándo acaba una unidad de trabajo.

## Prompt 8

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
Cambia R2 de "Haz un commit después de terminar cada petición." a Haz un commit después de terminar cada petición con /commit
```

**Qué salió:** cambió la frase de R2 para incluir `/commit`.

## Prompt 9

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
Ahora contrasta las reglas con los últimos 15 commits del repositorio y el estado actual de los archivos del proyecto
```

**Qué salió:** rellenó qué se revisó, veredicto y evidencia con git y `gh` sin tocar otros ficheros: R3 se cumple, R4 no, R1, R2 y R5 no se pueden comprobar.

## Prompt 10

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
por que no se estan escribiendo los prompts autolaticamente?
```

**Qué salió:** los hooks no estaban en la rama actual; propuso activarlos con `settings.local.json` y `.git/info/exclude` para no ensuciar la entrega.

## Prompt 11

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
por que estas en la rama auditoria-epo? estabamos en s5/start y no te he dicho que te cambies
```

**Qué salió:** reconoció que había cambiado de rama sin preguntar y ofreció deshacerlo.

## Prompt 12

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vamos a rellenar la ultima columna "que harias con ella":
R1: Me inclino por crear una regla en un hook pero saldria caro comprobar cada peticion y commit. No se como proteger las ramas main y sN/* en local y barato. Igual basta con poner una regla en github que prohiba push a main y sN/*
R2: Creo que me he equivocado con la descripcion de la regla, no es commit por peticion sino por peticion de cambio de codigo no? Y en cuanto a qué haria, crear un commit por peticion de calbio de codigo es demasiado ruido. Y un hook que lance commit por cada cambio de mas de X lineas de codigo?
R3: esta regla la dejaria tal cual y la reforzaria en un hook y en CI
R4: Esta la quitaria porque es dificil para un agente saber cuando el usuario ha terminado una unidad de trabajo, crearia una skill que ejecute los pasos de la regla
R5: La quitaria y la meteria como paso dentro del skill de la R4
```

**Qué salió:** rellenó la columna con bajar o borrar en cada regla y resolvió las dudas: un hook local barato para proteger ramas, R2 ambigua pendiente de confirmar y R4 y R5 borradas por depender de disparo manual. (1 herramienta)

## Prompt 13

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
VAmos con la parte B del ejericio, no rellenes nada por tu cuenta, propon y pregunta mi criterio
```

**Qué salió:** se pidió a la alumna empezar la parte B del ejercicio sin rellenar nada por su cuenta: el asistente propuso ir línea a línea, empezó por la regla 1 y preguntó si había apuntado una apuesta previa, sin escribir ninguna. (0 herramientas)

## Prompt 14

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
Lo apunte en otro sitio: dije que todas las reglas se cumplian excepto la 2 porque no entendi bien que era peticion, pensaba que el agente comiteaba tras cada peticion, fuera de codigo o no
```

**Qué salió:** sin usar herramientas, contrastó la apuesta del alumno con los veredictos de la tabla, señaló R4 como único desacuerdo, propuso R1 y R5 como alternativa y dejó dos preguntas abiertas. (0 herramientas)

## Prompt 15

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
si, anade la respuestas deabjo de la tabla
```

**Qué salió:** el asistente añadió la apuesta del alumno debajo de la tabla con una nota de que se escribió antes del resultado, y dejó entre paréntesis en R2 el motivo que dio el alumno; para seguir con la línea 1 le pidió que eligiera la regla (R4, la ú (1 herramienta)

## Prompt 16

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
perdon, mi apiuesta va encima de la tabla, el enunciado es confuso, dice que las tres lineas van debajo de la tabla y despues que mi expectativa tiene que estar escrita antes de la tabla, pero no veo donde en el enunciado dice que debo de apuntar mi expectativa encima de la tabla
```

**Qué salió:** el alumno preguntó dónde exige el enunciado anotar su expectativa; el asistente explicó que «escrita antes» se refiere al momento y no al lugar, dijo que las tres líneas de la parte B van debajo de la tabla, y movió la apuesta encima de la (1 herramienta)

## Prompt 17

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
La regla en la que mas me equivoque fue en la R2 y en el resto, me basé en que las regla eran comprobable con guardarails baratos
```

**Qué salió:** el alumno apostó en R2 y en el resto de reglas que eran comprobables con guardarraíles baratos, pero el asistente le señaló que en el repo no hay ninguno, y que en R2 se equivocó al interpretar la regla (creía que se commiteaba tras cada pe (0 herramientas)

## Prompt 18

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
déjala así y pasamos a la línea 2
```

**Qué salió:** añadió la línea 1 debajo de la tabla y propuso dos candidatas para la línea 2 (R2, que `/commit` deje un trailer, o R5, que ya queda registrada en `prompts.md`), y pidió al alumno que eligiera. (1 herramienta)

## Prompt 19

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
LA 2
```

**Qué salió:** se pidió una sola línea de resumen del turno, así que no hace falta tocar nada ni invocar herramientas. El turno fue una pregunta de aclaración: el alumno escribió «LA 2» y el asistente no ejecutó nada, sino que preguntó si se refería a la (0 herramientas)

## Prompt 20

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
la regla 2
```

**Qué salió:** añadió con Bash una segunda línea a la regla 2 y propuso borrar R4 por no cumplirse nunca, pidiendo confirmación; R5 quedó sin resolver, así que el turno quedó a medias. (1 herramienta)

## Prompt 21

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
déjala así con R4
```

**Qué salió:** añadió la línea 3 con R4 a `docs/auditoria/epo.md` y dio por cerrada la parte B; quedan pendientes que el alumno compruebe una fila en el historial y la rama y el PR, y preguntó si los hace él. (1 herramienta)

## Prompt 22

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
quiero comprobar la R3
```

**Qué salió:** dio cuatro comandos de `git` para comprobar la R3 sin ejecutar ninguno, pidiendo al alumno que los lanzara con `!`; la comprobación queda a medias hasta que pegue la salida. (0 herramientas)

## Prompt 23

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vale, crea la rama auditoria-epo y anade el archivo prompts y docs/auditoria/epo.md
```

**Qué salió:** creó la rama `auditoria-epo` y dejó en stage `docs/auditoria/epo.md` y `prompts.md` sin commitear; al revisar el registro de hooks detectó un prompt perdido entre el 11 y el 12 y preguntó si lo inserta. (2 herramientas)

## Prompt 24

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
commitea y haz push a mi fork y abre PR contra s5/start del repo del curso
```

**Qué salió:**
