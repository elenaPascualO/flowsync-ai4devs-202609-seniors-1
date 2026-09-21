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

## Prompt 13

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
Mira el proyecto y dime que capabilities ya hay construidas junto con el modelo de datos. Centrate en la fucnionalidad, no incluyas detalles tecnicos ni endpoints. La salida debe de ser un documento resumen de lo que hay hecho que me va a servir de base para hacer el PRD (product requirements document)
```

**Qué salió:** resumió las capabilities del proyecto (solo auth de usuario) y el modelo de datos (usuarios/sesiones) de forma centrada en funcionalidad, listo para el PRD. (3 herramientas)

## Prompt 14

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
hazme las cinco preguntas que más reducirían la incertidumbre sobre el problema, los usuarios y el alcance. No bajes al modelo de datos ni a los endpoints, mantente estrictamente en capa funcional, no entres en especificaciones tecnicas. El objetivo es acotar el alcance y el no alcance
```

**Qué salió:** generó 5 preguntas clave para acotar FlowSync sin bajar a técnico, cada una con su impacto de alcance; propuso un ciclo para llenar la ficha de hechos. (0 herramientas)

## Prompt 15

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
Esta es la ficha de hechos:
- Qué duele hoy: la daily de sincronización y el "¿en qué estás?" constante por Slack/chat. Nadie ve el estado del equipo sin interrumpir a alguien.
- Quién cobra el valor: los pares, no un lead. No hay reporte hacia arriba y a un manager le daría igual. Duele a los dos devs que descubren tarde que iban a lo mismo, y al que interrumpe a otro para preguntar.
- Episodio concreto: dos personas del equipo tocaron el mismo módulo la misma semana porque una empezó sin que la otra lo supiera. Dos días perdidos.
- Qué reunión desaparece (respuesta honesta, no la vendas de más): la daily NO desaparece entera. Desaparece la ronda de "¿en qué estás?", que hoy se come la mitad de los 15 minutos. La parte de bloqueos sigue, y este MVP no la resuelve.
- Usuarios / equipo: equipos remotos pequeños, 3–10 personas. Roles planos: en el MVP todos ven y editan lo mismo, sin jerarquía de permisos.
- Primer usuario concreto: equipo de 6 personas de producto SaaS, en 3 husos horarios, que hoy usa un gestor de tareas pesado y una daily de 15 minutos por videollamada. Es un CASO DE ESTUDIO, no un cliente real.
- Fronteras: un espacio único compartido, sin entidad "equipo". Varios equipos separados, o gente en más de uno, queda FUERA del MVP: se anota como supuesto en el PRD, no se construye.
- "Tiempo real" = ver los cambios de estado de las tareas sin refrescar ni preguntar. NO es chat, NO es videollamada, NO es colaboración simultánea sobre el mismo documento.
- Es frescura, no presencia: el estado es de la TAREA, no de la persona. Nada de "quién está conectado ahora" ni indicadores de actividad; eso es vigilancia y lo rechazamos a propósito.
- Forma de la señal: resumen que espera, no aviso que interrumpe. El caso es "llego por la mañana o vuelvo de una reunión y veo qué se ha movido". Sin notificaciones push.
- Qué decisión cambia: no empezar algo que otra persona ya está tocando, y elegir lo siguiente sabiendo qué está libre. Si la única respuesta fuera "sentirse informado", el tiempo real no valdría lo que cuesta.
- De dónde sale el estado: lo teclea la persona que hace la tarea, en segundos. Derivarlo de señales externas (Git/PRs, CI, calendario) está FUERA del MVP: es otro producto, con integraciones y OAuth de terceros.
- Por qué se sostiene: no porque sea más agradable, sino porque son dos clics sobre una lista ya abierta, sin campos obligatorios, sin decidir sprint ni estimación. Y quien lo escribe cobra en el momento: esa misma lista es su cola de trabajo, la mira para decidir qué coge, y de paso deja de recibir interrupciones preguntándole cómo va. Si el beneficio fuera solo para los demás, no lo escribiría.
- Si la información se queda vieja: el producto pierde el sentido, y lo asumo. Es el riesgo #1 a validar, no un detalle. La mitigación es que actualizar cueste dos clics, no obligar a nadie.
- Es donde se hace el trabajo, no donde se cuenta: sustituye al gestor de tareas, no convive con él. FlowSync crea las tareas, no lee las de otro sitio. Convivir exigiría doble actualización, que es como muere esta categoría.
- Renuncia explícita a sprints, estimaciones, épicas, backlog priorizado e informes. Un equipo que necesite eso no es nuestro usuario.
- "Menos rollo que Jira" = crear una tarea y cambiarle el estado en segundos, sin flujos de configuración ni campos obligatorios. Lo mínimo para saber quién está en qué.
- Qué necesita una tarea en el MVP: título, responsable, estado y fecha de vencimiento. La fecha, para ver de un vistazo qué se ha pasado de plazo.
- Cómo se consume la lista: filtrando por estado, para centrarse en lo pendiente.
- Éxito para el usuario: dejar de hacer la ronda de "¿en qué estás?" de la daily porque el estado del equipo se ve de un vistazo.
- Criterio a una semana de uso real: que el equipo cancele esa ronda y nadie pida que vuelva. Si la siguen haciendo igual, no funcionó.
- Cuánto construir: una vertical fina y usable de punta a punta, no el andamiaje amplio de un producto. Prefiero una capability terminada a tres a medias.
```

**Qué salió:** estructuró el PRD con Alcance claro (7 features: crear, filtrar, cambios en vivo, marca de nuevos) y NO-alcance razonado de 16+ exclusiones; sugirió qué priorizar si necesario. (0 herramientas)

## Prompt 16

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
esto queda fuera del mvp: 
- Fuera del MVP: notificaciones push, integración con Slack, roles/permisos avanzados, analítica/reporting, comentarios en tareas.

Rehaz el alcance con esta informacion nueva si aplica
```

