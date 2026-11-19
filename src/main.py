"""Punto de entrada del TP. Se corre desde la carpeta raiz con: python -m src.main"""
from src.p1_regresion_huespedes import correr_p1
from src.p4_knn_alojamientos_parecidos import correr_p4


def main():
    """corre el proyecto 1 y despues el 4"""
    correr_p1()
    print()
    correr_p4()


if __name__ == "__main__":
    main()
