#run_local.bat
@echo off  REM Disable command echo for cleaner output

REM Enable error exit on failure (not perfect but basic)
SETLOCAL ENABLEDELAYEDEXPANSION

REM Check if virtual environment folder exists
IF EXIST venv (
    REM Activate the virtual environment
    CALL venv\Scripts\activate
)

REM Run the FastAPI app using uvicorn
REM uvicorn is an ASGI server for running FastAPI apps (install via pip)
uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000
