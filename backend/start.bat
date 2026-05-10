@echo off
echo === Mohan Kumar Portfolio Backend ===
echo.

REM Detect Python
set PY=
where py >nul 2>&1 && set PY=py
if "%PY%"=="" where python >nul 2>&1 && set PY=python
if "%PY%"=="" where python3 >nul 2>&1 && set PY=python3

if "%PY%"=="" (
  echo ERROR: Python not found.
  echo Please install Python 3.10+ from https://www.python.org/downloads/
  echo Make sure to check "Add Python to PATH" during install.
  pause
  exit /b 1
)

echo Using: %PY%
%PY% --version
echo.

REM Install dependencies if fastapi is missing
%PY% -c "import fastapi" >nul 2>&1
if %errorlevel% neq 0 (
  echo Installing dependencies...
  %PY% -m pip install -r requirements.txt
  echo.
)

REM Seed database
echo Seeding database...
%PY% seed.py
echo.

REM Start server
echo Starting API server at http://localhost:8000
echo API docs: http://localhost:8000/docs
echo Press Ctrl+C to stop.
echo.
%PY% -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
