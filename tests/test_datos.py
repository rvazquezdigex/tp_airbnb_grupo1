"""Tests basicos del ETL. Correr desde la carpeta raiz: python -m unittest discover tests"""
import unittest

import pandas as pd

from src.config import RUTA_DATOS
from src.etl import convertir_precio, extraer_datos, transformar_datos


class TestDatos(unittest.TestCase):

    def test_existe_el_archivo(self):
        self.assertTrue(RUTA_DATOS.exists())

    def test_carga_el_csv(self):
        df = extraer_datos()
        self.assertGreater(len(df), 0)
        for columna in ["price", "accommodates", "bedrooms", "beds", "minimum_nights"]:
            self.assertIn(columna, df.columns)

    def test_convertir_precio(self):
        precios = convertir_precio(pd.Series(["$106,393.00", "$1,000.00", None]))
        self.assertEqual(precios[0], 106393.0)
        self.assertEqual(precios[1], 1000.0)
        self.assertTrue(pd.isna(precios[2]))

    def test_transformar_datos(self):
        df = pd.DataFrame({
            "accommodates": [2, 0, 3, None, 4, 2],
            "price": ["$100.00", "$200.00", "$0.00", "$300.00", "$400.00", "$150.00"],
        })
        datos = transformar_datos(df, ["accommodates"], {"accommodates": 1})
        self.assertFalse(datos.isna().any().any())
        self.assertTrue((datos["price"] > 0).all())
        self.assertTrue((datos["accommodates"] >= 1).all())


if __name__ == "__main__":
    unittest.main()
