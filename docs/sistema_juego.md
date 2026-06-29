# Sistema de juego — RPG MHA Custom

> **Estado:** esqueleto. Por definir: dados, números finales, fórmulas de progresión.

## Atributos del PC

Borrador propuesto (5 stats, en escala 1–10):

| Stat | Abreviatura | Significado |
|---|---|---|
| **Poder** | `PWR` | Fuerza bruta, capacidad de causar daño. |
| **Velocidad** | `VEL` | Tiempo de reacción, desplazamiento, esquiva. |
| **Técnica** | `TEC` | Habilidad marcial, control fino, combate cuerpo a cuerpo. |
| **Ingenio** | `ING` | Análisis, improvisación,解决问题. |
| **Cooperación** | `COO` | Trabajo en equipo, empatía táctica, comunicación bajo presión. |

Escala:

- 1–2: civil, sin quirk
- 3–4: estudiante UA novel
- 5–6: estudiante UA competente / pro-hero junior
- 7–8: top 10 hero / All Might en su día / Endeavor
- 9–10: Nivel All Might pico / No.1

## Quirk

Tres ejes:

1. **Tipo:** Emitter / Transformation / Mutant
2. **Potencial:** 1–5 estrellas (potencial bruto del quirk)
3. **Maestría:** 1–10 (lo que el PC ha entrenado de su quirk)

**Stat derivada:** `PWR_quirk` o `TEC_quirk` se calcula combinando potencial + maestría.

## Acciones y resolución

> Por definir: d20? 2d6? dado de quirk?

Borrador: **2d6 + stat_mod + modificadores situacionales**. Resultado:

- 2–6: fallo
- 7–9: éxito parcial
- 10–11: éxito
- 12+: éxito crítico

## Combate

> Por definir en `docs/combate.md`. Esqueleto:

- **HP:** `PWR × 3 + TEC × 2 + 10` (borrador)
- **Acción de ataque:** 2d6 + TEC + bonus de quirk
- **Acción de esquiva:** 2d6 + VEL
- **Acción de trabajo en equipo:** 2d6 + COO (PC) + COO (aliado) ÷ 2 (borrador)

## Entrenamiento y progresión

> Ver `docs/entrenamiento.md` y `docs/progresion_narrativa.md`.

Idea base: cada día de entrenamiento dedicado sube 1 punto de maestría del quirk. Cada arco terminado permite subir 1 stat base. Hitos especiales permiten evolución del quirk (cuarto, quinto, sexto huevo de Shōto; el seventh de Deku).

## Próximos pasos

- [ ] Decidir motor de dados
- [ ] Implementar `tools/resolver_accion.py`
- [ ] Implementar `tools/validar_estado.py`
- [ ] Probar con una sesión corta
