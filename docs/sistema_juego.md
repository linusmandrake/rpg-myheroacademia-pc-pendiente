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
