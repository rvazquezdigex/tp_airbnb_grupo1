"""ETL: extrae el CSV crudo de Inside Airbnb y lo transforma en datos limpios para los modelos."""
import pandas as pd

from src.config import RUTA_DATOS


def extraer_datos():
    """Lee el CSV crudo y lo devuelve como DataFrame."""
    df = pd.read_csv(RUTA_DATOS, low_memory=False)
    print("Filas:", len(df), "Columnas:", len(df.columns))
    return df


def convertir_precio(precio):
    """Pasa el precio de texto a numero; lo que no se puede convertir queda NaN."""
    # viene como texto, ej: "$106,393.00"
    precio = precio.astype(str).str.replace("$", "").str.replace(",", "")
    return pd.to_numeric(precio, errors="coerce")


def transformar_datos(df, columnas, minimos):
    """Deja las columnas pedidas y el precio, sin nulos, sin valores imposibles y sin precios extremos.

    minimos es el valor minimo aceptado por columna, ej: {"accommodates": 1}.
    """
    datos = df[columnas + ["price"]].copy()
    datos["price"] = convertir_precio(datos["price"])
    datos = datos.dropna()

    datos = datos[datos["price"] > 0]
    for columna in minimos:
        datos = datos[datos[columna] >= minimos[columna]]

    # sacamos los precios extremos
    minimo = datos["price"].quantile(0.01)
    maximo = datos["price"].quantile(0.99)
    datos = datos[(datos["price"] >= minimo) & (datos["price"] <= maximo)]

    print("Filas despues de limpiar:", len(datos))
    return datos
