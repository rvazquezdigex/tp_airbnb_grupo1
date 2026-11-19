"""Proyecto 4: k-NN para estimar el precio por noche a partir de alojamientos pareciddos"""
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

from src.etl import extraer_datos, transformar_datos
from src.reportes import guardar_grafico, mostrar_metricas

COLUMNAS = ["accommodates", "bedrooms", "beds", "minimum_nights"]


def correr_p4():
    """entrena knn con k=5 lo compara con el modelo base muestra los vecinos de un caso nuevo y guarda el grafico"""
    print("Proyecto 4 - k-NN")

    df = extraer_datos()
    # `bedrooms` puede ser 0 si es monoambientte
    minimos = {"accommodates": 1, "bedrooms": 0, "beds": 1, "minimum_nights": 1}
    datos = transformar_datos(df, COLUMNAS, minimos)

    X = datos[COLUMNAS]
    y = datos["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # escalamos porqe knn usa distancias y sino `minimum_nights` pesa mucho mas
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

    guardar_grafico(y_test, pred, [0, y_test.max()], [0, y_test.max()],
                    "Precio real", "Precio predicho", "Real vs predicho (k-NN)",
                    "p4_reales_vs_predichos.png")


if __name__ == "__main__":
    correr_p4()
