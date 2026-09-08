@echo off
chcp 65001 > nul

echo [1/3] Checking Python version...
python --version >nul 2>&1
if errorlevel 1 goto no_python

if exist ".venv" goto activate_venv

echo [2/3] First run: creating virtual environment .venv...
python -m venv .venv
    
echo [2/3] Installing dependencies from requirements.txt...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul
pip install -r requirements.txt
if errorlevel 1 goto pip_error
goto check_env

:activate_venv
call .venv\Scripts\activate.bat

:check_env
if exist ".env" goto start_bot
if not exist ".env.example" goto start_bot
echo [WARNING] .env file not found. Creating a copy from .env.example...
copy .env.example .env >nul
echo Please add your tokens to the .env file and rerun this script.
pause
exit /b 0

:start_bot
echo [3/3] Starting the bot...
echo ----------------------------------------
python -m bot.bot

if errorlevel 1 goto bot_error
pause
exit /b 0

:no_python
echo [ERROR] Python not found in PATH. Please install Python and make sure it is added to PATH.
pause
exit /b 1

:pip_error
echo [ERROR] Failed to install requirements.
pause
exit /b 1

:bot_error
echo ----------------------------------------
echo [ERROR] The bot process was interrupted or terminated with an error.
pause
exit /b 1