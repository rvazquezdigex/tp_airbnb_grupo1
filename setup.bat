@echo off
rem crea el entorno virtual e instala las dependencias
cd /d "%~dp0"
if not exist .venv py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
if not exist data\raw\listings.csv.gz call scripts\descargar_datos.bat
