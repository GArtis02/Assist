@echo off

:: Define variables for easy configuration
set WEB_SERVICE_VENV_NAME=web-service-env
set TKINTER_CLIENT_VENV_NAME=tkinter-client-env
set EXPO_CLIENT_VENV_NAME=expo-client-env
set PROJECT_NAME=ai-chat-app
set GITHUB_REPO=https://github.com/ingus-t/ai-chat-app.git
set ORIGIN_REPO=git@https://github.com/GArtis02/Assist.git

:: Get the current timestamp in a format suitable for file names: YYYY-MM-DD_HH-MM-SS
for /f "tokens=1-4 delims= " %%A in ('wmic os get localdatetime ^| find "."') do set datetime=%%A
set timestamp=%datetime:~0,8%_%datetime:~8,6%

:: Set the log file name
set LOG_FILE=logs\setup_log_%timestamp%.txt

:: Redirect all output (stdout and stderr) to the log file
>> %LOG_FILE% 2>&1

:: Create a logs folder if it doesn't exist
echo Step 0: Checking logs folder
if not exist logs (
    mkdir logs
    echo Created logs folder...
) else (
    echo Logs folder already exists...
)

:: Determine Python command
set PYTHON_CMD=python
echo Using Python command: %PYTHON_CMD%

:: Step 6: Create virtual environments

:: Create web-service virtual environment
echo Step 6.1: Creating virtual environment for web-service...
cd web-service
if not exist %WEB_SERVICE_VENV_NAME% (
    %PYTHON_CMD% -m venv %WEB_SERVICE_VENV_NAME%
    echo Created virtual environment: %WEB_SERVICE_VENV_NAME%
) else (
    echo Virtual environment %WEB_SERVICE_VENV_NAME% already exists. Not overwriting...
)
cd ..

:: Create tkinter-client virtual environment
echo Step 6.2: Creating virtual environment for tkinter-client...
cd tkinter-client
if not exist %TKINTER_CLIENT_VENV_NAME% (
    %PYTHON_CMD% -m venv %TKINTER_CLIENT_VENV_NAME%
    echo Created virtual environment: %TKINTER_CLIENT_VENV_NAME%
) else (
    echo Virtual environment %TKINTER_CLIENT_VENV_NAME% already exists. Not overwriting...
)
cd ..

:: Create expo-client virtual environment
echo Step 6.3: Creating virtual environment for expo-client...
cd expo-client
if not exist %EXPO_CLIENT_VENV_NAME% (
    %PYTHON_CMD% -m venv %EXPO_CLIENT_VENV_NAME%
    echo Created virtual environment: %EXPO_CLIENT_VENV_NAME%
) else (
    echo Virtual environment %EXPO_CLIENT_VENV_NAME% already exists. Not overwriting...
)
cd ..

timeout /t 30 /nobreak
