# RPG My Hero Academia Custom

Base de campaña TTRPG custom ambientada en el universo de **My Hero Academia** (Kohei Horikoshi), con tono shonen-heroico llevado a sus últimas consecuencias, sistema propio, y **PC homebrew** que llega a UA como alumno de **intercambio** o **matriculado a última hora**.

> **🔞 CAMPAÑA 18+ (ADULTOS).** Todos los personajes (PC, NPCs canon, NPCs custom) tienen **18 años o más**. La campaña incluye **violencia explícita** y **sexualidad explícita** sin eufemismos. No apta para menores ni para quien prefiera un tono shonen limpio. Ver `AGENTS.md` y `CLAUDE.md` para el detalle.

## Estado actual

**Esqueleto inicial.** PC definido: **Akari Hayami "Sanguine"** (carpeta `rpg-myheroacademia-akari-hayami`). Los `docs/` tienen estructura y placeholders; los `registros/` se están poblando; no hay sesión jugada todavía.

## Archivos principales

- `AGENTS.md`: directrices para agentes y GM, tono de campaña, procedimiento de sesión y principios de narración.
- `CLAUDE.md`: avisos puntuales de alta prioridad (estado actual del proyecto).
- `docs/sesion_cero.md`: primera sesión — definición del PC, tono, límites, decisiones iniciales.
- `docs/trasfondo_pc.md`: opciones de homebrew / intercambio / llegada tardía, con ejemplos.
- `docs/personaje_akari_hayami.md`: ficha completa del PC (`personaje_pc_pendiente.md` se conserva como índice histórico).
- `docs/sistema_juego.md`: sistema determinista de atributos, quirks, combate, entrenamiento y progresión.
- `docs/sistema_relaciones.md`: reglas de romance/sexo (mujeres = opción, hombres = amistad/rivalidad/mentor) con dificultad 1–10 y track de Closeness.
- `docs/registros_campania.md`: guía de registros persistentes de campaña (CSVs, índices, estados).
- `docs/facciones.md`: UA, Shiketsu, Ketsubutsu, Comisión de Seguridad Pública, Liga de Villanos, etc.
- `docs/npc_canon.md`: NPCs del canon (All Might, Aizawa, Bakugo, etc.) con Dificultad de relación (mujeres) o Vínculo (hombres).
- `docs/poderes_quirks.md`: sistema de quirks (clasificación emitter/transformation/mutant, costes, evolución).
- `docs/entrenamiento.md`: reglas de entrenamiento, sudor y subida de stats.
- `docs/equipo_inicial_pj.md`: equipo inicial (costume, gadgets, apoyo).
- `docs/combate.md`: reglas de combate 1-a-1, equipos, contra villanos.
- `docs/examenes_licencia.md`: Provisional License Exam y reglas asociadas.
- `docs/economia_y_recursos.md**: ingresos pro-hero, becas UA, costos de costume, vivienda.
- `docs/prensa_reputacion.md**: cobertura mediática, fans, haters, ranking.
- `docs/campus_ua.md**: aulas, dormitorios, sala común, enfermería, simuladores.
- `docs/curso_1a_1b.md**: compañeros de clase canon y sus quirks.
- `docs/complicaciones_encuentros.md**: tablas de complicaciones para clases, entrenamientos, prácticas, villanos.
- `docs/progresion_narrativa.md**: subidas de stats y habilidades, ritmo de poder.
- `docs/progresion_temprana.md**: mejoras recomendadas de los primeros arcos.
- `docs/mapa_regional_jugable.md**: Musutafu, Kamino, Deika, etc. — zonas, riesgos, accesibilidad.
- `docs/reglas_viaje.md**: transporte público, shinkansen, barcos (si la campaña sale de Tokyo).
- `docs/reloj_principal.md**: reloj de la amenaza villana de fondo.
- `docs/glosario.md**: términos MHA canon + términos del sistema custom.
- `docs/resumen_rapido.md`: TL;DR de la campaña para abrir sesión rápido.

## Estructura

```
.
├── AGENTS.md              directrices para agentes y GM
├── CLAUDE.md              avisos puntuales
├── README.md              este archivo
├── REGISTRO_TAREAS_CAMPANA.md   tareas/mejoras pendientes del esqueleto
├── .gitignore             exclusiones
├── .claude/               configuración del agente
├── arcos/                 arcos narrativos (vacío, se llena con la campaña)
├── catalogos/             catálogos de equipo/quirks enemigos (vacío por ahora)
├── data/                  datos de mundo (vacío por ahora)
├── docs/                  documentación canónica de campaña
├── registros/             CSVs y estados persistentes de campaña
└── tools/                 scripts de validación y resolución
```

## Convención de naming

- Descriptor actual: `akari-hayami` (carpeta `rpg-myheroacademia-akari-hayami`).
- Convención: `rpg-myheroacademia-<nombre-pc-kebab-case>`.
- Reglas de kebab-case: minúsculas, sin acentos, guiones entre palabras.

## Cómo empezar

1. **Definir el PC.** Sesión cero: nombre, edad 18+, sexo/género, orientación, **tipo de llegada** (intercambio / matriculado / custom), curso destino (UA Hero Course 1-A / 1-B / Support / General Studies), quirk custom, familia custom, backstory corta. Ver `docs/trasfondo_pc.md` y `docs/sesion_cero.md`.
2. **Decidir tono específico.** El esqueleto es shonen-heroico adulto (18+, sexo y violencia explícitos). Ajustar las líneas y velos con el jugador.
3. **Elegir arco inicial.** Examen de ingreso UA, Provisional License Exam, internado en agencia, primer encuentro villano, o custom. **Si el PC llega tarde, decidir qué arcos canon ya pasaron** (USJ asalto, Stain arc, Kamino,etc.).
4. **Renombrar carpeta y poblar `registros/pj.csv` y `registros/relaciones.csv`.**
5. **Primera sesión.**
