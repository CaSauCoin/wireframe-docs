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

if [ -d "docs" ] && [ -f "docs/mkdocs.yml" ]; then
    cd docs
    # Run in background (&) so we can proceed to start Backend
    python3 -m mkdocs serve --dev-addr 127.0.0.1:8001 &
    cd ..
    echo "   -> Docs running at: http://127.0.0.1:8001"
elif [ -d "Guide_line" ] && [ -f "Guide_line/mkdocs.yml" ]; then
    # Fallback for old structure
    cd Guide_line
    python3 -m mkdocs serve --dev-addr 127.0.0.1:8001 &
    cd ..
    echo "   -> Docs running at: http://127.0.0.1:8001"
else
    echo "   !! WARNING: docs/mkdocs.yml not found. Skipping Docs."
fi

# 3. START BACKEND (FOREGROUND PROCESS)
echo "--------------------------------------------------"
echo ">> [2/2] Starting Backend Server..."

if [ -d "backend" ]; then
    cd backend

    # --- ENVIRONMENT CONFIGURATION (LOCAL) ---
    # These flags tell the Python code we are running locally
    export APP_ENV="local"
    export BASE_URL="http://127.0.0.1:8000"

    # Optional: Enable Test Mode (Disable DB/Redis) if needed
    # export DOCS_TEST_MODE=true

    echo "   -> Environment: $APP_ENV"
    echo "   -> Base URL:    $BASE_URL"
    echo "   -> Web App:     http://127.0.0.1:8000"
    echo "   -> API Docs:    http://127.0.0.1:8000/docs"
    echo "--------------------------------------------------"

    # Run Uvicorn
    python3 -m uvicorn index:app --reload --port 8000
else
    echo "ERROR: 'backend' folder not found!"
    exit 1
fi

# Script stays here until you press Ctrl+C
wait
