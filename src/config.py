"""Rutas del proyecto, relativas a la carpeta raiz para que funcionen desde cualquier directorio."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA_DATOS = RAIZ / "data" / "raw" / "listings.csv.gz"
CARPETA_GRAFICOS = RAIZ / "reports" / "figures"
