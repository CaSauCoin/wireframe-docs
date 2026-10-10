#!/bin/bash
# Live preview of the WireFrame docs at http://127.0.0.1:8001
# Creates .venv on first run, installs requirements.txt whenever it changes,
# then serves the site with live reload. Stop with Ctrl+C.
set -e
cd "$(dirname "$0")"

PORT="${PORT:-8001}"

if [ ! -d ".venv" ]; then
    echo ">> Creating virtual environment (.venv)..."
    python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

STAMP=".venv/.requirements.installed"
if [ ! -f "$STAMP" ] || [ requirements.txt -nt "$STAMP" ]; then
    echo ">> Installing requirements..."
    python -m pip install --upgrade pip >/dev/null
    python -m pip install -r requirements.txt
    touch "$STAMP"
fi

echo "=================================================="
echo "   WireFrame docs: http://127.0.0.1:${PORT}"
echo "   Press Ctrl+C to stop."
echo "=================================================="
exec python -m mkdocs serve --dev-addr "127.0.0.1:${PORT}"
