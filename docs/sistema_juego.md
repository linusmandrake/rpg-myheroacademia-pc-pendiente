# Sistema de juego — RPG MHA Custom

> **Estado:** esqueleto con Quirk del PC definido. Por decidir: motor de dados final y fórmulas de progresión.

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

**Stats derivadas del Quirk:**
- `PWR_quirk` o `TEC_quirk` = potencial + maestría + bono por aspecto activo.
- **Aspectos activos** (cuántas proyecciones tiene el PC fuera) modifican el consumo y la fatiga.

## Acciones y resolución

Borrador: **2d6 + stat_mod + modificadores situacionales**. Resultado:

- 2–6: fallo
- 7–9: éxito parcial
- 10–11: éxito
- 12+: éxito crítico

**Modificadores por aspecto del Quirk:**
- Cuerpo del PC: +0 a +3 según stats base + maestría.
- Avatar Carmesí activo: +1 a PWR_quirk (cuerpo adicional).
- Bestias del Savia activas: +1 a TEC_quirk (apoyo táctico).
- Ecos Temporales activos: +1 a ING (información de momentos pasados).
- Combinaciones (2+ aspectos a la vez): bonus, pero aumenta el consumo de sangre y el cansancio.

## Combate

> Por definir en `docs/combate.md`. Esqueleto:

- **HP:** `PWR × 3 + TEC × 2 + 10` (borrador) + bonus por armadura de plantasangre.
- **Acción de ataque:** 2d6 + TEC + bonus de Quirk.
- **Acción de esquiva:** 2d6 + VEL + bonus de Avatar Carmesí si está activo.
- **Acción de trabajo en equipo:** 2d6 + COO (PC) + COO (aliado) ÷ 2 + Bestias del Savia si están protegiendo.
- **Rewind:** acción especial, gasta sangre + memoria. 1 vez por combate al inicio, 2–3 a mid, 5+ a endgame (con memory scars).
- **Drenaje de sangre:** acción especial, ver `docs/quirk_pc.md` sección "Drenaje de sangre". Coste 15 sangre; recuperación variable según compatibilidad de tipo. 1 acción de combate. Riesgo: backlash del Quirk del enemigo, memoria traumática, intoxicación si incompatible.
- **Donación de sangre:** acción especial, ver `docs/quirk_pc.md` sección "Efectos de la sangre del PC en otros cuerpos". Coste variable (30 para curación leve, 60 para grave, 100 para crítico, 200 para resurrección). Efectos: curación, regeneración, conversión, vínculo permanente, resurrección. Riesgo: savia se encariña con cuerpo ajeno, recipiente se vuelve dependiente.

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

## Próximos pasos

- [ ] Decidir motor de dados final
- [ ] Implementar `tools/resolver_accion.py` con las mecánicas del Quirk
- [ ] Implementar `tools/validar_estado.py` con checks de consistency
- [ ] Probar con una sesión corta
- [ ] Cuando el PC se defina: poblar `registros/equipo_pc.csv` con las capacidades del Quirk
