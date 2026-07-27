@echo off
title Class 12 AI - Python Library Installer
color 0A

echo ==================================================
echo        Class 12 Artificial Intelligence
echo        Python Library Installer
echo ==================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo.
    echo Please install Python from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit
)

echo [OK] Python detected.
python --version

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing required libraries...
python -m pip install -r requirements.txt

echo.
echo ==================================================
echo Installation Completed Successfully!
echo ==================================================

pause
