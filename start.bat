@echo off
title kissblossom bot
cd /d "%~dp0"

:loop
python main.py
echo.
echo  Bot stopped. Restarting in 5 seconds...
echo  (Close this window to stop)
echo.
timeout /t 5 /nobreak
goto loop
