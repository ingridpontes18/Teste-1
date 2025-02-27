@echo off
pipenv --version >nul 2>&1

if %errorlevel% neq 0 (
    pip install --user pipenv
)

pipenv run python schedule_message.py

exit