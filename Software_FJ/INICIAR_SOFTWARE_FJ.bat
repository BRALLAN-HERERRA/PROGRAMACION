@echo off
setlocal
cd /d "%~dp0"
title Software FJ - Inicio de aplicacion

echo ======================================================
echo              SOFTWARE FJ - APLICACION
 echo ======================================================
echo.

REM Primero intenta utilizar el lanzador oficial de Python para Windows.
where py >nul 2>nul
if %errorlevel%==0 (
    echo [INFO] Python Launcher detectado. Verificando Tkinter...
    py -c "import tkinter; print('Tkinter disponible - version', tkinter.TkVersion)"
    if errorlevel 1 goto SIN_TKINTER
    echo.
    echo [INFO] Iniciando la interfaz grafica...
    py aplicacion.py
    goto FIN
)

REM Si no existe el lanzador py, intenta con el comando python.
where python >nul 2>nul
if %errorlevel%==0 (
    echo [INFO] Comando python detectado. Verificando Tkinter...
    python -c "import tkinter; print('Tkinter disponible - version', tkinter.TkVersion)"
    if errorlevel 1 goto SIN_TKINTER
    echo.
    echo [INFO] Iniciando la interfaz grafica...
    python aplicacion.py
    goto FIN
)

echo [ERROR] No se encontro Python en el PATH.
echo Instala Python desde python.org y activa la opcion Add Python to PATH.
goto FIN

:SIN_TKINTER
echo.
echo [ERROR] Esta instalacion de Python no tiene Tkinter disponible.
echo En Windows, modifica la instalacion de Python y agrega Tcl/Tk and IDLE.
echo Luego vuelve a ejecutar este archivo.

:FIN
echo.
echo ======================================================
echo Si aparecio un error, toma una foto o copia el mensaje.
echo ======================================================
pause
endlocal
