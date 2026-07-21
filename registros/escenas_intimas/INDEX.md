# Escenas íntimas — archivo narrativo

> **Qué es esto.** Las escenas íntimas de esta campaña se jugaban latido a latido y luego quedaban comprimidas en una línea de `cronologia.csv` ("primera vez, mordida, fragmento X"). La mecánica sobrevivía; **la prosa se perdía**. Este directorio existe para conservar íntegras las que merecen la pena.
>
> Creado en **S28**, a petición del jugador. Se empieza tarde: **todo lo anterior a S28 está sin recuperar** y sólo existe resumido en `cronologia.csv`, `relaciones.csv` y los `sesion_NN.md`. Ver §Deuda de recuperación.

## Convención de nombres

```
S{sesión}_D{día}_{npc-slug}_{nn}_{titulo-slug}.md
```

- **`S28`** — sesión de juego. Ordena el directorio cronológicamente sin esfuerzo.
- **`D36`** — día de campaña (Curso 1 · T1 · Día 36). Permite cruzar con `calendario.md` y `cronologia.csv`.
- **`{npc-slug}`** — NPC en minúsculas y sin tildes (`midnight`, `momo`, `nejire`, `yuyu`). **Es el campo por el que se busca**: `ls *_midnight_*` da la historia íntima completa de un vínculo.
- **`{nn}`** — secuencia de esa NPC dentro de la campaña (`01`, `02`…). No de la sesión: de la relación.
- **`{titulo-slug}`** — título corto y evocador, para reconocer la escena de un vistazo.

Escenas con más de una NPC: slugs unidos por `+` (`nejire+yuyu`).

## Cabecera obligatoria de cada archivo

Cada escena abre con un bloque de estado: fecha/hora de campaña, ubicación, participantes, **estado del vínculo antes → después**, mecánica gastada (pool, fragmentos, drenajes) y consecuencias abiertas. La prosa va después, sin recortes.

## Índice

| Archivo | Día | NPC | Qué es |
|---|---|---|---|
| [S28_D36_midnight_01_el-despacho-de-las-once-y-media.md](S28_D36_midnight_01_el-despacho-de-las-once-y-media.md) | D36 | Midnight | **Primera vez.** El tabú-profesora salta por los aires. Cunnilingus, mordida sellada, fragmento Somnus. |
| [S29_D37_ochaco_01_volvio-aqui.md](S29_D37_ochaco_01_volvio-aqui.md) | D37 | Ochaco | Sexo del alba, la mañana después del preaviso sin nombre. Eco-excitación consentido (escalera + bucle de resonancia); orgasmo compartido. Sin drenaje ni mordida. |
| [S29_D37_kinoko_01_las-setas-que-brillaban.md](S29_D37_kinoko_01_las-setas-que-brillaban.md) | D37 | Kinoko | **Floración + primera vez.** El micelio-hijo revelado; cunnilingus + mordida Tipo A (éxtasis + recuerdo transmitido); primera sangre virgen; savia analgésica; orgasmo simultáneo. Entra al bosque. |

## Deuda de recuperación (pendiente)

Escenas anteriores a S28 que merecerían reconstruirse desde `cronologia.csv` + los `sesion_NN.md` si alguna vez apetece: Momo (S2-S3, S14 entre-muros), Jirō (S14, floración completa), Kendo (S20, virgen/rito), Tsuyu (S20, cita de lluvia), Reiko (S24, Paradise Lost), Ochaco, Setsuna, Nejire, Mei, Yuyu (S28/D36, la mañana de los tres — **jugada en la ventana paralela**).

> **Regla de mesa desde S28**: toda escena íntima con peso se vuelca aquí **en el mismo turno en que se juega**. No se deja para el cierre.
