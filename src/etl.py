"""ETL: saca los datos del csv crudo de Inside Airbnb y los deja limpios para los modelos"""
import pandas as pd

from src.config import RUTA_DATOS


def extraer_datos():
    """lee el csv crudo y lo devuelve como dataframe"""
    df = pd.read_csv(RUTA_DATOS, low_memory=False)
    print("Filas:", len(df), "Columnas:", len(df.columns))
    return df


def convertir_precio(precio):
    """pasa el precio de texto a numero y lo que no se puede convertir queda NaN"""
    # viene como texto tipo "$106,393.00" asi que hay que limpiarlo
    precio = precio.astype(str).str.replace("$", "").str.replace(",", "")
    return pd.to_numeric(precio, errors="coerce")


def transformar_datos(df, columnas, minimos):
    """deja las columnas que le pasamos y el precio sin nulos sin valores imposibles y sin precios extremos

    `minimos` tiene el valor minimo que aceptamos por columna ej {"accommodates": 1}
    """
    datos = df[columnas + ["price"]].copy()
    datos["price"] = convertir_precio(datos["price"])
    datos = datos.dropna()

    datos = datos[datos["price"] > 0]
    for columna in minimos:
        datos = datos[datos[columna] >= minimos[columna]]

    # sacamos el 1% mas barato y el 1% mas caro porqeu ensucian el modelo
    minimo = datos["price"].quantile(0.01)
    maximo = datos["price"].quantile(0.99)
    datos = datos[(datos["price"] >= minimo) & (datos["price"] <= maximo)]

    print("Filas despues de limpiar:", len(datos))
    return datos
