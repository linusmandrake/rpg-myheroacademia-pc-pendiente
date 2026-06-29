#!/usr/bin/env python3
"""
resolver_accion.py — resuelve acciones del PC en el sistema custom MHA.

Estado: esqueleto. Falta decidir motor de dados y fórmulas definitivas.
Ver docs/sistema_juego.md para las convenciones pendientes.
"""

import sys


def resolver_accion(stat_mod: int, modificadores: int = 0) -> dict:
    """Resuelve una acción. Esqueleto: dado ficticio 2d6."""
    import random
    dado = random.randint(1, 6) + random.randint(1, 6)
    total = dado + stat_mod + modificadores

    if total <= 6:
        resultado = "fallo"
    elif total <= 9:
        resultado = "exito_parcial"
    elif total <= 11:
        resultado = "exito"
    else:
        resultado = "exito_critico"

    return {
        "dado": dado,
        "stat_mod": stat_mod,
        "modificadores": modificadores,
        "total": total,
        "resultado": resultado,
    }


def main():
    if len(sys.argv) < 2:
        print("Uso: resolver_accion.py <stat_mod> [modificadores]")
        print("Ejemplo: resolver_accion.py 2 1")
        sys.exit(1)

    stat_mod = int(sys.argv[1])
    modificadores = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    resultado = resolver_accion(stat_mod, modificadores)
    for k, v in resultado.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
