#!/usr/bin/env python3
"""Resuelve una acción con el motor 2d6 de la campaña MHA."""

from __future__ import annotations

import argparse
import json
import random
from typing import Sequence


RESULTADOS = (
    (6, "fallo"),
    (9, "exito_parcial"),
    (11, "exito"),
)


def modificador_stat(valor: int) -> int:
    """Convierte una stat de 1-10 al modificador -1..+3."""
    if not 1 <= valor <= 10:
        raise ValueError("la stat debe estar entre 1 y 10")
    if valor <= 2:
        return -1
    return (valor - 3) // 2


def clasificar(total: int) -> str:
    for maximo, resultado in RESULTADOS:
        if total <= maximo:
            return resultado
    return "exito_critico"


def resolver_accion(
    valor_stat: int,
    modificadores: int = 0,
    dados: Sequence[int] | None = None,
    rng: random.Random | None = None,
) -> dict:
    """Tira 2d6 y devuelve el resultado estructurado."""
    mod_stat = modificador_stat(valor_stat)
    if not -4 <= modificadores <= 4:
        raise ValueError("los modificadores situacionales deben estar entre -4 y +4")

    if dados is None:
        generador = rng or random.Random()
        tirada = (generador.randint(1, 6), generador.randint(1, 6))
    else:
        if len(dados) != 2 or any(not 1 <= dado <= 6 for dado in dados):
            raise ValueError("dados debe contener exactamente dos valores entre 1 y 6")
        tirada = tuple(dados)

    suma_dados = sum(tirada)
    total = suma_dados + mod_stat + modificadores
    return {
        "dados": list(tirada),
        "suma_dados": suma_dados,
        "valor_stat": valor_stat,
        "mod_stat": mod_stat,
        "modificadores": modificadores,
        "total": total,
        "resultado": clasificar(total),
    }


def crear_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resuelve 2d6 + modificador de stat + situación.",
        epilog=(
            "Ejemplo: resolver_accion.py 4 -1 --stat TEC --semilla 42. "
            "Consulta docs/combate.md para posición, efecto y consecuencias."
        ),
    )
    parser.add_argument("valor_stat", type=int, help="valor de la stat, entre 1 y 10")
    parser.add_argument(
        "modificadores",
        type=int,
        nargs="?",
        default=0,
        help="suma situacional; normalmente entre -2 y +2",
    )
    parser.add_argument(
        "--stat",
        choices=("PWR", "VEL", "TEC", "ING", "COO"),
        help="nombre de la stat usada, solo para mostrarla",
    )
    parser.add_argument(
        "--dados",
        nargs=2,
        type=int,
        metavar=("D1", "D2"),
        help="fija los dos dados para una tirada manual o reproducible",
    )
    parser.add_argument("--semilla", type=int, help="semilla aleatoria reproducible")
    parser.add_argument("--json", action="store_true", help="imprime JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = crear_parser()
    args = parser.parse_args(argv)
    try:
        rng = random.Random(args.semilla) if args.semilla is not None else None
        resultado = resolver_accion(
            args.valor_stat,
            args.modificadores,
            dados=args.dados,
            rng=rng,
        )
    except ValueError as exc:
        parser.error(str(exc))

    if args.stat:
        resultado = {"stat": args.stat, **resultado}

    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, sort_keys=True))
    else:
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
