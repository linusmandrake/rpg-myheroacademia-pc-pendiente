# RPG My Hero Academia Custom — Akari Hayami

Campaña TTRPG custom inspirada en My Hero Academia, con sistema propio y un único PC homebrew: **Akari Hayami, “Sanguine”**, alumno de 18 años matriculado a última hora en UA 1-A.

> **Campaña 18+ para adultos.** Todos los personajes son mayores de edad. Las directrices completas de tono, contenido y dirección están en AGENTS.md y CLAUDE.md.

## Estado

La campaña está **en marcha**. El número de sesión, día de ficción, ubicación y decisión pendiente no se duplican aquí porque cambian constantemente.

Fuentes operativas:

1. **registros/punto_cierre_actual.md** — posición narrativa exacta y decisión pendiente.
2. **registros/*.csv** — estado estructurado por dominio.
3. **registros/sesion_XX.md** y **registros/cronologia.csv** — historia canónica.
4. **registros/estado_actual.md** — vista resumida derivada del punto de cierre.

## Documentos principales

- **AGENTS.md** — reglas de dirección, tono, POV y procedimiento.
- **CLAUDE.md** — avisos activos de alta prioridad.
- **docs/personaje_akari_hayami.md** — concepto y ficha inicial del PC.
- **docs/quirk_pc.md** — diseño canónico de Sanguine Verdant Echo.
- **docs/sistema_juego.md** — atributos y resolución general.
- **docs/combate.md** — combate, consecuencias, heridas y relojes.
- **docs/progresion_narrativa.md** — marcas, rutas y curva de poder.
- **docs/sistema_relaciones.md** — vínculos y Closeness.
- **docs/registros_campania.md** — jerarquía y mantenimiento del estado.
- **docs/npc_canon.md**, **docs/npc_custom.md** y **docs/facciones.md** — mundo y reparto.
- **docs/sesion_cero.md** — decisiones iniciales y configuración histórica.

## Operación

Abrir sesión:

1. Leer registros/punto_cierre_actual.md.
2. Leer registros/memoria_gm.md.
3. Leer la cabecera de AGENTS.md y los avisos de CLAUDE.md.
4. Presentar la decisión pendiente sin avanzar varios beats.

Cerrar sesión:

1. Crear o extender registros/sesion_XX.md.
2. Actualizar los CSV afectados.
3. Regenerar registros/estado_actual.md y registros/punto_cierre_actual.md.
4. Ejecutar: python3 tools/validar_estado.py

Resolver una acción:

    python3 tools/resolver_accion.py 4 -1 --stat TEC

Las opciones completas están disponibles con --help.

## Estructura

- **docs/** — reglas, ficha inicial, ambientación y world-building.
- **registros/** — estado vivo, cronología y sesiones.
- **tools/** — validación y resolución.
- **REGISTRO_TAREAS_CAMPANA.md** — backlog técnico y de campaña.

Los documentos históricos se conservan en subcarpetas historico o archivo; nunca se usan como fuente del estado vigente.
