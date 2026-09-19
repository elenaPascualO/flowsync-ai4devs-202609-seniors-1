#!/bin/bash
# Línea de estado de Claude Code para FlowSync.
# Claude Code llama a este script en cada turno y le pasa por la entrada
# estándar un JSON con los datos de la sesión. Lo que imprimamos aquí es lo
# que se ve siempre bajo el cuadro de escritura.
#
# Guarda además el último mensaje recibido en /tmp/claude-statusline-last.json
# para poder mirar qué campos trae de verdad esta versión.
input=$(cat)
printf '%s' "$input" > /tmp/claude-statusline-last.json

printf '%s' "$input" | python3 -c '
import json, sys, time

d = json.load(sys.stdin)
partes = []

# Modelo y, entre paréntesis, el nivel de esfuerzo en vivo (cambia con /effort).
# El campo solo llega si el modelo admite el parámetro de esfuerzo.
modelo = (d.get("model") or {}).get("display_name")
if modelo:
    esfuerzo = (d.get("effort") or {}).get("level")
    partes.append("%s (%s)" % (modelo, esfuerzo) if esfuerzo else modelo)

# Contexto libre.
ctx = d.get("context_window") or d.get("context") or {}
libre = ctx.get("remaining_percentage")
if libre is None and isinstance(ctx.get("used_percentage"), (int, float)):
    libre = 100 - ctx["used_percentage"]
if isinstance(libre, (int, float)):
    partes.append("ctx %d%% libre" % round(libre))

# Consumo de las dos ventanas de la suscripción, con la hora a la que se
# reinicia la de 5 horas.
lim = d.get("rate_limits") or {}
cinco = lim.get("five_hour") or {}
usado5 = cinco.get("used_percentage")
if isinstance(usado5, (int, float)):
    texto = "5h %d%%" % round(usado5)
    reset = cinco.get("resets_at")
    if isinstance(reset, (int, float)):
        texto += " (hasta %s)" % time.strftime("%H:%M", time.localtime(reset))
    partes.append(texto)

usado7 = (lim.get("seven_day") or {}).get("used_percentage")
if isinstance(usado7, (int, float)):
    partes.append("7d %d%%" % round(usado7))

coste = (d.get("cost") or {}).get("total_cost_usd")
if isinstance(coste, (int, float)):
    partes.append("~%.2f$" % coste)

lineas = d.get("cost") or {}
mas = lineas.get("total_lines_added")
menos = lineas.get("total_lines_removed")
if isinstance(mas, int) and isinstance(menos, int) and (mas or menos):
    partes.append("+%d/-%d" % (mas, menos))

print(" · ".join(partes) if partes else "sin datos de sesión")
'
