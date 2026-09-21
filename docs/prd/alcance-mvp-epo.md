# Alcance del MVP de FlowSync

## Parte A

### 1. El terreno que ya existe

FlowSync es por ahora solo la base: gestiona cuentas de usuario y nada más. Una persona puede registrarse, iniciar sesión, mantener la sesión abierta, ver su perfil (nombre, email, iniciales y fecha de alta) y cerrar sesión. El modelo de datos tiene solo dos conceptos: el usuario (nombre opcional, email único, contraseña) y sus sesiones abiertas. No hay tareas, ni equipos, ni ninguna forma de ver en qué trabaja cada persona: la propuesta de valor está por construir entera.

### 2. El interrogatorio

1. ¿Qué reunión o qué momento concreto tiene que desaparecer, y cómo sabremos que ha funcionado?
2. ¿Quién es el usuario principal y quién consulta la información: un equipo de iguales o un responsable que necesita la visión de todos? ¿De qué tamaño es un equipo típico?
3. ¿Qué significa "en tiempo real" para este equipo: ver el cambio al instante, enterarse durante el día o tenerlo listo al empezar la jornada? ¿Hay husos horarios distintos?
4. ¿De dónde sale la tarea y quién la crea: cada persona apunta lo suyo, alguien reparte el trabajo, o el trabajo ya vive en otra herramienta y FlowSync solo lo refleja?
5. ¿Qué de Jira es "rollo" y hay que evitar a propósito, y qué mínimo imprescindible tiene que tener una tarea para que sea útil?

Las respuestas son las de la ficha de hechos del ejercicio.

### 3. El alcance en cinco bloques

#### Problema

En los equipos remotos pequeños nadie puede ver en qué está cada uno sin interrumpir a alguien. Eso tiene dos costes:

- **Interrupciones constantes**: el "¿en qué estás?" por chat, y una ronda en la daily que se come la mitad de sus 15 minutos.
- **Trabajo duplicado**: dos personas se enteran tarde de que iban a lo mismo. En el caso real, tocaron el mismo módulo la misma semana y se perdieron dos días.

La parte de bloqueos de la daily sigue existiendo, y este MVP no la resuelve.

#### Usuarios

- **Quiénes son**: equipos remotos de 3 a 10 personas, de igual a igual, sin jerarquía. Todos ven y editan lo mismo.
- **Quién gana con el producto**: el desarrollador que va a empezar algo y necesita saber si otra persona ya lo está tocando, y el que hoy tiene que interrumpir para preguntar cómo va algo.
- **Quién no es el usuario**: un manager que quiere informes. No hay reporte hacia arriba.
- **Caso de estudio**: un equipo de producto SaaS de 6 personas en 3 husos horarios, con un gestor de tareas pesado y una daily de 15 minutos por videollamada.

#### Propuesta de valor

Una lista de tareas compartida que es a la vez la cola de trabajo de cada persona y el estado del equipo, siempre al día sin preguntar a nadie.

- **Quien la actualiza gana en el momento**: la usa para decidir qué coge y deja de recibir preguntas sobre cómo va lo suyo.
- **Quien la consulta** ve de un vistazo qué está ocupado, qué está libre y qué se ha movido.
- **La decisión que cambia**: no empezar algo que otra persona ya tiene y elegir lo siguiente sabiendo qué está libre.
- **Cómo se sabe si funciona**: tras una semana de uso real, el equipo cancela la ronda de "¿en qué estás?" y nadie pide que vuelva.

#### Alcance (lo que entra)

Una sola capability de principio a fin: **ver y actualizar quién está en qué**. Se apoya en el registro y el inicio de sesión que ya existen.

1. **Crear y editar una tarea** con título, responsable, estado y fecha de vencimiento. Solo el título es obligatorio.
2. **Tres estados fijos**: por hacer, en curso y hecha. El estado se cambia en dos clics desde la propia lista.
3. **Tareas libres**: una tarea sin responsable está libre, y cualquiera puede quedársela en un clic.
4. **Una única lista compartida** por todos los usuarios, filtrable por estado.
5. **Tareas vencidas destacadas**, para ver de un vistazo qué se ha pasado de plazo.
6. **Los cambios de los demás aparecen solos**, sin refrescar la página.
7. **Marca de "ha cambiado desde tu última visita"**, para cuando llegas por la mañana o vuelves de una reunión.

#### NO-alcance (lo que queda fuera y por qué)

**Descartado por decisión del producto:**

