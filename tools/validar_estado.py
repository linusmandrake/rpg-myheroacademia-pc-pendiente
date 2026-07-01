#!/usr/bin/env python3
"""
validar_estado.py — verifica consistencia de registros/.

Comprueba CSVs vacíos, columnas esperadas, capa 4 sexoafectiva, saldo de
finanzas contra el comentario de cierre, y sincronía del cierre de sesión
(sesion_XX.md ↔ punto_cierre_actual.md ↔ cronologia.csv).
"""

import csv
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTROS = ROOT / "registros"


CSV_REQUERIDOS = {
    "finanzas.csv": ["timestamp", "concepto", "id_entidad", "descripcion", "cantidad", "tipo"],
    "progreso_narrativo.csv": ["id", "rasgo", "peso", "marca", "otorgada", "sesion"],
    "hitos_progresion.csv": ["id", "sesion", "marca_id", "rasgo", "de", "a", "motivo"],
    "rutas_crecimiento.csv": ["id", "rasgo_objetivo", "tipo", "descripcion", "requisitos", "coste_narrativo", "activa"],
    "companeros.csv": ["id", "nombre", "tipo", "rol", "quirk", "vinculo", "nivel", "regimen", "relevancia", "estado"],
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


def validar_finanzas() -> list[str]:
    """Suma finanzas.csv y la cuadra contra el comentario '# Saldo al cierre'."""
    avisos: list[str] = []
    path = REGISTROS / "finanzas.csv"
    if not path.exists():
        return avisos
    saldo = 0
    saldo_declarado = None
    con_movimientos = False
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row:
                continue
            if row[0].startswith("#"):
                linea = ",".join(row)
                m = re.search(r"saldo al cierre[^:]*:?\s*~?¥?\s*([\d.,]+)", linea, re.I)
                if m:
                    saldo_declarado = int(re.sub(r"[.,]", "", m.group(1)))
                continue
            if row[0] == "timestamp":
                continue
            try:
                saldo += int(row[4])
                con_movimientos = True
            except (IndexError, ValueError):
                avisos.append(f"[WARN] finanzas: cantidad no numérica en fila {row[:3]}")
    if not con_movimientos:
        return avisos
    if saldo_declarado is not None and saldo != saldo_declarado:
        avisos.append(f"[WARN] finanzas: la suma de movimientos da ¥{saldo:,} pero el "
                      f"comentario de cierre declara ¥{saldo_declarado:,}".replace(",", "."))
    return avisos


def validar_sincronia_cierre() -> list[str]:
    """El punto de cierre y las crónicas deben ir a la par de la última sesión jugada."""
    avisos: list[str] = []
    sesiones_md = set()
    for p in REGISTROS.glob("sesion_*.md"):
        m = re.match(r"sesion_(\d+)\.md$", p.name)
        if m:
            sesiones_md.add(int(m.group(1)))

    # Sesiones que la cronología da por cerradas ("[SESIÓN N CERRADA]")
    max_cerrada = 0
    crono = REGISTROS / "cronologia.csv"
    if crono.exists():
        texto = crono.read_text(encoding="utf-8")
        for m in re.finditer(r"SESI[ÓO]N\s+(\d+)\s+CERRADA", texto, re.I):
            max_cerrada = max(max_cerrada, int(m.group(1)))

    # Sesión que refleja el punto de cierre (cabecera "sesión N")
    sesion_pc = None
    pc = REGISTROS / "punto_cierre_actual.md"
    if pc.exists():
        primera = pc.read_text(encoding="utf-8").splitlines()[0] if pc.stat().st_size else ""
        m = re.search(r"sesi[óo]n\s+(\d+)", primera, re.I)
        if m:
            sesion_pc = int(m.group(1))

    ultima = max(sesiones_md | {max_cerrada}) if (sesiones_md or max_cerrada) else 0
    if max_cerrada and max_cerrada not in sesiones_md:
        avisos.append(f"[ERROR] cronologia.csv da la sesión {max_cerrada} por cerrada "
                      f"pero falta registros/sesion_{max_cerrada:02d}.md")
    if sesion_pc is not None and ultima and sesion_pc < ultima:
        avisos.append(f"[ERROR] punto_cierre_actual.md es de la sesión {sesion_pc} pero la "
                      f"última sesión jugada es la {ultima} (regenerar con cierre-sesion-mha)")
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

    # Saldo de finanzas y sincronía del cierre de sesión
    for w in validar_finanzas() + validar_sincronia_cierre():
        print(w)
        total_warnings += 1

    print(f"\n=== {total_warnings} avisos ===")


if __name__ == "__main__":
    main()
