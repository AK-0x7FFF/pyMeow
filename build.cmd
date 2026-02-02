@echo off

echo [pyMeow Build]
echo.

:: Quick checks
if not exist "pyMeow.nim" (
    echo ERROR: pyMeow.nim not found!
    pause
    exit 1
)

where nim >nul || (
    echo ERROR: Nim not found in PATH
    pause
    exit 1
)

echo [1/2] Installing dependencies...
echo nimble install -y nimpy nimraylib_now x11 winim
echo.
echo This may take a few minutes...
echo.

nimble install -y nimpy nimraylib_now x11 winim

if errorlevel 1 (
    echo.
    echo WARNING: Some dependencies may have failed
    echo Continuing with build anyway...
    echo.
)

echo [2/2] Compiling pyMeow...
echo nim c pyMeow
echo.

nim c pyMeow

if errorlevel 1 (
    echo.
    echo COMPILATION FAILED!
    echo.
    echo Try running these commands separately:
    echo   nimble install -y nimpy
    echo   nimble install -y nimraylib_now
    echo   nimble install -y winim
    echo   nim c pyMeow
    pause
    exit 1
)

echo.
echo SUCCESS!
pause