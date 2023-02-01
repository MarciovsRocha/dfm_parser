:: ------------------------------------------------
:: excludes previous version
del D:\Marcio\auxiliares\DFMParser.exe

:: ------------------------------------------------
:: compiles new version
DEL /S /Q .\Product\DFMParser*
python.exe -m PyInstaller --onefile -n DFMParser --clean --distpath Product .\main.py

:: ------------------------------------------------
:: deploy new compiled version 
xcopy .\Product\DFMParser.exe D:\Marcio\auxiliares /Y
