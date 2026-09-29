# Cuentas y acceso

## Purpose

Permite que una persona cree una cuenta, inicie y cierre sesión, conserve la sesión entre visitas y vea su perfil, e impide el acceso a las zonas privadas sin una sesión válida.

## Requirements

### Requirement: Alta de cuenta

El sistema SHALL permitir crear una cuenta con email, contraseña y confirmación de contraseña, con el nombre como dato opcional, y SHALL devolver en la misma respuesta los datos de la persona y un token de acceso, de forma que quede autenticada sin ningún paso adicional.

#### Scenario: Registro con datos válidos

- **WHEN** se envía una petición de registro con un email no registrado, una contraseña de entre 8 y 32 caracteres y una confirmación idéntica
- **THEN** la respuesta es un 200 y contiene, dentro de `data`, los datos de la persona (identificador, nombre, email, iniciales y fechas de alta y actualización) y un token de acceso

#### Scenario: Registro sin nombre

- **WHEN** se envía una petición de registro válida con el nombre a `null`
- **THEN** la cuenta se crea igualmente y los datos devueltos tienen el nombre a `null`

### Requirement: Validación de los datos de registro

El sistema SHALL rechazar un registro con datos no válidos con un error 422 que indique, para cada problema, el campo afectado y la regla incumplida, y SHALL no crear la cuenta.

#### Scenario: Email con formato no válido

- **WHEN** se envía una petición de registro cuyo email no tiene formato de email
- **THEN** la respuesta es un 422 con un error asociado al campo email

#### Scenario: Email ya registrado

- **WHEN** se envía una petición de registro con un email que ya pertenece a otra cuenta
- **THEN** la respuesta es un 422 con un error de unicidad asociado al campo email

#### Scenario: Contraseña fuera de longitud

- **WHEN** se envía una petición de registro con una contraseña de menos de 8 o de más de 32 caracteres
- **THEN** la respuesta es un 422 con un error asociado al campo contraseña

#### Scenario: Confirmación distinta de la contraseña

- **WHEN** se envía una petición de registro cuya confirmación no coincide con la contraseña
- **THEN** la respuesta es un 422 con un error asociado al campo de confirmación

### Requirement: Pantalla de registro

El sistema SHALL ofrecer una pantalla de registro con los campos nombre (marcado como opcional), email, contraseña y repetir contraseña, que muestre los errores en castellano junto al campo al que se refieren y que, al completarse el registro, deje a la persona dentro con la sesión iniciada.

#### Scenario: Contraseñas que no coinciden

- **WHEN** la persona envía el formulario con la contraseña y su repetición distintas
- **THEN** ve «Las contraseñas no coinciden.» bajo el campo de repetir contraseña y el registro no se envía al servidor

#### Scenario: Email ya registrado

- **WHEN** la persona envía el formulario con un email que ya tiene cuenta
- **THEN** ve «Ese email ya está registrado. Inicia sesión en su lugar.» bajo el campo email

#### Scenario: Envío en curso

- **WHEN** la persona envía el formulario y el servidor aún no ha respondido
- **THEN** el botón muestra «Creando cuenta…» y no se puede volver a pulsar

#### Scenario: Registro completado

- **WHEN** el registro se completa correctamente
- **THEN** la persona pasa a la pantalla de perfil con la sesión iniciada, sin volver a introducir sus credenciales

#### Scenario: Ayuda sobre la contraseña

- **WHEN** la persona está rellenando el formulario y el campo contraseña no tiene ningún error
- **THEN** ve bajo él la indicación «Entre 8 y 32 caracteres.»

### Requirement: Inicio de sesión

El sistema SHALL permitir iniciar sesión con email y contraseña y, si las credenciales corresponden a una cuenta, SHALL devolver los datos de la persona y un token de acceso; si no corresponden, SHALL rechazar el intento sin revelar si el fallo está en el email o en la contraseña.

#### Scenario: Credenciales correctas

- **WHEN** se envía una petición de inicio de sesión con el email y la contraseña de una cuenta existente
- **THEN** la respuesta es un 200 y contiene, dentro de `data`, los datos de la persona y un token de acceso

#### Scenario: Contraseña incorrecta

- **WHEN** se envía una petición de inicio de sesión con el email de una cuenta existente y una contraseña que no es la suya
- **THEN** la respuesta es un 400 con un error sin campo asociado y no incluye ningún token

#### Scenario: Email no registrado