**Qué salió:** rehizo el bloque NO-alcance identificando que solo Slack era nuevo; reorganizó en dos secciones con argumentación clara: descartado vs. recortado. (0 herramientas)

## Prompt 17

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
genera el documento docs/prd/alcance-mvp-epo.md y guarda el contenido del alcance entero, excepto tus sugerencias sobre mis recortes
```

**Qué salió:** generó `docs/prd/alcance-mvp-epo.md` en rama nueva sin sus sugerencias; quedó a medias porque faltan Parte B y commit. (2 herramientas, 1 fichero editado)

## Prompt 18

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
en la parte de alcance:
- numero 5: donde se sugiere que las tareas vencidas se destaquen? por que no las libres? la opcio de destacar tickets por un estado cubre algun dolor exlpicito que los usuarios tiene o es un nice to have?
- numero 7: es ralmente necesario para el mvp?
```

**Qué salió:** analizó si dos features debían estar en el MVP (#5 destacar vencidas, #7 marca de cambios), concluyó que ambas son nice-to-have sin dolor explícito, y propuso excluirlas del alcance. (0 herramientas)

## Prompt 19

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
Vamos a analizar tb la funcionalidad numero 6, por que la decidiste incluir en el alcance? que quieres decir con los cambios de los demas?
```

**Qué salió:** explicó qué significa "cambios de los demás", justificó la funcionalidad 6 por la definición de la ficha, argumentó a favor y en contra, y propuso una redacción más precisa (0 herramientas)

## Prompt 20

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
anade la 5 y la 7 en la parte B del documento, tal y como dice el README y deja la 6 en la parte A pero anadela tb en la parte B como la funcionalidad que mas duda me genera, ademas, necesito que anadas al final de la parte B que tu razonamiento sobre funcionalidad 6 es correcto para mi, aunque hay que redactarla mejor
```

**Qué salió:** añadió la Parte B tal como pidió pero detectó inconsistencias que dejó pendientes: falta una exclusión, ambigüedad sobre si la 6 entra o sale, e incoherencia en la Parte A. (1 herramienta)

## Prompt 21

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
/commit
```

**Qué salió:** completó commit en `alcance-epo` con dos ficheros nuevos, pero se quedó a medias: Parte B pendiente y `prompts.md` incompleto. (3 herramientas)

## Prompt 22

**Modelo:** Opus 5 High
**Herramienta:** Claude Code

```
te has equivocado. Necesito que borres la rama que has creado alcance-epo, vuelvas a s2/start y hagas commit y push en ella, luego crea una rama alcalce-epo en local a partir de upstream/s2/start y le anadas el fichero prompts.md y docs/prd/alcance-mvp-epo.md. La rama alcance-epo solo debe de llevar el prompts y el alcance, nada mas
```

**Qué salió:**
