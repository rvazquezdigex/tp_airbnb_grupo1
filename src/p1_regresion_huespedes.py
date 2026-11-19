# proyecto 1: regresion lineal del precio segun huespedes
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from src.etl import extraer_datos, transformar_datos
from src.reportes import guardar_grafico, mostrar_metricas


# entrena compara con base estima caso nuevo y grafica
def correr_p1():
    print("Proyecto 1 - Regresion lineal")

    df = extraer_datos()
    datos = transformar_datos(df, ["accommodates"], {"accommodates": 1})

    X = datos[["accommodates"]]
    y = datos["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    print("Pendiente:", round(modelo.coef_[0]))
    print("Intercepto:", round(modelo.intercept_))

    # base predice siempre el promedio
    base = DummyRegressor()
    base.fit(X_train, y_train)

    pred = modelo.predict(X_test)
    mostrar_metricas("Regresion lineal", y_test, pred)
    mostrar_metricas("Modelo base", y_test, base.predict(X_test))

    nuevo = pd.DataFrame({"accommodates": [4]})
    print("Precio estimado para 4 huespedes:", round(modelo.predict(nuevo)[0]))

    guardar_grafico(X_test["accommodates"], y_test, X_test["accommodates"], pred,
                    "Huespedes", "Precio por noche", "Precio vs huespedes",
                    "p1_precio_vs_huespedes.png")


if __name__ == "__main__":
    correr_p1()
