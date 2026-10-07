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

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
lee el readme de root del repo del ejercicio para que tengas contexto. No ejecutes nada ni propongas nada aun, solo lee el README para que tengas el contexto
```

**Qué salió:** leyó el `README.md` y resumió la tarea (matriz, tests, tres líneas, entrega) sin ejecutar ni proponer nada.

## Prompt 2

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
empieza construyendo la matriz de trazabilidad vacia del requisito que piden: «Lo que cada tarea muestra de su responsable» . Tiene tres escenarios por lo que la matriz debe de tener 3 filas y cuatro columnas, segun el formato dado en el ejercicio. Creala en el archivo docs/verificacion/epo.md, como dice la parte B
```

**Qué salió:** creó la rama `trazabilidad-epo` y `docs/verificacion/epo.md` con los dos números arriba, las 3 filas con el scenario en una línea y el resto vacío, y los huecos de la parte B.

## Prompt 3

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
la columna "prueba que lo cubre" ha de llamarse  "test que lo cubre", por que le has puesto "prueba"?
```

**Qué salió:** renombró la columna a «Test que lo cubre»; «prueba» venía del README («Qué prueba lo cubre»), no fue un cambio a propósito.

## Prompt 4

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vamos a recorrer los escenarios uno a uno para ver que tests deberian de tener para verse totalmente cubierto y a continuacion, que tests existen. Escenario por escenario, cada paso debe de ser aprobado por mi antes de pasar al siguiente
```

**Qué salió:** desglosó qué tendría que comprobar un test del scenario 1 (lista y tarea suelta, nombre e iniciales exactos) y señaló dos huecos: qué iniciales esperar y si `POST`/`PATCH`/`PUT` cuentan como «obtener».

## Prompt 5

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
Tenemmos que cubrir los huecos de spec en la matriz tb o se sale del alcance del ejericio?
```

**Qué salió:** aclaró que los huecos de spec no se arreglan: se anotan en la columna 4 si impiden decidir el estado, o en las líneas 2 y 3 de la parte B.

## Prompt 6

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, ahora busca qué tests existen para el escenario 1
```

**Qué salió:** no encontró ningún test de `tasks`; el de iniciales de `auth` mira el login, no la tarea, pero confirma que «AL» lo fija la spec de `auth`. Propuso «No cubierto».

## Prompt 7

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
Fijate en el ejericio de nuevo, que esta en el README, y lee la parte A entera porque ademas de rellenar la matriz, hay que hacer los tests que faltan y ejecutarlos y observar el resultado. Vamos a estructurar el recorrido de cada esceneario con lo que se pide y no se pasa al siguiente hasta que este completado
```

**Qué salió:** rehízo el recorrido en 5 pasos por scenario (qué comprobar, qué existe, fila, test, ejecutar) y corrigió su propuesta: un test por scenario, no dos.

## Prompt 8

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, escribe la fila y el test del escenario 1
```

**Qué salió:** escribió la fila «No cubierto» y `backend/tests/functional/tasks/assignee.spec.ts` con el test del scenario 1; en verde.

## Prompt 9

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
si, apruebo el escenario 1, pero nos falta aun la columna "Si «no lo sé», qué faltó" por rellenar
```

**Qué salió:** explicó que la columna 4 solo se rellena con «No lo sé» y propuso poner «—» para que no pareciera olvidada.

## Prompt 10

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, pon «—» y pasa al escenario 2
```

**Qué salió:** puso «—» y planteó el scenario 2 con una lista blanca de claves (`id`, `fullName`, `initials`), avisando de que el `id` lo decidía él y de que la lista probablemente saldría roja.

## Prompt 11

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
para la lista blanca, tomariamos una decision basada en un hueco de spec no?
```

**Qué salió:** distinguió: la lista blanca sí sale del requisito («ningún otro dato»), el hueco es solo el `id`; propuso ceñir el test al scenario (sin email ni datos de acceso) y llevar el `id` a la parte B.

## Prompt 12

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, déjalo así y pasa al paso 2
```

**Qué salió:** no encontró ningún test; el de la contraseña de `signup` comprueba otra respuesta. Propuso «No cubierto».

## Prompt 13

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
si
```

**Qué salió:** escribió la fila y el test del scenario 2: rojo, la lista expone `email` en `assignee`. Avisó de que el bucle no llega a comprobar la tarea suelta y ofreció separar las comprobaciones.

## Prompt 14

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
no, eso seria tocar el test que has escrito originalmente no?
```

**Qué salió:** me dio la razón: separar sería reescribir el test después de verlo rojo; lo dejó como estaba y cerró el scenario 2.

## Prompt 15

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, pasa al escenario 3
```

**Qué salió:** planteó el scenario 3 (`fullName` nulo e iniciales «AE», sacadas de la spec de `auth`) y señaló un choque: las iniciales salen del email que el scenario quiere evitar.

## Prompt 16

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, pasa al paso 2
```

**Qué salió:** no encontró ningún test; los de `auth` comprueban cada mitad, pero en el login y el registro, no en la tarea. Propuso «No cubierto».

## Prompt 17

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, escribe la fila y el test del escenario 3
```

**Qué salió:** escribió la fila y el test del scenario 3: verde; suite completa con 22 verdes y 1 rojo (el del scenario 2).

## Prompt 18

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, cierra el escenario 3 y pasa a la parte B
```

**Qué salió:** propuso «Cubiertos: 0» y pidió mi estimación previa en vez de inventarla.

## Prompt 19

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
CReia que estaban cubiertos todos pero no he mirado el codigo, ha sido intuicion
```

**Qué salió:** escribió «Creía cubiertos: 3 · Lo estaban: 0» y propuso tres candidatos para la línea 2, recomendando el del `id` en el scenario 2.

## Prompt 20

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
la b
```

**Qué salió:** escribió la línea 2 con la b) y propuso tres candidatos para la línea 3, recomendando qué cuenta como «dato de acceso».

## Prompt 21

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, la a, el spec no especifica cuales que se considera datos de acceso en este requisito.
```

**Qué salió:** escribió la línea 3 con mi matiz; revisó `prompts.md` y propuso borrar el ejemplo, renumerar, añadir el prompt del README y revisar los «Qué salió» de Haiku.

## Prompt 22

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, haz el 1 y el 2 y arregla los "que salio" que haiku ha escrito
```

**Qué salió:** completó cambios 1 y 2 en `prompts.md` con 22 prompts numerados y corrigió los 20 resúmenes «qué salió» con descripciones precisas desde tu perspectiva; el prompt 22 quedó vacío para rellenar por el hook. (3 herramientas)

## Prompt 23

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
si, pero tienes que comitear y pushear a mi fork desde otra rama, la que pide el ejercicio "trazabilidad-epo", se dice en el punto 8 del enunciado
```

**Qué salió:**
