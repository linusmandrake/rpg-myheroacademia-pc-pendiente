# Sistema de juego — RPG MHA Custom

> **Estado:** motor 2d6 definitivo; combate detallado en `docs/combate.md`. La progresión se rige por marcas narrativas.

## Atributos del PC

5 stats, escala 1–10:

| Stat | Abreviatura | Significado |
|---|---|---|
| **Poder** | `PWR` | Fuerza bruta, capacidad de causar daño. |
| **Velocidad** | `VEL` | Tiempo de reacción, desplazamiento, esquiva. |
| **Técnica** | `TEC` | Habilidad marcial, control fino, combate cuerpo a cuerpo. |
| **Ingenio** | `ING` | Análisis, improvisación, resolución de problemas. |
| **Cooperación** | `COO` | Trabajo en equipo, empatía táctica, comunicación bajo presión. |

Escala:

- 1–2: civil, sin quirk
- 3–4: estudiante UA novel
- 5–6: estudiante UA competente / pro-hero junior
- 7–8: top 10 hero / All Might en su día / Endeavor
- 9–10: Nivel All Might pico / No.1

## Quirk del PC — Sanguine Verdant Echo

> **Diseño completo en `docs/quirk_pc.md`.** El PC tiene un savia vegetal en la sangre. Tres aspectos manifestables: **Cuerpo** (ancla principal), **Avatar Carmesí** (proyección humanoide de sangre), **Bestias del Savia** (criaturas de plantasangre), **Ecos Temporales** (versiones pasadas del PC).

**Ejes del Quirk:**

- **Potencial:** 1–5 estrellas (potencial bruto del quirk) — **5 para Sanguine Verdant Echo** (top-tier).
- **Maestría:** 1–10 (lo que el PC ha entrenado de su quirk) — **1–2 al inicio** (aprendiendo a invocar).
- **Voluntad del savia:** el savia tiene semi-autonomía y puede cooperar o resistirse según su relación con el PC.

**Aplicación mecánica del Quirk:**
- La stat base describe el método usado; la maestría determina capacidades, simultaneidad y coste.
- Los aspectos no conceden bonos automáticos acumulables. Cambian la ficción, el efecto o la posición cuando aportan una ventaja concreta.
- Los costes y límites canónicos están en `docs/quirk_pc.md`; las reglas R3-R8 prevalecen.

## Acciones y resolución

Motor definitivo: **2d6 + modificador de stat + situación**.

| Stat | Modificador |
|---|---:|
| 1-2 | -1 |
| 3-4 | +0 |
| 5-6 | +1 |
| 7-8 | +2 |
| 9-10 | +3 |

Resultados: 6 o menos = fallo; 7-9 = éxito parcial con coste; 10-11 = éxito; 12+ = éxito crítico.

Solo se tira cuando existen incertidumbre y una consecuencia interesante. Antes de tirar, el GM declara el riesgo y el jugador confirma objetivo y método. Una tirada resuelve tanto la acción como la respuesta de la oposición.

## Combate

El sistema completo está en `docs/combate.md`.

- Sin HP: heridas en niveles 0-4 y consecuencias coherentes con la posición.
- Sin tiradas enemigas separadas: la amenaza modifica presión, posición y efecto.
- Un intercambio importante por beat; se actualiza el estado y se devuelve la decisión.
- Relojes de 4/6/8 segmentos para conflictos con varios objetivos.
- Pool, scars, drenaje, Ecos y rewind conservan sus reglas de `docs/quirk_pc.md`.
- Herramienta oficial: `python3 tools/resolver_accion.py --help`.

## Marco legal del uso de Quirks (regla canónica, fijada S9/D9)

> **Regla rectora (propuesta del jugador, adoptada):** *"Los quirks constitutivos no se sancionan; los quirks activados se sancionan cuando alteran el espacio público, afectan a terceros, dan ventaja en una acción ilegal o sustituyen trabajo heroico autorizado."*

Esto separa dos capas que la campaña mezclaba:

- **Capa LEGAL** (esta regla): qué puede hacer un ciudadano/estudiante sin licencia de héroe.
- **Capa OPSEC/estratégica** (aparte): qué esconde Akari por el borrado (maestría real + aspecto temporal Ecos/rewind + Corvax/vuelo). Algo puede ser *legal* y aun así *taboo estratégico*. No confundir.

### Aplicación al Quirk de Akari

| Uso | Categoría | ¿Sancionable sin licencia? |
|---|---|---|
| **Percepción sanguínea** (sentido pasivo, mutant) | Constitutivo | No — libre siempre |
| **Coloración/segunda piel sobre su propio cuerpo** | Constitutivo (estético, como el rosa de Ashido) | No — libre |
| **Vines/raíces menores desde su piel** que no invaden ni afectan a nadie | Constitutivo/gris | No, si no altera espacio ni toca a terceros |
| **Bestias** (Blackroot, Corvax, gorila…) en la calle | Activado | **Sí** — alteran espacio público / afectan terceros |
| **Avatar Carmesí** en público | Activado | **Sí** |
| **Raíces ancladas a estructuras públicas, catapultas, columpio** | Activado | **Sí** — altera espacio público |
| **Drenaje** con consentimiento en privado | Activado, pero privado + consentido + sin terceros | **No** (limpio legalmente; el riesgo es OPSEC/ético, no legal) |
| **Segunda piel sobre un tercero** con su consentimiento, en privado | Activado, privado + consentido | **No** |

### Contextos que LEVANTAN la sanción (uso activado permitido)

1. **Autodefensa / emergencia** (canon MHA): parar un villano, un rescate — cubierto.
2. **Recinto autorizado**: UA, campos de entrenamiento, exámenes, Fundamentos con All Might — duelo de Quirks consentido.
3. **Espacio privado con consentimiento** y sin terceros afectados (p. ej. el estudio de fotografía prestado, la habitación, un entre-muros discreto).
4. **Bajo licencia** (provisional o plena) en acto de servicio autorizado.

**Corolario práctico:** lo del colector del D9 (bestias en la infraestructura de UA, sin autorización, alterando un espacio semi-restringido) **sí** caía en zona sancionable — coherente con que Aizawa dijo que tendría consecuencia. Lo del estudio con Toru (privado + consentido) es legalmente limpio.

## Entrenamiento y progresión

> Ver `docs/progresion_narrativa.md` y `docs/quirk_pc.md`.

Idea base:
- Cada día de entrenamiento dedicado sube 1 punto de maestría del Quirk.
- Cada arco terminado permite subir 1 stat base.
- Hitos especiales permiten evolución del Quirk (awakening del savia, integración de aspectos,etc.).
- El savia tiene su propia curva de aceptación: si el PC abusa de las bestias o de los Ecos, el savia se "retrae" y bloquea el uso de ciertos aspectos.

## Estado de implementación

- [x] Motor 2d6 definitivo.
- [x] `tools/resolver_accion.py` con CLI reproducible.
- [x] `tools/validar_estado.py` con validación estructural y semántica.
- [x] PC y equipo poblados en `registros/`.
- [ ] Probar el motor en el próximo combate o práctico y registrar ajustes de mesa.
