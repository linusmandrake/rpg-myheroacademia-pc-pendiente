#!/usr/bin/env python3
"""
validar_estado.py — verifica consistencia de registros/.

Estado: esqueleto. Comprueba CSVs vacíos, columnas esperadas, y cruces básicos.
"""

import csv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTROS = ROOT / "registros"


CSV_REQUERIDOS = {
    "finanzas.csv": ["timestamp", "concepto", "id_entidad", "descripcion", "cantidad", "tipo"],
    "progreso_narrativo.csv": ["id", "rasgo", "peso", "marca", "otorgada", "sesion"],
    "hitos_progresion.csv": ["id", "sesion", "marca_id", "rasgo", "de", "a", "motivo"],
    "rutas_crecimiento.csv": ["id", "rasgo_objetivo", "tipo", "descripcion", "requisitos", "coste_narrativo", "activa"],
    "companeros.csv": ["id", "nombre", "tipo", "rol", "quirk", "relevancia", "estado"],
    "mentores.csv": ["id", "nombre", "rol", "quirk", "relevancia", "estado"],
    "equipo_pc.csv": ["id", "nombre", "tipo", "quirk", "potencial", "maestria_inicial", "descripcion", "limitaciones"],
    "misiones.csv": ["id", "tipo", "descripcion", "lugar", "fecha_ficcion", "resultado", "recompensa"],
    "conocimientos.csv": ["id", "concepto", "estado", "notas"],
    "cronologia.csv": ["id", "fecha", "evento", "participantes", "consecuencias"],
    "facciones_estado.csv": ["id", "faccion", "simpatia", "influencia", "ultimo_cambio", "notas"],
    "reputacion.csv": ["id", "evento", "medio", "tono", "impacto_pc", "impacto_agencia", "notas"],
    "enemigos.csv": ["id", "nombre", "quirk", "afiliacion", "amenaza", "ultimo_avistamiento", "notas"],
}


def validar_csv(nombre: str, columnas_esperadas: list[str]) -> list[str]:
    """Devuelve lista de warnings/errores para un CSV."""
    warnings = []
    path = REGISTROS / nombre

    if not path.exists():
        return [f"[ERROR] falta {nombre}"]

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if r and not all(c.startswith("#") for c in r)]
        if not rows:
            warnings.append(f"[INFO] {nombre} está vacío (esperable si PC no definido)")
            return warnings

        header = rows[0]
        if header != columnas_esperadas:
            warnings.append(f"[WARN] {nombre} header inesperado: {header}")

    return warnings


def main():
    print(f"=== Validación de estado — {ROOT.name} ===\n")
    total_warnings = 0
    for nombre, columnas in CSV_REQUERIDOS.items():
        warnings = validar_csv(nombre, columnas)
        for w in warnings:
            print(w)
            total_warnings += 1

    print(f"\n=== {total_warnings} avisos ===")


if __name__ == "__main__":
    main()
