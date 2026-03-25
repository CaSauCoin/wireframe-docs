#!/bin/bash
set -e

# --- FUNCTION: CLEANUP ON EXIT ---
# This ensures that when you press Ctrl+C, both Backend and Docs (running in background) are killed.
trap "kill 0" EXIT

echo "=================================================="
echo "   WIREFRAME MONOREPO - DEV ENVIRONMENT"
echo "=================================================="

# 1. SETUP VIRTUAL ENVIRONMENT
# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo ">> [Init] Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate
echo ">> [Init] Virtual Environment (venv) activated."

# Optional: Auto-install dependencies if needed (Uncomment to use)
# pip install -r backend/requirements.txt
# pip install -r docs/requirements.txt

# 2. START DOCUMENTATION (BACKGROUND PROCESS)
echo "--------------------------------------------------"
echo ">> [1/2] Starting Docs Server..."

if [ -f "mkdocs.yml" ]; then
    # mkdocs.yml is in the current directory (Guide_line/)
    python3 -m mkdocs serve --dev-addr 127.0.0.1:8001 &
    echo "   -> Docs running at: http://127.0.0.1:8001"
elif [ -d "docs" ] && [ -f "docs/mkdocs.yml" ]; then
    cd docs
    python3 -m mkdocs serve --dev-addr 127.0.0.1:8001 &
    cd ..
    echo "   -> Docs running at: http://127.0.0.1:8001"
else
    echo "   !! WARNING: mkdocs.yml not found. Skipping Docs."
fi

# 3. BACKEND (OPTIONAL - only if backend/ exists)
echo "--------------------------------------------------"

if [ -d "backend" ]; then
    echo ">> [2/2] Starting Backend Server..."
    cd backend

    # --- ENVIRONMENT CONFIGURATION (LOCAL) ---
    export APP_ENV="local"
    export BASE_URL="http://127.0.0.1:8000"

    echo "   -> Environment: $APP_ENV"
    echo "   -> Base URL:    $BASE_URL"
    echo "   -> Web App:     http://127.0.0.1:8000"
    echo "   -> API Docs:    http://127.0.0.1:8000/docs"
    echo "--------------------------------------------------"

    python3 -m uvicorn index:app --reload --port 8000
else
    echo ">> [2/2] No backend/ folder found. Running docs only."
    echo "=================================================="
    echo "   Docs server: http://127.0.0.1:8001"
    echo "   Press Ctrl+C to stop."
    echo "=================================================="
fi

# Script stays here until you press Ctrl+C
wait
