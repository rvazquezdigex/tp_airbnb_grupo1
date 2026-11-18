import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

RUTA_DATOS = "data/listings.csv.gz"


def cargar_datos():
    df = pd.read_csv(RUTA_DATOS, low_memory=False)
    print("Filas:", len(df), "Columnas:", len(df.columns))
    return df


def convertir_precio(precio):
    # viene como texto, ej: "$106,393.00"
    precio = precio.astype(str).str.replace("$", "").str.replace(",", "")
    return pd.to_numeric(precio, errors="coerce")


def limpiar(df, columnas, minimos):
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


def mostrar_metricas(nombre, y_real, y_pred):
    mae = mean_absolute_error(y_real, y_pred)
    rmse = np.sqrt(mean_squared_error(y_real, y_pred))
    r2 = r2_score(y_real, y_pred)
    print(nombre, "- MAE:", round(mae), "RMSE:", round(rmse), "R2:", round(r2, 3))