- **Notificaciones push, emails o avisos.** El problema de partida son las interrupciones. La información tiene que esperar a que la mires, no avisarte.
- **Integración con Slack.** Llevar los cambios al chat vuelve a meterlos en el sitio que interrumpe. Además, que la información se consulte en dos sitios separa el lugar donde se trabaja del lugar donde se cuenta. El estado se ve en FlowSync, y la gente va a mirarlo cuando lo necesita.
- **Roles y permisos, también los avanzados.** El equipo es plano y todos ven y editan lo mismo. Cualquier jerarquía añade pasos a una acción que tiene que costar dos clics.
- **Analítica e informes.** Nadie reporta hacia arriba y a un manager le daría igual. Lo que hay que validar se mide con una pregunta: ¿el equipo ha cancelado la ronda de "¿en qué estás?"?
- **Comentarios en las tareas.** Vuelven a meter la conversación que queremos quitar, y no hacen falta para saber quién está en qué.

**Recortado para acotar la validación:**

- **Varios equipos o espacios, y personas en más de uno.** Para validar que el estado se mantiene al día basta con un equipo. Se deja anotado como supuesto: hay un único espacio compartido.
- **Gestión de miembros e invitaciones.** Registrarse ya equivale a entrar en ese espacio único.
- **Ver quién está conectado o indicadores de actividad.** El estado es de la tarea, no de la persona. Enseñar la actividad de cada uno es vigilancia, y se rechaza a propósito.
- **Chat o edición simultánea de la misma tarea.** "Tiempo real" aquí significa que los cambios de estado se vean al día, no que se hable o se escriba a la vez.
- **Estado sacado de Git, pull requests, integración continua o calendario.** Eso es otro producto, con integraciones de terceros. El estado lo escribe la persona que hace la tarea.
- **Importar o sincronizar con otro gestor de tareas.** Obligaría a actualizar dos sitios, y así es como muere este tipo de producto. FlowSync sustituye al gestor, no convive con él.
- **Sprints, estimaciones, épicas y backlog priorizado.** Un equipo que necesite eso no es nuestro usuario.
- **Estados configurables o campos personalizados.** Es justo el "rollo" de Jira que queremos evitar.
- **Descripción, subtareas, etiquetas, prioridad y adjuntos.** Cada campo de más encarece actualizar, y el riesgo número 1 es que la información se quede vieja.
- **Registrar bloqueos.** Esa parte de la daily sigue existiendo y este MVP no la resuelve.
- **Tablero por columnas, vista por persona o calendario.** Con una lista filtrada por estado ya se ve quién está en qué.
- **Historial de cambios de cada tarea.** Para saber qué se ha movido basta con la marca de "ha cambiado desde tu última visita".
- **Borrar o archivar tareas.** Una tarea acabada se marca como hecha y se puede quitar de la vista con el filtro.
- **Editar el perfil, recuperar la contraseña o confirmar el email.** Ninguno ayuda a validar que la información se mantiene al día.

## Parte B

### 1. Los dos números

- La IA propuso meter **7** cosas dentro del alcance.
- Después de mi recorte quedan **5**.

### 2. Tres cosas que dejé fuera y por qué

1. **Destacar las tareas vencidas (número 5) fuera**, porque no ayuda a validar que el equipo deja de pisarse el trabajo ni de interrumpirse para preguntar: los plazos no aparecen en ninguno de los dolores. La fecha de vencimiento se queda como campo de la tarea; lo que sale es destacarlas.
2. **La marca de "ha cambiado desde tu última visita" (número 7) fuera**, porque no ayuda a validar que la lista cambia la decisión de qué coger: para eso basta con ver el estado actual. Saber qué se ha movido mientras no estaba es sentirse informado, y eso solo no justifica el coste.
3. _Pendiente._

### 3. La que más dudas me genera

**Ver los cambios sin recargar (número 6).** No la he excluido: se queda dentro del alcance, pero es la decisión de la que menos seguridad tengo. Es la más cara de las cinco, y el episodio real, dos personas en el mismo módulo, se desarrolló en días, no en segundos: una lista que se pone al día cada vez que se abre quizá habría bastado.

Qué tendría que pasar para sacarla: que en la semana de prueba nadie tenga la lista abierta durante horas, sino que se abra, se consulte y se cierre. En ese caso basta con que esté al día al abrirla.

### Nota sobre la funcionalidad 6

Doy por bueno el razonamiento de la IA para mantenerla: la lista es la cola de trabajo de cada persona y suele estar abierta durante horas, así que sin ver los cambios al momento alguien puede coger una tarea que un compañero acaba de quedarse, que es justo el dolor de trabajo duplicado. Aquí el tiempo real no sirve para sentirse informado, sino para no pisarse. Falta redactarla mejor en el alcance.
