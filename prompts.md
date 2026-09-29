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
el prompt 2 de prompts.md no tiene que estar ahi, no es un prompt mio
```

**Qué salió:** limpió prompts.md removiendo el prompt 2 ajeno, implementó filtro en hooks y test para evitar que vuelva a ocurrir, commiteó y pusheó cambios a PR. (4 herramientas)

## Prompt 2

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
que specs del backlog estan implementadas y cuales no? y que codigo implementado tiene specs y que no?
```

**Qué salió:** analizó backlog vs código implementado; E1 (auth) está hecha pero sin historias en `backlog/`, E2-E3 sin código: cero solapamiento. (4 herramientas)

## Prompt 3

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
que diferencia hay entre los dos documentos de la carpeta prd?
```

**Qué salió:** explicó que `alcance-mvp.md` es el acuerdo y `flowsync-mvp.md` el PRD derivado, detalló contenidos, jerarquía y secciones relevantes para el ejercicio; exhaustivo pero muy preciso. (1 herramienta)

## Prompt 4

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
entonces tengo que crear 4 archivos del tipo us-xxxx.md con la spec, al igual que los archivos que existen dentro de las epicas backlog/EX?
```

**Qué salió:** corrigió que es un archivo `docs/spec-viva/<iniciales>.md` (no 4 como historias), explicó diferencias entre historias de usuario y specs vivas, mostró tabla comparativa y el esqueleto con Purpose, Requirements y análisis posterior. (1 herramienta)

## Prompt 5

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vamos a trabajar en esta rama y cuando terminemos, creamos la rama oficial tan solo con los archivos prompts.md y docs/spec-viva/epo.md
```

**Qué salió:** reformuló el plan de trabajo en rama, descubrió que `prompts.md` acumula ya entradas del hook, y pidió al alumno decidir qué prompts van a la rama oficial. (1 herramienta)

## Prompt 6

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
- incluimos todos los prompts tal cual estan ya. Ayudame a resoler primero estas dudas: 
  - para hacer las specs, no es mejor primero recoger a nivel funcional (entiendo que el user story) que hace el codigo de la     vertical E1? o es normal ir directamente a hacer las specs?
  - en un archivo de spec, se mezclan requisitos del backend y del frontend?
```

**Qué salió:** recomendó un inventario antes de spec en lugar de historias de usuario, y explicó cómo mezclar backend/frontend agrupados por flujo. (0 herramientas)

## Prompt 7

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
antes de seguir, como podemos deducir el "para qué" de las funcionalidades extraidas de un proyecto brownfield?
```

**Qué salió:** dijo dónde buscar el "para qué": personas, documentación, historial, tests, código y uso real, en orden de fiabilidad; y qué hacer (anotar dudas) cuando no se encuentra. (0 herramientas)

## Prompt 8

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
puedes darme un ejemplo de ese "para qué" en la user story us-filtrar-estado, por ejemplo?
```

**Qué salió:** buscó la historia de estado, explicó el «para qué» en dos niveles y enseñó a diferenciar decisiones deliberadas de olvidos cuando resultan en código idéntico. (1 herramienta)

## Prompt 9

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
para que sirve el "para qué"?
```

**Qué salió:** explicó conceptualmente para qué sirve el "para qué" con cinco puntos y casos reales; demasiado texto de una vez. (0 herramientas)

## Prompt 10

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
empecemos con el inventario de la vertical E1
```

**Qué salió:** inventarió autenticación (signup, login, sesión, perfil, logout); mapeó APIs y rutas, flagó inconsistencias: logout sin `{ data }`, email case-sensitive, token eterno, iniciales de email, contraseña ilimitada. (2 herramientas)

## Prompt 11

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
es necesario resolver los  ⚠️ ejecutnado para crear las specs?
```

**Qué salió:** explicó que ejecutar no es obligatorio y pasó tres opciones (comprobar con curl, escribir igualmente, dejar fuera de spec) con tabla de `⚠️` mapeados a acciones concretas. (0 herramientas)

## Prompt 12

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
entonces los dejamos para la lista tres.
Empecemos escribiendo las specs. Hay que hacer una por RF?
```

**Qué salió:** aclaró que la spec es un único archivo por capability agrupado por flujos (no por RF), explicó el razonamiento, y empezó a escribir `spec-viva` con Purpose y el flujo de registro. (1 herramienta, 1 fichero editado)

