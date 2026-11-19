"""Punto de entrada del TP. Uso, desde la carpeta raiz: python -m src.main"""
from src.p1_regresion_huespedes import correr_p1
from src.p4_knn_alojamientos_parecidos import correr_p4


def main():
    """Corre el proyecto 1 y despues el proyecto 4."""
    correr_p1()
    print()
    correr_p4()


if __name__ == "__main__":
    main()
