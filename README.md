TP Airbnb  Grupo 1

Ejercicios con el dataset de Airbnb


P1:  regresion lineal simple, precio segun capacidad.
P4:  k-NN para regresion, precio segun alojamientos parecidos

## Estructura

    data/raw/            dataset original (no se sube a git, se descarga con el script)
    docs/diagrama.html   diagrama del programa: flujo de datos, ETL, modulos y reportes
    reports/figures/     graficos que genera el programa
    scripts/             descarga de datos
    src/                 codigo
        config.py        rutas del proyecto
        etl.py           extraccion y limpieza de datos
        reportes.py      metricas y graficos
        p1_regresion_huespedes.py
        p4_knn_alojamientos_parecidos.py
        main.py          corre P1 y P4
    tests/               tests del ETL

## Instrucciones de ejecución

1. Crear el entorno virtual e instalar dependencias (desde la carpeta del proyecto):
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

2. Descargar los datos (quedan en data\raw\listings.csv.gz):
   scripts\descargar_datos.bat

3. Correr los tests:
   python -m unittest discover tests

4. Correr los dos proyectos (con el entorno activado):
   python -m src.main
   Guarda los gráficos en reports\figures.



P1 — Regresion lineal | 48.485 | 79.839 | 0,261 |
P4 — k-NN escalado, k=5 | 55.155 | 84.308 | 0,119 |
