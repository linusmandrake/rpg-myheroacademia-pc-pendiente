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
    "expediente_academico.csv": ["id", "asignatura", "profesor", "estado_flanco", "ultima_medicion", "puntos_debiles", "refuerzos_activos", "proximo_hito", "notas"],
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
                m = re.search(r"saldo al cierre[^:¥]*:?\s*~?¥\s*([\d.,]+)", linea, re.I)
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


def validar_anchos() -> list[str]:
    """Detecta filas cuyo número de campos difiere del header."""
    avisos: list[str] = []
    for nombre in CSV_REQUERIDOS:
        path = REGISTROS / nombre
        if not path.exists():
            continue
        try:
            with open(path, newline="", encoding="utf-8") as f:
                rows = [
                    (linea, row)
                    for linea, row in enumerate(csv.reader(f, strict=True), start=1)
                    if row and not row[0].startswith("#")
                ]
        except csv.Error as exc:
            avisos.append(f"[ERROR] {nombre}: sintaxis CSV inválida ({exc})")
            continue
        if len(rows) < 2:
            continue
        ancho = len(rows[0][1])
        malas = [
            f"línea {linea} ({row[0] or 'sin id'}: {len(row)} campos)"
            for linea, row in rows[1:]
            if len(row) != ancho
        ]
        if malas:
            detalle = "; ".join(malas[:8])
            sufijo = "; …" if len(malas) > 8 else ""
            avisos.append(
                f"[ERROR] {nombre}: {len(malas)} fila(s) con ancho distinto "
                f"del header de {ancho} campos: {detalle}{sufijo}"
            )
    return avisos


def validar_identificadores() -> list[str]:
    """Los CSV cuyo primer campo es id deben tener IDs presentes y únicos."""
    avisos: list[str] = []
    for nombre, columnas in CSV_REQUERIDOS.items():
        if not columnas or columnas[0] != "id":
            continue
        path = REGISTROS / nombre
        if not path.exists():
            continue
        try:
            with open(path, newline="", encoding="utf-8") as f:
                rows = [
                    (linea, row)
                    for linea, row in enumerate(csv.reader(f, strict=True), start=1)
                    if row and not row[0].startswith("#")
                ]
        except csv.Error:
            continue
        vistos: dict[str, int] = {}
        for linea, row in rows[1:]:
            if len(row) != len(columnas):
                continue
            identificador = row[0].strip()
            if not identificador:
                avisos.append(f"[ERROR] {nombre}: ID vacío en línea {linea}")
            elif identificador in vistos:
                avisos.append(
                    f"[ERROR] {nombre}: ID duplicado '{identificador}' en líneas "
                    f"{vistos[identificador]} y {linea}"
                )
            else:
                vistos[identificador] = linea
    return avisos


def validar_pj() -> list[str]:
    """pj.csv debe seguir siendo header + UNA fila de datos parseables."""
    avisos: list[str] = []
    path = REGISTROS / "pj.csv"
    if not path.exists():
        return ["[ERROR] falta pj.csv"]
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r]
    if len(rows) != 2:
        avisos.append(f"[ERROR] pj.csv tiene {len(rows)} filas (esperadas 2: header+datos) "
                      f"— posible comilla rota en el campo notas")
    return avisos


