@ECHO OFF


ECHO Welcome to simple classifier menu
ECHO Choose your option
ECHO 1. Starts the server
ECHO 2. Backups model
ECHO 3. Exits the program



:MENU
SET /P choice="Choice>>"



IF %choice% EQU 1 (
GOTO ONE
)
IF %choice% EQU 2 (
GOTO TWO
)
IF %choice% EQU 3 (
GOTO THREE
)

:ONE
START server.exe
GOTO MENU


:TWO
XCOPY server.exe ..\backup
XCOPY network.json ..\backup
XCOPY ..\src ..\backup
GOTO MENU


:THREE

