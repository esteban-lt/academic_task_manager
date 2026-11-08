#!/usr/bin/env bash
# Saca las capturas de wireframes y prototipo con Chrome sin ventana (390×844).
# Uso (Git Bash, desde la raíz del repo): bash design/capturas.sh
set -e
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
ROOT="$(cd "$(dirname "$0")/.." && pwd -W)"
URL="file:///$ROOT/design/prototype/index.html"

shot() {  # shot <carpeta> <nombre> <query+hash>
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=390,844 \
    --virtual-time-budget=4000 --screenshot="$ROOT/design/$1/$2.png" "$URL$3" 2>/dev/null
}

for s in login dashboard nueva detalle eliminar materias; do
  shot wireframes "$s" "?wireframe#$s"
  shot prototipo "$s" "#$s"
done
shot prototipo dashboard_tarea_guardada "?toast=Tarea%20guardada#dashboard"
shot prototipo dashboard_tarea_eliminada "?toast=Tarea%20eliminada#dashboard"
echo "listo"
