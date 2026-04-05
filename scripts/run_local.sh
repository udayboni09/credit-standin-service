#run_local.sh
#!/usr/bin/env bash  # Use the system's bash interpreter

# Exit immediately if any command fails
set -e

# Print each command before executing it (useful for debugging)
set -x

# Activate virtual environment if it exists
if [ -d "venv" ]; then  # Check if venv directory exists
  source venv/bin/activate  # Activate the virtual environment
fi

# Run the FastAPI app using uvicorn
# uvicorn is an ASGI server for running FastAPI apps (install via pip)
uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000  # Start the API server
