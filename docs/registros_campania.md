# Registros de campaña — RPG MHA Custom

> Convenciones de persistencia. Esta jerarquía evita que una vista resumida contradiga a la historia o a los datos estructurados.

## Jerarquía de verdad

1. **punto_cierre_actual.md**: ubicación, hora, estado narrativo y decisión pendiente.
2. **CSV por dominio**: valores actuales y entidades consultables.
3. **sesion_XX.md + cronologia.csv**: historia canónica; nunca se poda para actualizar el presente.
4. **estado_actual.md**: resumen derivado y reemplazable.
5. **agenda.md y ganchos_futuros.md**: planificación, no hechos consumados.
6. **docs/**: reglas, concepto inicial y world-building.

Si dos fuentes discrepan, la crónica determina qué ocurrió; el CSV debe reconciliar el valor actual y el punto de cierre debe reflejar la posición final.

## CSV operativos

| Archivo | Una fila por |
|---|---|
| pj.csv | PC |
| companeros.csv | compañero o aliado |
| mentores.csv | mentor |
| relaciones.csv | vínculo sexoafectivo |
| equipo_pc.csv | ítem |
| finanzas.csv | movimiento |
| reputacion.csv | evento reputacional |
| misiones.csv | misión o compromiso |
| expediente_academico.csv | asignatura |
| conocimientos.csv | conocimiento |
| enemigos.csv | amenaza |
| facciones_estado.csv | facción |
| progreso_narrativo.csv | marca |
| hitos_progresion.csv | subida concedida |
| rutas_crecimiento.csv | ruta |
| cronologia.csv | evento canónico |

Los campos escalares guardan estado actual. La prosa extensa pertenece a sesiones y cronología. El contenido histórico que ya existe dentro de celdas no se elimina: se conserva hasta una migración explícita con archivo de respaldo.

## Markdown operativo

| Archivo | Función |
|---|---|
| punto_cierre_actual.md | reapertura exacta |
| estado_actual.md | dashboard derivado |
| memoria_gm.md | preferencias persistentes de dirección |
| agenda.md | compromisos con fecha |
| ganchos_futuros.md | semillas y posibilidades |
| calendario.md | fechas y relojes |
| regalos.md | continuidad de regalos |
| sesion_XX.md | acta canónica de sesión |

## Regla de preservación

- El world-building, las crónicas y los detalles emocionales no se borran por estar antiguos.
- Lo superado sale de la vista operativa mediante archivo, no mediante eliminación.
- Un cambio de esquema CSV requiere copia histórica o migración verificable.
- La ficha narrativa puede conservar valores iniciales; los valores actuales viven en pj.csv.

## Cierre de sesión

1. Crear o extender sesion_XX.md.
2. Actualizar solo los CSV afectados.
3. Actualizar agenda, calendario y ganchos.
4. Regenerar estado_actual.md.
5. Reescribir punto_cierre_actual.md con una única decisión pendiente.
6. Ejecutar python3 tools/validar_estado.py.

## Apertura

1. Leer punto_cierre_actual.md.
2. Leer memoria_gm.md.
3. Leer la cabecera de AGENTS.md y los avisos de CLAUDE.md.
4. Consultar el CSV del dominio necesario.
5. Abrir con fecha, estado breve y decisión pendiente.