- **WHEN** se envía una petición de inicio de sesión con un email que no pertenece a ninguna cuenta
- **THEN** la respuesta es idéntica a la de una contraseña incorrecta

### Requirement: Validación de los datos de inicio de sesión

El sistema SHALL rechazar con un error 422, indicando el campo afectado, una petición de inicio de sesión cuyo email no tenga formato de email o a la que le falte la contraseña.

#### Scenario: Email con formato no válido

- **WHEN** se envía una petición de inicio de sesión cuyo email no tiene formato de email
- **THEN** la respuesta es un 422 con un error asociado al campo email

#### Scenario: Falta la contraseña

- **WHEN** se envía una petición de inicio de sesión sin contraseña
- **THEN** la respuesta es un 422 con un error asociado al campo contraseña

### Requirement: Pantalla de inicio de sesión

El sistema SHALL ofrecer una pantalla de inicio de sesión con los campos email y contraseña que muestre en castellano por qué no se ha podido entrar y que, al entrar, lleve a la persona a su perfil.

#### Scenario: Credenciales incorrectas

- **WHEN** la persona envía el formulario con un email o una contraseña que no corresponden a ninguna cuenta
- **THEN** ve el aviso «El email o la contraseña no son correctos.» encima del formulario y sigue en la pantalla de inicio de sesión

#### Scenario: Email con formato no válido

- **WHEN** la persona envía el formulario con un email sin formato de email
- **THEN** ve «Introduce una dirección de email válida.» bajo el campo email

#### Scenario: Envío en curso

- **WHEN** la persona envía el formulario y el servidor aún no ha respondido
- **THEN** el botón muestra «Entrando…» y no se puede volver a pulsar

#### Scenario: Inicio de sesión completado

- **WHEN** la persona envía el formulario con credenciales correctas
- **THEN** pasa a la pantalla de perfil con la sesión iniciada

#### Scenario: Ir al registro

- **WHEN** la persona pulsa el enlace «Crea una» de la pantalla de inicio de sesión
- **THEN** pasa a la pantalla de registro

### Requirement: Persistencia de la sesión

El sistema SHALL conservar la sesión en el navegador de forma que sobreviva a recargar la página y a cerrar la pestaña, y SHALL validarla contra el servidor cada vez que la aplicación arranca antes de mostrar contenido privado.

#### Scenario: Recarga con sesión válida

- **WHEN** la persona tiene la sesión iniciada y recarga la página de perfil
- **THEN** sigue en su perfil sin volver a introducir sus credenciales

#### Scenario: Pestaña nueva con sesión válida

- **WHEN** la persona tiene la sesión iniciada, cierra la pestaña y abre la aplicación en una pestaña nueva del mismo navegador
- **THEN** entra en su perfil sin volver a introducir sus credenciales

#### Scenario: Validación en curso

- **WHEN** la aplicación arranca con una sesión guardada y el servidor aún no ha confirmado que es válida
- **THEN** se muestra un indicador de carga y no se redirige a ninguna pantalla

### Requirement: Sesión guardada que el servidor ya no acepta

El sistema SHALL descartar una sesión guardada que el servidor rechaza y SHALL explicar en la pantalla de inicio de sesión por qué se ha perdido.

#### Scenario: Sesión rechazada

- **WHEN** la aplicación arranca con una sesión guardada que el servidor rechaza
- **THEN** la persona acaba en la pantalla de inicio de sesión con el aviso «Tu sesión ha caducado. Vuelve a iniciar sesión.» y, al recargar, sigue sin sesión

### Requirement: Servidor no disponible al arrancar

El sistema SHALL tratar como anónima a la persona cuando no puede validar su sesión guardada por un fallo del servidor o de la conexión, SHALL explicarlo en la pantalla de inicio de sesión y SHALL conservar la sesión guardada para recuperarla cuando el servidor vuelva.

#### Scenario: Sin conexión con el servidor

- **WHEN** la aplicación arranca con una sesión guardada y no consigue conectar con el servidor
- **THEN** la persona acaba en la pantalla de inicio de sesión con el aviso «No se pudo conectar con el servidor. Comprueba que el backend está arrancado.»

#### Scenario: Error del servidor

- **WHEN** la aplicación arranca con una sesión guardada y el servidor responde con un error interno
- **THEN** la persona acaba en la pantalla de inicio de sesión con el aviso «Algo ha ido mal en el servidor. Inténtalo de nuevo en un momento.»

#### Scenario: El servidor vuelve

