# Niebla del bosque — quién conoce a quién

> **Regla base** ([[niebla-informacion-npc]]): cada flor sabe **sólo** lo que presenció o lo que le contaron. **No se cruza información entre NPCs.** Que dos personas estén en el bosque no significa que se conozcan como tales.
>
> **Momo es el ÁRBOL MADRE**: la única que hoy conoce a todas — **excepto a Midnight**, que es la deuda de marco abierta del D36.
>
> **La identidad de Momo es SECRETA.** Sólo se revela si ella quiere. Akari puede dar todos los demás nombres, el suyo no. **La conocen dos: Nejire (por derecho) y Yuyu (por un escape de Nejire, sellado).**

## Grafo

> **Bandas horizontales por closeness.** Momo va sola en la banda **10+**: no es un peldaño más, es el eje.
>
> **Las flechas sólo existen si hay conocimiento real.** El vacío significa que no se conocen — que es el caso de casi todas.

```mermaid
graph TD
    subgraph B11["★ 10+ · ÁRBOL MADRE"]
        direction LR
        MO["🌳 MOMO<br/><i>identidad secreta</i><br/>conoce a TODAS menos Midnight"]
    end

    subgraph B10["10"]
        direction LR
        NE["NEJIRE"]
        JI["JIRŌ"]
        TS["TSUYU"]
    end

    subgraph B9["9"]
        direction LR
        NI["🌙 MIDNIGHT<br/><i>florece D36</i>"]
        OC["OCHACO"]
        KE["KENDO"]
    end

    subgraph B8["8"]
        direction LR
        MI["MINA"]
        TO["TŌRU"]
        ME["MEI"]
    end

    subgraph B7["7"]
        direction LR
        IB["IBARA"]
    end

    subgraph B6["6"]
        direction LR
        PO["PONY"]
    end

    subgraph B5["5"]
        direction LR
        AW["AWATA"]
    end

    subgraph B4["4"]
        direction LR
        YU["YUYU"]
        SE["SETSUNA"]
        KI["KINOKO"]
        RE["REIKO"]
    end

    B11 ~~~ B10 ~~~ B9 ~~~ B8 ~~~ B7 ~~~ B6 ~~~ B5 ~~~ B4

    NE ==>|"sabe quién es"| MO
    YU ==>|"se le escapó a Nejire<br/>SELLADO"| MO
    YU <-->| NE
    OC <-->|"hermanas de bosque"| MI
    JI <-->|"la segunda piel"| TO

    style MO fill:#2d5016,color:#fff,stroke:#7cb342,stroke-width:4px
    style NI fill:#4a148c,color:#fff,stroke:#ce93d8,stroke-width:2px
    style NE fill:#01579b,color:#fff
    style YU fill:#37474f,color:#fff
    style OC fill:#5d4037,color:#fff
    style MI fill:#5d4037,color:#fff
    style JI fill:#4e342e,color:#fff
    style TO fill:#4e342e,color:#fff
```

**Fuera del grafo por definición:** **AKARI**, que conoce a todas y es el único radio de cada una. Dibujar sus diecisiete aristas sólo taparía lo que importa.

**Cuatro aristas en diecisiete flores.** Eso es el mapa entero.

## Lectura del grafo

- **Cuatro aristas.** Diecisiete flores y sólo cuatro líneas. El bosque **no es una red: es una estrella**, y cada radio existe por separado.
- **Dos aristas suben** (hacia Momo) y **dos son horizontales**. Las horizontales son las únicas relaciones entre iguales que existen: **Ochaco ↔ Mina** ("hermanas de bosque", S20/D25) y **Jirō ↔ Tōru** (la segunda piel como espejo, S20). Las dos nacieron de un destape **deliberado**.
- **De las dos que suben, sólo una es legítima.** Nejire lo sabe por derecho; Yuyu por un escape.
- **Trece flores no tienen ninguna arista.** Saben que hay un bosque; no saben quién más lo habita. Y no lo sabrán salvo que Akari lo decida.
- **Yuyu está en la banda 4 y conoce más que las de la banda 10.** El closeness mide el vínculo, no el acceso — y esa asimetría es un riesgo abierto, no una curiosidad.

## Lo que Akari puede ofrecer (declarado S28)

A **Ochaco**, si ella lo pide: **todos los nombres menos el de Momo.** El de Momo es secreto y sólo lo levanta ella.

## Quién conoce la identidad de Momo — CONFIRMADO (S28)

**Dos personas, y la segunda por accidente:**

1. **NEJIRE** — corona. Lo sabe por derecho propio.
2. **YUYU** — **se le escapó a Nejire** (S27). Confirmado por el jugador en S28: no es sólo el apellido, **la conoce**. Gestionado como leak y **sellado**.

De ese escape nace el **protocolo OPSEC de 3 reglas** que Momo redactó para Nejire y entregó el D36: *apellidos sólo dentro del perímetro · ¿protege o sólo emociona? · si falla, se dice y se repara sin esconderlo*. **Formación, no sanción** — porque *"no falla por descuido, falla por generosidad"*.

## Pendiente de niebla (D36)

🔴 **Momo no sabe lo de Midnight.** Floración nueva → deuda de marco, y con Midnight **cara a cara**, no por mensaje.
