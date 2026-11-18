import os

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

from funciones_airbnb import cargar_datos, limpiar, mostrar_metricas

COLUMNAS = ["accommodates", "bedrooms", "beds", "minimum_nights"]


def correr_p4():
    print("Proyecto 4 - k-NN")

    df = cargar_datos()
    # bedrooms puede ser 0 (monoambiente)
    minimos = {"accommodates": 1, "bedrooms": 0, "beds": 1, "minimum_nights": 1}
    datos = limpiar(df, COLUMNAS, minimos)

    X = datos[COLUMNAS]
    y = datos["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # escalamos porque knn usa distancias
    escalador = StandardScaler()
    X_train_esc = escalador.fit_transform(X_train)
    X_test_esc = escalador.transform(X_test)

    knn = KNeighborsRegressor(n_neighbors=5)
    knn.fit(X_train_esc, y_train)

    base = DummyRegressor()
    base.fit(X_train, y_train)

    pred = knn.predict(X_test_esc)
    mostrar_metricas("k-NN k=5", y_test, pred)
    mostrar_metricas("Modelo base", y_test, base.predict(X_test))

    nuevo = pd.DataFrame([[4, 2, 3, 2]], columns=COLUMNAS)
    nuevo_esc = escalador.transform(nuevo)
    print("Precio estimado para 4 huespedes, 2 dormitorios, 3 camas, 2 noches:",
          round(knn.predict(nuevo_esc)[0]))

    distancias, indices = knn.kneighbors(nuevo_esc)
    vecinos = X_train.iloc[indices[0]].copy()
    vecinos["price"] = y_train.iloc[indices[0]]
    print("Vecinos:")
    print(vecinos)

    os.makedirs("graficos", exist_ok=True)
    plt.scatter(y_test, pred, s=5)
    plt.plot([0, y_test.max()], [0, y_test.max()], color="red")
    plt.xlabel("Precio real")
    plt.ylabel("Precio predicho")
    plt.title("Real vs predicho (k-NN)")
    plt.savefig("graficos/p4_reales_vs_predichos.png")
    plt.close()


if __name__ == "__main__":
    correr_p4()
