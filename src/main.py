# punto de entrada correr desde la raiz con: python -m src.main
from src.p1_regresion_huespedes import correr_p1
from src.p4_knn_alojamientos_parecidos import correr_p4


def main():
    correr_p1()
    print()
    correr_p4()


if __name__ == "__main__":
    main()