## Prompt 13

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
voy a ir a revisar en el codigo lo tres requisitos que has sacado. Me indicas de donde has sacado cada escenario?
```

**Qué salió:** trazó cada requisito a líneas concretas en `backend/` y `frontend/`, señaló las asunciones de framework con ⚠️ y advirtió al alumno qué verificar directamente en el código. (1 herramienta)

## Prompt 14

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vamos requisito a requisito y escenario por escenario. Hay algunos escenarios que no son requisitos, son bugs o huecos funcionales que no deberian de ser requisitos, o que son duda. El objetivo es ir creando las tres listas
```

**Qué salió:** propuso criterio de clasificación (contrato/bug/duda) y procesó Requirement 1 identificando la duda del nombre opcional; respuesta a medias esperando confirmación (0 herramientas)

## Prompt 15

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
en realidad todo va a spec y las listas son para remarcar las incoherencias (lista 2) y las dudas (lista 3), no?
```

**Qué salió:** corrigió su interpretación anterior: la spec describe el sistema tal como es, y las listas marcan incoherencias y dudas; añadió la sección Parte B al archivo. (1 herramienta)

## Prompt 16

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
añádelas tal cual y pasamos al requisito 3
```

**Qué salió:** añadió las tres entradas y analizó registro; halló 3 contratos, 2 incoherencias de código (nombre en blanco y validación incompleta) y propuso 3 adiciones a listas. (1 herramienta)

## Prompt 17

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
para la lista 1, no he comprobado nada en el codigo yo directamente, lo he hecho con un agente, no entiendo typescript. Que seria lo mas adecuado? es realmente necesario invertir tiempo en revisar manualmente el codigo?
```

**Qué salió:** propuso probar desde el navegador en lugar de leer TypeScript, justificó reportar 0 comprobados si es así, e indicó cómo automatizar pruebas de API con curl. (0 herramientas)

## Prompt 18

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
vale, y si lanzamos varios tests e2e para comprobar lo sacado por el agente?
```

**Qué salió:** explicó por qué tests e2e vale para verificar, estableció tres condiciones (fuera del repo, aserciones revisadas, documentación), propuso curl y Playwright, pidió confirmar servidor antes de escribir aserciones (0 herramientas)

## Prompt 19

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
no quiero que escribas los e2e, sino que lances un subagente para que los vaya lanzando al vuelo. A partir del siguiente flujo, inicio de sesion, al recorrerlo por requisitos, comprueba con un e2e cada escenario y me lo sacas junto con el resto, etiendes ?
```

**Qué salió:** lanzó subagente e2e que verificó 10 escenarios del login con curl/Playwright; todos pasaron; descubrió incoherencia de seguridad (login oculta cuenta existente, signup la revela); recomendó añadir códigos HTTP a spec. (10 herramientas)

## Prompt 20

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí a las tres, lanza también las del registro
```

**Qué salió:** ejecutó E2E del registro (11 escenarios), identificó una entrada falsa en lista 2 (nombre en blanco), confirmó otras y extrajo 4 nuevos hallazgos. (2 herramientas)

## Prompt 21

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, aplica todo y sigue con persistencia de sesión
```

**Qué salió:** aplicó cambios en las listas, definió especificación de persistencia con 4 requisitos y 8 escenarios, y lanzó subagente para pruebas E2E; a medias, esperando resultados. (3 herramientas)

## Prompt 22

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, aplica todo y sigue con perfil y cierre de sesión
```

**Qué salió:** aplicó las cuatro entradas, elaboró spec de perfil y cierre de sesión con 15 requisitos y 11 escenarios cumplidos, y el subagente identificó bugs con espacios duplicados, emojis rotos, nombre sin límite de longitud y token vigente tras logo (3 herramientas)

## Prompt 23

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, aplica todo y sigue con protección de rutas
```

**Qué salió:** aplicó entrada, agregó protección de rutas (4 requisitos, 7 escenarios), lanzó subagente E2E; 19 requisitos en total, pendiente. (2 herramientas)

## Prompt 24

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, escríbela y crea la rama a partir de upstream/s3/start y anade solo el archivo prompts.md y el docs/spec-viva/epo.md
```

**Qué salió:** escribió la lista 1 (19 requisitos, 47 escenarios comprobados con e2e, 0 leyendo el código), comprobó que la spec no nombra archivos ni clases y creó la rama `spec-viva-epo` desde `upstream/s3/start` con solo los dos archivos en stage.

## Prompt 25

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
sí, borra el ejemplo y haz commit, push y PR
```

**Qué salió:** borró el prompt de ejemplo de la plantilla, completó a mano este registro (en la rama de entrega no está el hook que lo rellena), hizo commit, push al fork y abrió el PR contra el repositorio del curso.
