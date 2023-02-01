:: ------------------------------------------------
:: excludes previous version
set DEPLOY_FOLDER=D:\Marcio\auxiliares
set PROD_FOLDER=.\Product

:: ------------------------------------------------
:: excludes previous version
del %DEPLOY_FOLDER%\DFMParser.exe

:: ------------------------------------------------
:: compiles new version
DEL /S /Q .\Product\DFMParser*
python.exe -m PyInstaller --onefile -n DFMParser --clean --distpath Product .\main.py

:: ------------------------------------------------
:: deploy new compiled version 
xcopy %PROD_FOLDER%\DFMParser.exe %DEPLOY_FOLDER% /Y
