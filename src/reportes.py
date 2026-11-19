"""reportes de los modelos: las metricas salen por consola y los graficos van a reports/figures"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.config import CARPETA_GRAFICOS


def mostrar_metricas(nombre, y_real, y_pred):
    """imprime MAE RMSE y R2 de una predicion"""
    mae = mean_absolute_error(y_real, y_pred)
    rmse = np.sqrt(mean_squared_error(y_real, y_pred))
    r2 = r2_score(y_real, y_pred)
    print(nombre, "- MAE:", round(mae), "RMSE:", round(rmse), "R2:", round(r2, 3))


def guardar_grafico(x, y, linea_x, linea_y, etiqueta_x, etiqueta_y, titulo, archivo):
    """guarda un grafico de puntos con una linea roja de referenica"""
    CARPETA_GRAFICOS.mkdir(parents=True, exist_ok=True)
    plt.scatter(x, y, s=5)
    plt.plot(linea_x, linea_y, color="red")
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.title(titulo)
    plt.savefig(CARPETA_GRAFICOS / archivo)
    plt.close()
