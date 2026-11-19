@echo off
rem Descarga el dataset de Inside Airbnb (Buenos Aires, 2026-09-23) en data\raw
set DESTINO=%~dp0..\data\raw
if not exist "%DESTINO%" mkdir "%DESTINO%"
curl -L -f -o "%DESTINO%\listings.csv.gz" "https://data.insideairbnb.com/argentina/ciudad-aut%%C3%%B3noma-de-buenos-aires/buenos-aires/2026-09-23/data/listings.csv.gz"
