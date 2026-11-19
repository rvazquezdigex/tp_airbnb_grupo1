# etl extrae los datos del csv y los limpia
import pandas as pd

from src.config import RUTA_DATOS


# lee csv raw y devuelve como df
def extraer_datos():
    df = pd.read_csv(RUTA_DATOS, low_memory=False)
    print("Filas:", len(df), "Columnas:", len(df.columns))
    return df


# convierte a numerico y usa nan si hay error
def convertir_precio(precio):
    # viene como "$106,393.00"
    precio = precio.astype(str).str.replace("$", "").str.replace(",", "")
    return pd.to_numeric(precio, errors="coerce")


# conserva solo columnas pasadas y limpia nulos y outliers de precios
def transformar_datos(df, columnas, minimos):
    datos = df[columnas + ["price"]].copy()
    datos["price"] = convertir_precio(datos["price"])
    datos = datos.dropna()

    datos = datos[datos["price"] > 0]
    for columna in minimos:
        datos = datos[datos[columna] >= minimos[columna]]

    # saca el 1% de cada punta
    minimo = datos["price"].quantile(0.01)
    maximo = datos["price"].quantile(0.99)
    datos = datos[(datos["price"] >= minimo) & (datos["price"] <= maximo)]

    print("Filas despues de limpiar:", len(datos))
    return datos