- **WHEN** tras uno de los fallos anteriores el servidor vuelve a responder y la persona recarga la página
- **THEN** recupera su sesión y entra en su perfil sin volver a introducir sus credenciales

### Requirement: Varias sesiones simultáneas

El sistema SHALL emitir un token nuevo en cada registro o inicio de sesión sin invalidar los anteriores, de modo que una misma cuenta puede tener varias sesiones válidas a la vez.

#### Scenario: Dos inicios de sesión

- **WHEN** una persona inicia sesión dos veces con la misma cuenta y obtiene dos tokens
- **THEN** los dos tokens son aceptados por el servidor

### Requirement: Consulta del perfil

El sistema SHALL devolver, a quien presenta un token válido, los datos de su propia cuenta: identificador, nombre, email, iniciales y fechas de alta y actualización, sin incluir la contraseña.

#### Scenario: Perfil con token válido

- **WHEN** se pide el perfil con un token válido
- **THEN** la respuesta es un 200 y contiene, dentro de `data`, el identificador, el nombre, el email, las iniciales y las fechas de alta y actualización de la cuenta dueña del token, y ningún dato de la contraseña

### Requirement: Iniciales de la persona

El sistema SHALL calcular unas iniciales de la persona en mayúsculas: a partir de las dos primeras palabras del nombre si tiene más de una, de las dos primeras letras si tiene una sola palabra, y del email si no tiene nombre.

#### Scenario: Nombre de dos palabras

- **WHEN** la cuenta se llama «ana garcía»
- **THEN** sus iniciales son «AG»

#### Scenario: Nombre de una palabra

- **WHEN** la cuenta se llama «Ada»
- **THEN** sus iniciales son «AD»

#### Scenario: Sin nombre

- **WHEN** la cuenta no tiene nombre y su email es `ana@gmail.com`
- **THEN** sus iniciales son «AG», la primera letra del email y la primera del dominio

### Requirement: Cierre de sesión en la API

El sistema SHALL invalidar el token con el que se pide cerrar sesión, sin afectar a otros tokens de la misma cuenta.

#### Scenario: Cierre de sesión con token válido

- **WHEN** se pide cerrar sesión con un token válido
- **THEN** la respuesta es un 200 y, a partir de ese momento, ese token deja de ser aceptado

#### Scenario: Otras sesiones de la misma cuenta

- **WHEN** una cuenta tiene dos tokens válidos y se cierra sesión con uno de ellos
- **THEN** el otro sigue siendo aceptado

### Requirement: Pantalla de perfil

El sistema SHALL mostrar a la persona con sesión iniciada sus iniciales, su nombre (o «Sin nombre» si no tiene), su email, la fecha de alta como «Miembro desde» con la fecha larga en castellano, y un botón «Cerrar sesión».

#### Scenario: Perfil con nombre

- **WHEN** una persona con nombre entra en su perfil
- **THEN** ve sus iniciales, su nombre, su email, «Miembro desde» seguido de la fecha de alta (por ejemplo, «29 de septiembre de 2026») y el botón «Cerrar sesión»

#### Scenario: Perfil sin nombre

- **WHEN** una persona sin nombre entra en su perfil
- **THEN** ve «Sin nombre» en lugar del nombre

### Requirement: Cierre de sesión desde la pantalla

El sistema SHALL cerrar la sesión en el navegador al pulsar «Cerrar sesión», aunque el servidor no llegue a confirmarlo, SHALL llevar a la persona a la pantalla de inicio de sesión y SHALL impedir que volver atrás en el navegador muestre de nuevo el perfil.

#### Scenario: Cierre de sesión

- **WHEN** la persona pulsa «Cerrar sesión»
- **THEN** acaba en la pantalla de inicio de sesión, sin ningún aviso, y al recargar sigue sin sesión

#### Scenario: Volver atrás tras cerrar sesión

- **WHEN** la persona ha cerrado sesión y pulsa «atrás» en el navegador
- **THEN** no vuelve a ver su perfil

#### Scenario: El servidor no confirma el cierre

- **WHEN** la persona pulsa «Cerrar sesión» y el servidor no responde
- **THEN** acaba igualmente en la pantalla de inicio de sesión y sin sesión en el navegador

### Requirement: Zonas privadas de la API

El sistema SHALL rechazar con un 401 cualquier petición a la zona privada de la API (perfil y cierre de sesión) que no traiga un token válido.

#### Scenario: Sin token