def validar_marca_cierre() -> list[str]:
    """La ÚLTIMA fila de datos de cronologia.csv debe llevar la marca de cierre
    de la MISMA sesión que declara punto_cierre_actual.md."""
    avisos: list[str] = []
    crono = REGISTROS / "cronologia.csv"
    pc = REGISTROS / "punto_cierre_actual.md"
    if not (crono.exists() and pc.exists()):
        return avisos
    primera = pc.read_text(encoding="utf-8").splitlines()[0]
    m = re.search(r"sesi[óo]n\s+(\d+)", primera, re.I)
    if not m:
        return avisos
    sesion_pc = int(m.group(1))
    with open(crono, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")]
    if len(rows) < 2:
        return avisos
    ultima = ",".join(rows[-1])
    m2 = re.search(r"SESI[ÓO]N\s+(\d+)\s+CERRADA", ultima, re.I)
    if not m2:
        avisos.append(f"[WARN] cronologia.csv: la última fila ({rows[-1][0]}) no lleva la "
                      f"marca [SESIÓN {sesion_pc} CERRADA] que el punto de cierre implica")
    elif int(m2.group(1)) != sesion_pc:
        avisos.append(f"[WARN] cronologia.csv cierra la sesión {m2.group(1)} pero "
                      f"punto_cierre_actual.md declara la sesión {sesion_pc}")
    return avisos



def validar_auditoria_direccion() -> list[str]:
    """Exige métricas mínimas de POV y ritmo en sesiones S19+."""
    avisos: list[str] = []
    campos = (
        "Beats totales:",
        "POV Akari:",
        "POV NPC:",
        "Marcha de avance:",
        "Marcha de profundidad:",
        "Beats importantes encadenados indebidamente:",
        "Handoffs con decisión al jugador:",
    )
    for path in sorted(REGISTROS.glob("sesion_*.md")):
        match = re.fullmatch(r"sesion_(\d+)\.md", path.name)
        if not match or int(match.group(1)) < 19:
            continue
        contenido = path.read_text(encoding="utf-8")
        if "## Auditoría de dirección" not in contenido:
            avisos.append(
                f"[WARN] {path.name}: falta la auditoría de dirección obligatoria desde S19"
            )
            continue
        for campo in campos:
            if campo not in contenido:
                avisos.append(f"[WARN] {path.name}: auditoría sin campo '{campo}'")

        pov = re.search(r"^- POV NPC:\s*(.+)$", contenido, re.MULTILINE)
        if pov and pov.group(1).strip().lower() in {"0", "ninguno", "ninguna", "—", "..."}:
            avisos.append(
                f"[WARN] {path.name}: sesión completa sin POV NPC registrado"
            )

        cadena = re.search(
            r"^- Beats importantes encadenados indebidamente:\s*(\d+)",
            contenido,
            re.MULTILINE,
        )
        if cadena and int(cadena.group(1)) > 0:
            avisos.append(
                f"[WARN] {path.name}: {cadena.group(1)} beat(s) importante(s) "
                "encadenado(s); revisar ritmo"
            )
    return avisos

# ---------------------------------------------------------------------------
# CORRECTOR DE SALUD ANTI-CENSURA
# ---------------------------------------------------------------------------
# La campaña rige por UNCENSORED START + CORRECCIÓN REACTIVA (AGENTS.md).
# Sólo el JUGADOR pone restricciones, y sólo a posteriori. El riesgo real es
# que el GM se auto-imponga cautelas y las escriba en los registros como si
# fueran acuerdos de mesa: una vez escritas, se leen en cada apertura y se
# aplican para siempre. Eso ya pasó (nota de mesa S26, retirada en S28).
# Este check vigila que no vuelva a colarse.

# Frases que sólo tienen sentido como AUTO-CENSURA del GM.
PATRONES_CENSURA = [
    (r"no (?:se |)escribir[áa]? (?:contenido |)(?:sexual|er[óo]tic\w+|expl[íi]cit\w+)", "veto de escritura sexual"),
    (r"(?:cerrand\w+|cierran?|cierre|se juegan?|resolver|resuelve|queda\w*|dejar\w*)"
     r"[^.]{0,60}fuera de c[áa]mara", "cierre de escena fuera de cámara"),
    (r"(?:se |)(?:elide|elidir|omitir|omite|corta|cortar)\w* (?:el |la |)(?:acto|escena|parte) (?:sexual|[íi]ntim\w+)", "elisión del acto"),
    (r"sin (?:contenido |)(?:sexual |)expl[íi]cit\w+", "prohibición de explícito"),
    (r"(?<!sin )(?<!nunca )(?<!, )(?:con |usar |usando )eufemismos?\b", "eufemismos como norma"),
    (r"(?:sugerid\w+|insinuad\w+|velad\w+) en (?:lugar|vez) de", "sugerir en vez de narrar"),
    (r"(?:el |)GM (?:no |)(?:evitar[áa]|se abstiene|se abstendr[áa]|no narrar[áa])", "abstención del GM"),
    (r"por (?:prudencia|cautela|responsabilidad) narrativa", "cautela auto-impuesta"),
    (r"(?:fade|corte) a negro", "fade a negro"),
]

# Restricciones legítimas del jugador: se respetan y NO se marcan.
EXENCIONES = (
    "retirada",
    "retirado",
    "derogad",
    "anulad",
    "ya no aplica",
    "por el jugador",
    "el jugador pidi",
    "el jugador veta",
    "el jugador marc",
    "línea del jugador",
    "veto del jugador",
    "corrector de salud",
    "anti-censura",
    "patrones_censura",
)


def validar_anticensura() -> list[str]:
    """Detecta reglas que AÑADEN censura sin venir del jugador.

    Marca [ERROR]: una cautela auto-impuesta que sobreviva en registros se
    aplicará en cada apertura de sesión. Debe romper el validador, no
    limitarse a avisar.
    """
    avisos: list[str] = []
    objetivos: list[Path] = [
        *sorted(REGISTROS.glob("*.md")),
        *sorted((ROOT / "docs").glob("*.md")),
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
    ]
    for path in objetivos:
        if not path.is_file() or path.name == "sesion_plantilla.md":
            continue
        try:
            lineas = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for num, linea in enumerate(lineas, 1):
            bajo = linea.lower()
            if any(ex in bajo for ex in EXENCIONES):
                continue
            if bajo.lstrip().startswith(("~~", "- ~~", "> ~~")):
                continue  # ya tachada
            for patron, etiqueta in PATRONES_CENSURA:
                if re.search(patron, bajo):
                    rel = path.relative_to(ROOT)
                    avisos.append(
                        f"[ERROR] {rel}:{num}: posible AUTO-CENSURA del GM "
                        f"({etiqueta}). La campaña es uncensored con corrección "
                        f"reactiva: sólo el jugador restringe, y sólo a posteriori. "
                        f"Si esta regla NO la puso el jugador, bórrala. Si la puso él, "
                        f"escríbelo explícitamente ('retirada'/'por el jugador')."
                    )
                    break
    return avisos


def validar_namespace_cronologia() -> list[str]:
    """Los beats de mundo/POV sin avance de reloj usan el prefijo pov-.

    Dos ventanas escriben en cronologia.csv a la vez. La linea principal usa
    ev-N correlativo; los beats sin avance de reloj usan pov-NNN, un espacio
    de nombres disjunto para que no puedan colisionar NUNCA (un bloque
    numerico reservado solo aplaza el choque hasta que la serie lo alcanza).
    Excepciones historicas: IDs anteriores a la convencion ya referenciados.
    """
    HISTORICOS = {"ev-382", "ev-389"}
    avisos: list[str] = []
    path = REGISTROS / "cronologia.csv"
    if not path.exists():
        return avisos
    try:
        with open(path, newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f, strict=True))
    except (csv.Error, OSError):
        return avisos
    for linea, row in enumerate(rows[1:], start=2):
        if not row or row[0].startswith("#") or len(row) < 2:
            continue
        ident, fecha = row[0].strip(), row[1]
        if ident in HISTORICOS:
            continue
        sin_reloj = "sin avance de reloj" in fecha or "BEATS DE MUNDO" in fecha
        if sin_reloj and not ident.startswith("pov-"):
            avisos.append(
                f"[ERROR] cronologia.csv:{linea}: '{ident}' es un beat sin avance "
                "de reloj y debe usar el prefijo 'pov-' (espacio de nombres "
                "reservado anti-colision entre ventanas)."
            )
        elif not sin_reloj and ident.startswith("pov-"):
            avisos.append(
                f"[ERROR] cronologia.csv:{linea}: '{ident}' usa el prefijo 'pov-' "
                "pero avanza el reloj; la linea principal usa 'ev-N'."
            )
    return avisos


