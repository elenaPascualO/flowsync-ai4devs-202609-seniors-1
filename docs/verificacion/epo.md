# Verificación: «Lo que cada tarea muestra de su responsable»

Requisito de `openspec/specs/tasks/spec.md`.

**Scenarios del requisito:** 3
**Cubiertos:** 0

## Matriz de trazabilidad

| Scenario | Test que lo cubre | Estado | Si «no lo sé», qué faltó |
|---|---|---|---|
| Responsable identificable: con responsable «Ada Lovelace», `assignee` trae ese nombre y sus iniciales. | — (ninguno) | No cubierto | — |
| La tarea no filtra datos de cuenta: en cualquier tarea, suelta o en la lista, `assignee` no trae email ni datos de acceso. | — (ninguno) | No cubierto | — |
| Responsable sin nombre: si la cuenta se registró sin nombre, `assignee` trae nombre nulo y sigue trayendo iniciales. | — (ninguno) | No cubierto | — |

## Las tres líneas

1. Creía cubiertos: 3 · Lo estaban: 0
2. Scenario «La tarea no filtra datos de cuenta»: el requisito prohíbe exponer «ningún otro dato de esa cuenta», pero el scenario solo concreta email y datos de acceso, y no sé si el `id` que viaja en `assignee` es un incumplimiento que nadie comprueba o un dato que la spec nunca decidió.
3. En «La tarea no filtra datos de cuenta» la spec no dice qué cuenta como «dato de acceso», y decidí yo que son el email, la contraseña y el token de sesión; cualquier otro dato que abra la cuenta y se añada después pasaría el test sin que nadie lo note.
