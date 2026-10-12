# Auditoría de las reglas de proceso

## Mi apuesta

Escrita fuera de este archivo antes de hacer la tabla; la copio aquí sin cambios.

| Regla | Apuesta |
|---|---|
| R1 | Sí |
| R2 | No (pensaba que el agente commiteaba tras cada petición, fuera de código o no) |
| R3 | Sí |
| R4 | Sí |
| R5 | Sí |

## Auditoría

| Regla | Qué pide la regla | Qué se revisó para comprobarla | Veredicto | Evidencia | Qué harías con ella |
|---|---|---|---|---|---|
| **R1** | Crea rama nueva por unidad de trabajo antes de tocar código si estás en `main` o `sN/*`. Si no estás en esas ramas, continúa en la que estás y nunca commitees en `main` ni `sN/*`. | `git log --format='%h %p %an %cn' b955a72^..a3bb962`, `git log --merges` en el mismo rango, `git branch -r --contains <sha>` | No se puede comprobar con lo que hay | Historial lineal sin merges y con committer «LIDR Academy» distinto del autor: se reescribió al publicarlo, así que no queda en qué rama se hizo cada commit. | **Bajarla**: impedir commits y push a `main` y `sN/*` con protección de ramas en GitHub (y en local, un hook barato que mire el nombre de la rama). |
| **R2** | Haz un commit después de terminar cada petición con `/commit`. | `git log --format='%h %ad %s %b'` de los 15 commits (formato, trailers y minutos entre commits) | No se puede comprobar con lo que hay | Los commits del 20-08 son convencionales, de un solo tema y separados 2-4 min, pero nada registra qué fue una petición ni si se usó `/commit` o un `git commit` a mano. | **Bajarla**: un commit por petición es demasiado ruido; un hook que haga commit tras cambios de más de X líneas de código. |
| **R3** | Si la unidad de trabajo es sobre rutas, controladores, validadores o transformers de una capability, actualiza OpenAPI y README de esa capability y añade esos cambios al commit también. | `git show --stat` de cada commit; `git show <sha>:CLAUDE.md` para ver desde cuándo existe la regla (`160fbc7`) | Se cumple | `cbe9617`, el único que toca controladores tras `160fbc7`, lleva los decoradores OpenAPI y `docs/capabilities/tasks/README.md`. `4e03d1f` toca un transformer sin README, pero es anterior a la regla. | **Bajarla**: mantener la regla escrita y reforzarla con un hook y en CI. |
| **R4** | Crear PR con `gh pr create` que contenga una descripción de todos los cambios en su cuerpo, y lanza el agente `adversarial-reviewer` al final. Haz esto al final de cada unidad de trabajo. | `gh api repos/LIDR-academy/flowsync-ai4devs-202609-seniors-1/commits/<sha>/pulls` para cada commit; `gh pr list --state all` | No se cumple | Ninguno de los 15 commits pertenece a un PR del repo, y no hay merges: llegaron a `s4/end`/`s5/start` sin PR ni rastro del `adversarial-reviewer`. | **Borrarla**: el agente no sabe cuándo termina una unidad de trabajo; sustituirla por una skill que ejecute sus pasos. |
| **R5** | Al abrir PR responde solo con la URL del mismo, el resto va en la propia PR. | Nada en el repo: la regla habla de la respuesta en el chat | No se puede comprobar con lo que hay | Las sesiones no se guardan en el repo; haría falta el transcript de la sesión que abrió cada PR. | **Borrarla**: pasa a ser un paso dentro de la skill de R4. |

## Las tres líneas

1. **R2.** Aposté a que no se cumplía, pero porque no entendí la regla: creía que el agente commiteaba tras cada petición, fuera de código o no, y la regla deja abierto qué cuenta como petición. En el resto me apoyé en que eran comprobables con guardarraíles baratos, pero en el repo no hay ninguno: lo daba por hecho.
2. **R2.** Nada registra si un commit se hizo con `/commit` ni a qué petición corresponde; para que dejara rastro, la skill tendría que añadir un trailer al mensaje del commit.
3. **R4**, del grupo de las que no se cumplen nunca y a nadie le ha importado: ninguno de los 15 commits pasó por PR ni por el `adversarial-reviewer`. Además depende de saber cuándo termina una unidad de trabajo, y eso solo lo sabe quien la pide; mejor una skill que se lance a mano.
