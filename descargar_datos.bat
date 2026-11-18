@echo off
if not exist data mkdir data
curl -L -f -o data\listings.csv.gz "https://data.insideairbnb.com/argentina/ciudad-aut%%C3%%B3noma-de-buenos-aires/buenos-aires/2026-09-23/data/listings.csv.gz"
