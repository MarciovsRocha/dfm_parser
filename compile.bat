DEL /S /Q .\Product\DFMParser*
python.exe -m PyInstaller --onefile -n DFMParser --clean --distpath Product .\main.py
