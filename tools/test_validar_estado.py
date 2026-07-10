#!/usr/bin/env python3
"""Pruebas de regresión para la integridad estructural de registros CSV."""

import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validar_estado


class ValidarEstadoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.registros_original = validar_estado.REGISTROS
        self.csv_original = validar_estado.CSV_REQUERIDOS
        validar_estado.REGISTROS = Path(self.tmp.name)
        validar_estado.CSV_REQUERIDOS = {"muestra.csv": ["id", "valor"]}

    def tearDown(self):
        validar_estado.REGISTROS = self.registros_original
        validar_estado.CSV_REQUERIDOS = self.csv_original
        self.tmp.cleanup()

    def escribir(self, rows):
        with open(
            validar_estado.REGISTROS / "muestra.csv",
            "w",
            newline="",
            encoding="utf-8",
        ) as archivo:
            csv.writer(archivo).writerows(rows)

    def test_ancho_invalido_es_error(self):
        self.escribir([["id", "valor"], ["x-001", "ok", "campo extra"]])

        avisos = validar_estado.validar_anchos()

        self.assertEqual(len(avisos), 1)
        self.assertTrue(avisos[0].startswith("[ERROR]"))
        self.assertIn("3 campos", avisos[0])

    def test_id_duplicado_es_error(self):
        self.escribir([["id", "valor"], ["x-001", "uno"], ["x-001", "dos"]])

        avisos = validar_estado.validar_identificadores()

        self.assertEqual(len(avisos), 1)
        self.assertTrue(avisos[0].startswith("[ERROR]"))
        self.assertIn("ID duplicado 'x-001'", avisos[0])

    def test_main_devuelve_uno_si_hay_error(self):
        validar_estado.CSV_REQUERIDOS = {}
        funciones_vacias = (
            "validar_relaciones",
            "validar_finanzas",
            "validar_sincronia_cierre",
            "validar_pj",
            "validar_marca_cierre",
            "validar_identificadores",
        )
        parches = [patch.object(validar_estado, nombre, return_value=[]) for nombre in funciones_vacias]
        for parche in parches:
            parche.start()
        self.addCleanup(lambda: [parche.stop() for parche in reversed(parches)])

        with patch.object(validar_estado, "validar_anchos", return_value=["[ERROR] roto"]):
            self.assertEqual(validar_estado.main(), 1)


if __name__ == "__main__":
    unittest.main()
