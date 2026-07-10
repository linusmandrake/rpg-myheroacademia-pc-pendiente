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


    def test_s19_sin_auditoria_genera_warning(self):
        (validar_estado.REGISTROS / "sesion_18.md").write_text(
            "# sesión histórica sin auditoría\n",
            encoding="utf-8",
        )
        (validar_estado.REGISTROS / "sesion_19.md").write_text(
            "# sesión nueva sin auditoría\n",
            encoding="utf-8",
        )

        avisos = validar_estado.validar_auditoria_direccion()

        self.assertEqual(len(avisos), 1)
        self.assertIn("sesion_19.md", avisos[0])

    def test_s19_con_auditoria_completa_no_avisa(self):
        contenido = """# Sesión 19

## Auditoría de dirección
- Beats totales: 12
- POV Akari: 8
- POV NPC: Ochaco: 2; Bakugo: 2
- Marcha de avance: 4 beats
- Marcha de profundidad: 8 beats
- Beats importantes encadenados indebidamente: 0
- Handoffs con decisión al jugador: 9
"""
        (validar_estado.REGISTROS / "sesion_19.md").write_text(
            contenido,
            encoding="utf-8",
        )

        self.assertEqual(validar_estado.validar_auditoria_direccion(), [])


if __name__ == "__main__":
    unittest.main()
