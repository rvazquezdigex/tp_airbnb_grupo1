import os

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from funciones_airbnb import cargar_datos, limpiar, mostrar_metricas


def correr_p1():
    print("Proyecto 1 - Regresion lineal")

    df = cargar_datos()
    datos = limpiar(df, ["accommodates"], {"accommodates": 1})

    X = datos[["accommodates"]]
    y = datos["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    print("Pendiente:", round(modelo.coef_[0]))
    print("Intercepto:", round(modelo.intercept_))

    # modelo base para comparar, predice siempre el promedio
    base = DummyRegressor()
    base.fit(X_train, y_train)

    pred = modelo.predict(X_test)
    mostrar_metricas("Regresion lineal", y_test, pred)
    mostrar_metricas("Modelo base", y_test, base.predict(X_test))

    nuevo = pd.DataFrame({"accommodates": [4]})
    print("Precio estimado para 4 huespedes:", round(modelo.predict(nuevo)[0]))

    os.makedirs("graficos", exist_ok=True)
    plt.scatter(X_test["accommodates"], y_test, s=5)
    plt.plot(X_test["accommodates"], pred, color="red")
    plt.xlabel("Huespedes")
    plt.ylabel("Precio por noche")
    plt.title("Precio vs huespedes")
    plt.savefig("graficos/p1_precio_vs_huespedes.png")
    plt.close()


if __name__ == "__main__":
    correr_p1()