- **WHEN** se pide el perfil o se pide cerrar sesión sin token
- **THEN** la respuesta es un 401 con el error «Unauthorized access»

#### Scenario: Token no válido

- **WHEN** se pide el perfil o se pide cerrar sesión con un token que no existe o que ya se cerró
- **THEN** la respuesta es un 401 con el error «Unauthorized access»

### Requirement: Pantallas privadas

El sistema SHALL llevar a la pantalla de inicio de sesión a quien intente entrar sin sesión en una pantalla privada.

#### Scenario: Perfil sin sesión

- **WHEN** una persona sin sesión abre la pantalla de perfil
- **THEN** acaba en la pantalla de inicio de sesión y no llega a ver ningún dato de perfil

### Requirement: Pantallas de acceso con sesión iniciada

El sistema SHALL llevar a su perfil a quien, con la sesión iniciada, abra la pantalla de inicio de sesión o la de registro.

#### Scenario: Inicio de sesión con sesión iniciada

- **WHEN** una persona con la sesión iniciada abre la pantalla de inicio de sesión
- **THEN** acaba en su perfil

#### Scenario: Registro con sesión iniciada

- **WHEN** una persona con la sesión iniciada abre la pantalla de registro
- **THEN** acaba en su perfil

### Requirement: Direcciones desconocidas

El sistema SHALL tratar cualquier dirección de la aplicación que no sea una pantalla conocida, incluida la raíz, como la pantalla de perfil.

#### Scenario: Dirección desconocida con sesión

- **WHEN** una persona con la sesión iniciada abre la raíz de la aplicación o una dirección que no existe
- **THEN** acaba en su perfil

#### Scenario: Dirección desconocida sin sesión

- **WHEN** una persona sin sesión abre la raíz de la aplicación o una dirección que no existe
- **THEN** acaba en la pantalla de inicio de sesión

---

## Parte B

### 1. Requisitos escritos y comprobados

- **Escritos por el agente:** 19 requisitos (47 escenarios).
- **Comprobados por mí leyendo el código:** 0. No leo TypeScript.
- **Comprobados con pruebas e2e de caja negra:** 19 requisitos (47 de 47 escenarios). Las lanzaron subagentes contra el sistema en marcha, sin leer el código, y yo revisé los resultados escenario a escenario.
- **Afirmaciones del agente que resultaron falsas al ejecutar:** 1. Leyendo el código, había dicho que la API guardaba un nombre en blanco tal cual; no es así, y la entrada se retiró de la lista 2.
- **Nota sobre RF-4:** el PRD pide que sin sesión «ninguna tarea es visible», pero todavía no existen tareas; la protección solo se ha podido comprobar sobre el perfil.

### 2. Incoherencias

- **La contraseña se valida distinto según la puerta.** En el registro debe tener entre 8 y 32 caracteres; en el inicio de sesión se acepta cualquier longitud. Se ve comparando las respuestas de la API de registro y de inicio de sesión ante una misma contraseña de 40 caracteres.
- **La pantalla de registro valida en cliente solo una de las dos reglas que anuncia.** Comprueba antes de enviar que las contraseñas coinciden, pero no su longitud, aunque indica «Entre 8 y 32 caracteres.»: una contraseña de 3 caracteres se envía y la rechaza el servidor.
- **La existencia de una cuenta se oculta en una puerta y se revela en la otra.** El inicio de sesión responde exactamente igual a un email no registrado que a una contraseña incorrecta, sin decir si la cuenta existe; el registro, con un email ya usado, responde que ese email ya está registrado, así que cualquiera puede averiguar si un email tiene cuenta.
- **El email se normaliza a medias.** Un email con espacios delante y detrás se acepta y se guarda recortado, pero las mayúsculas se conservan: `Mixto@Example.com` y `mixto@example.com` quedan como cuentas distintas. Se ve registrando las dos variantes.
- **Los mensajes de longitud de la contraseña no siguen el estilo del resto.** En la pantalla de registro, con una contraseña de 3 caracteres, aparece «la contraseña debe tener al menos 8 caracteres.» en minúscula, frente a «Las contraseñas no coinciden.»; y el mismo error de longitud aparece también bajo «Repite la contraseña» aunque las dos coincidan.

