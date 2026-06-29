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
    "relaciones.csv": ["id", "npc", "tipo", "closeness", "deseo", "confianza", "compromiso", "regimen", "marco", "dificultad", "ultimo_cambio", "hitos", "notas"],
}

# Capa 4: vocabulario controlado del dashboard sexoafectivo
VOC_REL = {
    "deseo": {"—", "latente", "abierto", "voraz", "asentado"},
    "confianza": {"baja", "media", "alta", "total"},
    "compromiso": {"ninguno", "casual", "pareja", "juramento"},
    "regimen": {"volátil", "anclado"},
}
DESEO_ABIERTO = {"abierto", "voraz", "asentado"}
TIPOS_SIN_DESEO = {"maternal", "familiar-afecto", "duelo-cuidado"}


def validar_relaciones() -> list[str]:
    """Capa 4: checks semánticos del dashboard sexoafectivo (relaciones.csv)."""
    avisos: list[str] = []
    path = REGISTROS / "relaciones.csv"
    if not path.exists():
        return avisos
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not all(c.startswith("#") for c in r)]
    if len(rows) < 2:
        return avisos
    h = rows[0]
    ci = {c: (h.index(c) if c in h else None) for c in (
        "npc", "tipo", "closeness", "deseo", "confianza",
        "compromiso", "regimen", "marco", "hitos")}
    nombres = {r[ci["npc"]].strip() for r in rows[1:]
               if ci["npc"] is not None and len(r) > ci["npc"] and r[ci["npc"]].strip()}
    for r in rows[1:]:
        if ci["npc"] is None or len(r) <= ci["npc"] or not r[ci["npc"]].strip():
            continue
        npc = r[ci["npc"]].strip()

        def v(c, _r=r):
            i = ci[c]
            return _r[i].strip() if i is not None and len(_r) > i else ""

        for campo, vocab in VOC_REL.items():
            x = v(campo)
            if x and x not in vocab:
                avisos.append(f"[WARN] relaciones {npc}: {campo}='{x}' fuera del vocabulario")
        cl = v("closeness")
        if cl and (not cl.isdigit() or not 0 <= int(cl) <= 10):
            avisos.append(f"[WARN] relaciones {npc}: closeness='{cl}' fuera de 0-10")
        if v("tipo") in TIPOS_SIN_DESEO and v("deseo") in DESEO_ABIERTO:
            avisos.append(f"[WARN] relaciones {npc}: deseo='{v('deseo')}' en tipo "
                          f"'{v('tipo')}' (¿sexualizando figura de cuidado/duelo?)")
        if v("regimen") == "anclado" and not v("hitos"):
            avisos.append(f"[WARN] relaciones {npc}: regimen=anclado sin hitos (capa 3)")
        m = v("marco")
        if m.startswith("frontera-con-"):
            obj = m[len("frontera-con-"):].strip()
            if not any(obj.lower() in nm.lower() for nm in nombres):
                avisos.append(f"[WARN] relaciones {npc}: frontera '{m}' apunta a npc inexistente")
    return avisos


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

    # Capa 4: dashboard sexoafectivo
    for w in validar_relaciones():
        print(w)
        total_warnings += 1

    print(f"\n=== {total_warnings} avisos ===")


if __name__ == "__main__":
    main()
