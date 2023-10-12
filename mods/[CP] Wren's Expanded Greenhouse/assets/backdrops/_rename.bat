@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
FOR %%f in (*.tbin) do (
	ECHO renamed %%f
	SET name=%%f
	REN %%f !name:backdrop_=!
)
pause