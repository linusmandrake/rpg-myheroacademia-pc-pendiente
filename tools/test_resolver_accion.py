#!/usr/bin/env python3
"""Pruebas del motor de resolución 2d6."""

import contextlib
import io
import json
import unittest

import resolver_accion


class ResolverAccionTests(unittest.TestCase):
    def test_modificadores_de_stat(self):
        esperados = {
            1: -1,
            2: -1,
            3: 0,
            4: 0,
            5: 1,
            6: 1,
            7: 2,
            8: 2,
            9: 3,
            10: 3,
        }
        self.assertEqual(
            {valor: resolver_accion.modificador_stat(valor) for valor in esperados},
            esperados,
        )

    def test_bandas_de_resultado(self):
        casos = [
            ((3, 3), "fallo"),
            ((3, 4), "exito_parcial"),
            ((5, 5), "exito"),
            ((6, 6), "exito_critico"),
        ]
        for dados, esperado in casos:
            with self.subTest(dados=dados):
                resultado = resolver_accion.resolver_accion(4, dados=dados)
                self.assertEqual(resultado["resultado"], esperado)

    def test_stat_fuera_de_rango(self):
        with self.assertRaisesRegex(ValueError, "entre 1 y 10"):
            resolver_accion.resolver_accion(11, dados=(3, 3))

    def test_cli_json_reproducible(self):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            codigo = resolver_accion.main(
                ["4", "-1", "--stat", "TEC", "--dados", "4", "5", "--json"]
            )
        resultado = json.loads(salida.getvalue())
        self.assertEqual(codigo, 0)
        self.assertEqual(resultado["stat"], "TEC")
        self.assertEqual(resultado["total"], 8)
        self.assertEqual(resultado["resultado"], "exito_parcial")


if __name__ == "__main__":
    unittest.main()