- **El aviso «Tu sesión ha caducado» describe algo que nunca pasa.** Es el único aviso cuando el servidor rechaza una sesión guardada, tanto si el token es inválido como si se cerró explícitamente desde otro sitio; pero los tokens no caducan nunca. Se ve cerrando la sesión de un token por la API y recargando la pantalla de perfil del navegador que lo usaba.
- **El cierre de sesión responde con otro formato.** Devuelve `{"message":"Logged out successfully"}`, sin el envoltorio `data` que usan el resto de respuestas correctas de la API, en inglés, y además deja una cookie de sesión aunque la autenticación sea por token.
- **La regla de las iniciales se rompe con nombres poco habituales.** «Ana García» da «AG», pero «Ana  García» (con dos espacios) da «AN»: los espacios del principio se recortan y los de en medio no. Y «😀 Ana» da un carácter roto seguido de «A», porque toma media letra del emoji. Se ve en las iniciales que devuelve el registro y en la pantalla de perfil.
- **El nombre no tiene límite de longitud.** El email tiene un máximo de 254 caracteres y la contraseña de 32, pero el nombre acepta 300 o más; y la pantalla de perfil no lo contiene: desborda la tarjeta y aparece scroll horizontal, en escritorio y en móvil.

### 3. Bug o contrato

- **El nombre es opcional al registrarse.** El PRD lo enumera entre los datos del registro («crear una cuenta con nombre, email y contraseña», RF-1), así que tratarlo como opcional sería un bug; pero el código lo trata como opcional de forma deliberada en las dos capas (la API acepta `null`, la pantalla lo etiqueta «(opcional)», el perfil muestra «Sin nombre» y las iniciales salen del email), así que parece una decisión.
- **Mayúsculas en el email.** Registrar `Mixto@Example.com` y después `mixto@example.com` crea dos cuentas distintas, cada una con su propia contraseña. O son la misma persona y permitir dos cuentas es un bug, o el email se compara tal cual por decisión y son cuentas legítimamente distintas.
- **El máximo de 32 caracteres en la contraseña.** O es un límite decidido (la pantalla lo anuncia: «Entre 8 y 32 caracteres.»), o es un límite heredado sin motivo que perjudica a quien usa contraseñas largas o un gestor de contraseñas.
- **El destino tras el registro.** O incumple RF-1 («ve el espacio», y el propio PRD lo admite en PA-11) y la pantalla de perfil es un apaño, o, como el espacio todavía no existe, el perfil es el destino decidido para el sistema de hoy.
- **El nombre «opcional» es obligatorio como dato de la petición.** La pantalla lo marca como opcional, pero la API rechaza con un 422 una petición de registro que no lo incluye; solo acepta que venga vacío. O es deliberado y el contrato es «hay que enviarlo aunque sea vacío», o es un efecto de cómo se declaró la validación y «opcional» debería significar que se puede omitir.
- **Las iniciales de quien no tiene nombre.** Se forman con la primera letra del email y la primera del dominio: `ana.garcia@gmail.com` da «AG», pero la G es de *gmail*, no de *García*, `e2e@example.com` da «EE» y `b@1790.example.com` da «B1», con un número como segunda inicial. O alguien decidió sacar las iniciales del email así, o es la lógica de partir el nombre en dos aplicada al email, y el resultado es casual.
- **El token de acceso no caduca nunca.** El inicio de sesión no devuelve ninguna caducidad, y cerrar sesión solo invalida ese token: los demás siguen valiendo, así que las sesiones se acumulan sin límite y no hay forma de cerrarlas todas. O es deliberado, como la forma más simple de cumplir RF-3 (la sesión sobrevive al cierre de la pestaña), o es una omisión y un token robado vale para siempre. No se puede confirmar ejecutando: habría que esperar indefinidamente.
- **Tras un fallo del servidor, ¿hay sesión o no?** La pantalla dice que no: la persona está en el inicio de sesión con un aviso y, navegando por la aplicación, no se vuelve a comprobar el token. Pero el token sigue guardado, y cualquier recarga, incluso de la pantalla de registro, la devuelve a su perfil. O la sesión sigue viva y solo se oculta hasta recargar (conservar el token parece deliberado, para no echar a nadie por un corte pasajero), o la persona está fuera y una recarga le resucita la sesión sin credenciales.
- **Cerrar sesión sin que el servidor lo confirme.** Si el servidor no responde al cierre de sesión, la pantalla deja a la persona fuera, pero el token sigue siendo válido en el servidor y, como no caduca, lo sigue siendo para siempre. O es deliberado, porque lo que importa es que ese navegador deje de tener sesión, o es un fallo de seguridad: la persona cree haber cerrado la sesión y su token sigue vivo.
