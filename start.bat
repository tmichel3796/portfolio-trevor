@echo off
REM ==========================================================
REM  Flask Server Launcher — starts your local website
REM ==========================================================

REM Change directory to this script’s location
cd d %~dp0

REM Optional activate virtual environment if you use one
REM call venvScriptsactivate

REM Start the Flask app
echo Starting Flask server...
python app.py

REM Keep window open if something crashes
pause
