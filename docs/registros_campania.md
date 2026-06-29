# Registros de campaña — RPG MHA Custom

> Convenciones de los registros persistentes. Todo lo que cambia sesión a sesión va aquí.

## Principio rector

**Un CSV por concepto, una fila por entidad.** Los CSVs son la fuente de verdad operativa. Los `.md` narrativos complementan, pero los datos numéricos viven en CSV.

## CSVs en `registros/`

| Archivo | Contenido | Una fila por… |
|---|---|---|
| `pj.csv` | Ficha del PC (stats, quirk, equipo, finanzas) | PC |
| `companeros.csv` | Compañeros de clase / aliados cercanos | NPC aliado |
| `mentores.csv` | Profesores, maestros, senseis | mentor |
| `equipo_pc.csv` | Equipo del PC (costume, gadgets, apoyo) | ítem |
| `finanzas.csv` | Ingresos, gastos, deudas, becas | movimiento |
| `reputacion.csv` | Cobertura mediática, ranking,粉丝/haters | evento |
| `entrenamientos.csv` | Sesiones de entrenamiento,汗 | sesión |
| `misiones.csv` | Misiones de实习, patrullaje, rescate | misión |
| `examenes.csv` | Exámenes UA, license exam, simulacros | examen |
| `incidentes.csv` | Incidentes villanos,袭击,报警 | incidente |
| `enemigos.csv` | Villanos conocidos, amenazas | villano |
| `conocimientos.csv` | Cosas que el PC sabe o ha aprendido | conocimiento |
| `progreso_narrativo.csv` | Marcas narrativas (peso 1/2/3) | marca |
| `hitos_progresion.csv` | Subidas concedidas | subida |
| `rutas_crecimiento.csv` | Caminos de subida activos | ruta |
| `cronologia.csv` | Timeline canónico de la campaña | día/fecha |
| `facciones_estado.csv` | Estado de cada facción | facción |
| `relaciones.csv` | Relaciones del PC: eje afecto (closeness 0–10) + eje deseo (0–10 o —) + flag `anclado` | NPC |

## Archivos `.md` en `registros/`

| Archivo | Contenido |
|---|---|
| `agenda.md` | Tareas/mejoras de campaña |
| `estado_actual.md` | Resumen del estado al cierre de la última sesión |
| `punto_cierre_actual.md` | Estado narrativo exacto + decisión pendiente del jugador (clave para abrir sesión) |
| `deudas_favores.md` | Quién le debe qué a quién |
| `eventos_calendario.md` | Fechas importantes (examen final, festival, etc.) |
| `calendario_referencia.md` | Calendario académico UA |

## Sesiones de agente

- Carpeta: `registros/_opencode_sessions/`
- Una subcarpeta por sesión con nombre aleatorio.
- **NO se commitea** (ver `.gitignore`).

## Regla de oro

**Si cambia, va a CSV.** Si es narrativo extenso, va a `.md` enlazando al CSV.

## Sistema de relaciones

Ver `docs/sistema_relaciones.md` para el detalle completo. Resumen:

- Cada NPC tiene una **dificultad de relación** (1–10) basada en personalidad canon y obstáculos externos.
- El PC lleva un track de **Closeness** (0–10, eje **afecto**) por NPC en `registros/relaciones.csv`, un eje **deseo** aparte (0–10 o `—` si no aplica) y un flag `anclado` (si/no).
- **Dos ejes:** *afecto* (universal) y *deseo* (íntimo, **no se abre por defecto**: `—` para figuras maternas, abuelas, amistades, duelo, mentoras; 18+ habilita pero no obliga).
- Las acciones que coinciden con la personalidad del NPC suben Closeness; las que no, la bajan o congelan.
- **Dos regímenes:** un vínculo **volátil** (no anclado) se enfría con el tiempo si se desatiende; un vínculo **anclado** (cruzó un hito de afecto sincero) ya **no** decae por el paso del tiempo, solo por eventos con peso (traición, abandono, daño).
- Los hitos emocionales (primer beso, primera confesión, primer sexo, ruptura, etc.) tienen **peso narrativo** (0/1/2/3) y se registran en `progreso_narrativo.csv`.

## Procedimiento de cierre de sesión

1. Auditar el estado (ver `tools/validar_estado.py`).
2. Actualizar CSVs.
3. Reescribir `punto_cierre_actual.md`.
4. Crear/extender `sesion_XX.md` en `registros/_opencode_sessions/`.

## Procedimiento de apertura de sesión

1. Leer `punto_cierre_actual.md`.
2. Leer cabecera de `AGENTS.md` y avisos en `CLAUDE.md`.
3. Saludar al jugador con cabecera 📅 + resumen breve + decisión pendiente.
