# REGISTRO_TAREAS_CAMPANA.md

Tareas pendientes para terminar de armar el esqueleto inicial. Marcar con `[x]` cuando se complete.

## PC y ambientación

- [x] Definir PC: nombre, curso UA, quirk (tipo/nombre/mecánica custom/limitaciones), backstory corta — **Akari Hayami "Sanguine"**
- [x] Renombrar carpeta `rpg-myheroacademia-pc-pendiente` → `rpg-myheroacademia-akari-hayami`
- [x] Renombrar `docs/personaje_pc_pendiente.md` → `docs/personaje_akari_hayami.md` y rellenar (el original se conserva como índice histórico)
- [x] Crear `registros/pj.csv` con ficha inicial del PC
- [ ] Crear `registros/companeros.csv` con compañeros de clase canon relevantes

## Sistema

- [ ] Decidir versión final del sistema de stats (5 stats? 8 stats? otro?)
- [ ] Decidir sistema de quirks custom (dados, cartas, descriptivo libre?)
- [ ] Decidir cómo se mide el "esfuerzo" de entrenamiento (días,汗, arcos?)
- [ ] Definir curva de progresión temprana (ver `docs/progresion_temprana.md`)
- [ ] Implementar `tools/resolver_accion.py` con el sistema definitivo

## Mundo

- [ ] Rellenar `docs/facciones.md` con UA, Shiketsu, Ketsubutsu, Comisión, Liga
- [ ] Rellenar `docs/campus_ua.md` con detalle de aulas, dormitorios, simuladores
- [ ] Rellenar `docs/curso_1a_1b.md` con compañeros canon
- [ ] Decidir ambientación temporal (¿año 1, año 2, post-canon?)

## Skills del agente

- [ ] Crear `.claude/skills/apertura-sesion-mha/SKILL.md`
- [ ] Crear `.claude/skills/cierre-sesion-mha/SKILL.md`
- [ ] Crear `.claude/skills/ficha-mha/SKILL.md`
- [ ] Crear `.claude/skills/que-tengo-a-punto-mha/SKILL.md`
- [ ] Crear `.claude/skills/evaluar-progresion-mha/SKILL.md`
- [ ] Crear `.claude/skills/rutas-crecimiento-mha/SKILL.md`
- [ ] Crear `.claude/skills/generar-misiones-mha/SKILL.md`

## Primera sesión

- [ ] Rellenar `docs/sesion_cero.md` con la sesión cero del PC
- [ ] Primer arco: decidir entre Examen de Ingreso UA / Provisional License Exam /实习 / Custom
- [ ] Programar `cron` o hook de `rpg_sync.sh` para esta carpeta

## Catálogos y datos

- [ ] `catalogos/quirks_canon.csv` — quirks de NPCs canon
- [ ] `catalogos/quirks_custom.csv` — quirks custom que el sistema puede generar
- [ ] `catalogos/costumes.csv` — catálogo de costumes de héroes
- [ ] `catalogos/villanos.csv` — villanos de la Liga y asociados
- [ ] `catalogos/agencias.csv` — agencias heroicas de Japón
- [ ] `data/musutafu.geojson` o similar — mapa de Musutafu

## Validación

- [ ] `tools/validar_estado.py` con checks de consistencia
- [ ] Verificar que `registros/*.csv` siguen el formato definido en `docs/registros_campania.md`
