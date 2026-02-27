@echo off
setlocal

set "ENV_DIR=%USERPROFILE%\.uv-envs\toy-flet-gh-pages"
set "PY=%ENV_DIR%\Scripts\python.exe"

@REM if not exist "%PY%" (
@REM   uv venv "%ENV_DIR%"
@REM )

set "UV_PROJECT_ENVIRONMENT=%ENV_DIR%"

uv %*