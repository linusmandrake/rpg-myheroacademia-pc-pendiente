# REGISTRO_TAREAS_CAMPANA.md

> **Fase de esqueleto COMPLETADA** (2026-07-01, con 4 sesiones jugadas). Lo que queda abajo sin marcar es backlog opcional — nada de ello bloquea jugar. Marcar con `[x]` cuando se complete.

## PC y ambientación

- [x] Definir PC: nombre, curso UA, quirk (tipo/nombre/mecánica custom/limitaciones), backstory corta — **Akari Hayami "Sanguine"**
- [x] Renombrar carpeta `rpg-myheroacademia-pc-pendiente` → `rpg-myheroacademia-akari-hayami`
- [x] Renombrar `docs/personaje_pc_pendiente.md` → `docs/personaje_akari_hayami.md` y rellenar (el original se conserva como índice histórico)
- [x] Crear `registros/pj.csv` con ficha inicial del PC
- [x] Crear `registros/companeros.csv` con compañeros de clase canon relevantes

## Sistema

- [x] Decidir versión final del sistema de stats — **5 stats: PWR/VEL/TEC/ING/COO (escala 1-10)**
- [x] Decidir sistema de quirks custom — **descriptivo narrativo** (potencial/maestría + aspectos; ver `docs/quirk_pc.md`)
- [x] Decidir cómo se mide el "esfuerzo" de entrenamiento — **días de entrenamiento dedicado** (+1 maestría/día al inicio; curva ralentizada desde M4 por aviso de Aizawa)
- [x] Definir curva de progresión temprana — en uso (`docs/progresion_narrativa.md` + `docs/progresion_temprana.md`)
- [ ] Implementar `tools/resolver_accion.py` con el sistema definitivo (sigue en esqueleto 2d6; la resolución real es narrativa — decidir si se mantiene así)

## Mundo

- [x] Rellenar `docs/facciones.md` con UA, Shiketsu, Ketsubutsu, Comisión, Liga
- [ ] Rellenar `docs/campus_ua.md` con detalle de aulas, dormitorios, simuladores (relevante pronto: Heights Alliance en construcción)
- [ ] Rellenar `docs/curso_1a_1b.md` con compañeros canon (cubierto de facto por `registros/companeros.csv` + `docs/npc_canon.md`)
- [x] Decidir ambientación temporal — **año 1, post-USJ; Día 1 de Akari = lunes 13 de mayo** (ver `registros/calendario.md`)

## Skills del agente

- [x] Crear `.claude/skills/apertura-sesion-mha/SKILL.md`
- [x] Crear `.claude/skills/cierre-sesion-mha/SKILL.md`
- [x] Crear `.claude/skills/ficha-mha/SKILL.md`
- [x] Crear `.claude/skills/que-tengo-a-punto-mha/SKILL.md`
- [x] Crear `.claude/skills/evaluar-progresion-mha/SKILL.md`
- [x] Crear `.claude/skills/rutas-crecimiento-mha/SKILL.md`
- [x] Crear `.claude/skills/generar-misiones-mha/SKILL.md`
- [x] Crear `.claude/skills/validar-estado-mha/SKILL.md`

## Primera sesión

- [x] Rellenar `docs/sesion_cero.md` con la sesión cero del PC
- [x] Primer arco — **custom: matriculado a última hora post-USJ** (jugado desde S1)
- [x] Programar `cron` o hook de `rpg_sync.sh` para esta carpeta (auto-sync cada 10 min, operativo)

## Catálogos y datos (backlog opcional)

- [ ] `catalogos/quirks_canon.csv` — quirks de NPCs canon (cubierto de facto por `docs/npc_canon.md`)
- [ ] `catalogos/quirks_custom.csv` — quirks custom que el sistema puede generar
- [ ] `catalogos/costumes.csv` — catálogo de costumes de héroes (relevante cuando Akari diseñe el suyo)
- [ ] `catalogos/villanos.csv` — villanos de la Liga y asociados (cubierto de facto por `registros/enemigos.csv`)
- [ ] `catalogos/agencias.csv` — agencias heroicas de Japón
- [ ] `data/musutafu.geojson` o similar — mapa de Musutafu

## Validación

- [x] `tools/validar_estado.py` con checks de consistencia (CSVs + capa 4 sexoafectiva + saldo finanzas + sincronía de cierre de sesión)
- [x] Verificar que `registros/*.csv` siguen el formato definido en `docs/registros_campania.md` (lo hace el validador)