def validar_csv(nombre: str, columnas_esperadas: list[str]) -> list[str]:
    """Devuelve lista de warnings/errores para un CSV."""
    warnings = []
    path = REGISTROS / nombre

    if not path.exists():
        return [f"[ERROR] falta {nombre}"]

    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, strict=True)
            rows = [r for r in reader if r and not all(c.startswith("#") for c in r)]
    except csv.Error as exc:
        return [f"[ERROR] {nombre}: sintaxis CSV inválida ({exc})"]

    if not rows:
        warnings.append(f"[WARN] {nombre} está vacío")
        return warnings

    header = rows[0]
    if header != columnas_esperadas:
        warnings.append(f"[ERROR] {nombre} header inesperado: {header}")

    return warnings


def main() -> int:
    print(f"=== Validación de estado — {ROOT.name} ===\n")
    avisos: list[str] = []

    for nombre, columnas in CSV_REQUERIDOS.items():
        avisos.extend(validar_csv(nombre, columnas))

    # Semántica, sincronía e integridad estructural.
    avisos.extend(validar_relaciones())
    avisos.extend(validar_finanzas())
    avisos.extend(validar_sincronia_cierre())
    avisos.extend(validar_pj())
    avisos.extend(validar_marca_cierre())
    avisos.extend(validar_anchos())
    avisos.extend(validar_identificadores())
    avisos.extend(validar_auditoria_direccion())
    avisos.extend(validar_anticensura())
    avisos.extend(validar_namespace_cronologia())

    for aviso in avisos:
        print(aviso)

    errores = sum(aviso.startswith("[ERROR]") for aviso in avisos)
    warnings = sum(aviso.startswith("[WARN]") for aviso in avisos)
    infos = sum(aviso.startswith("[INFO]") for aviso in avisos)
    print(
        f"\n=== {errores} error(es), {warnings} warning(s), "
        f"{infos} info(s) ==="
    )
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
