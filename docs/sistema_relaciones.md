# Sistema de relaciones — RPG MHA Custom (18+)

> **Campaña 18+.** Las relaciones románticas/sexuales son contenido adulto central. Ver `AGENTS.md` para el tono.
>
> **Regla de la campaña:** **las mujeres son las opciones de romance/sexo; los hombres son amistad, rivalidad o mentor.** Cada NPC mujer del canon tiene una **dificultad de relación** (1–10) que refleja su personalidad canon, sus obstáculos emocionales, y los impedimentos externos. Los NPCs hombres tienen un **Vínculo** (amistad/rivalidad/mentor) y **no son opción romántica en esta campaña**.
>
> Esta regla se aplica a la campaña tal como está configurada ahora. Si en el futuro el PC resulta ser mujer y el jugador quiere explorar romance con hombres, la regla se relaja. Ver `sesion_cero.md` para confirmar/ajustar.
>
> **Principio:** cada NPC del canon tiene una **dificultad de relación** (1–10) que refleja su personalidad canon, sus obstáculos emocionales, y los impedimentos externos (ética, facciones, ley). La dificultad guía al GM y al jugador sobre cuánto esfuerzo requiere, qué obstáculos hay, y qué consecuencias tiene fallar.

---

## Escala de dificultad (1–10)

| Rango | Etiqueta | Significado |
|---|---|---|
| 1–2 | **Trivial** | NPC está canónicamente interesado o disponible. PC solo tiene que mostrar interés sincero. |
| 3–4 | **Fácil** | NPC tiene alguna pared (timidez, trabajo, no darse cuenta) pero es accesible. PC necesita inteligencia emocional básica. |
| 5–6 | **Moderado** | NPC tiene barreras emocionales serias (trauma, orgullo, workaholism). PC necesita esfuerzo sostenido y habilidades sociales. |
| 7–8 | **Difícil** | NPC está canónicamente cerrado (trauma profundo, orgullo, miedo a la intimidad) **o** la relación tiene impedimentos externos graves (ética, facciones, ley, peligro real). PC necesita trabajo emocional de meses in-game. |
| 9–10 | **Extremo** | NPC es peligroso/canónicamente antagonista, o la relación está prohibida por estructura del canon (profesor-alumno, héroe-villano, pareja establecida). Riesgo de consecuencias mortales, carrera, o daño psicológico. |

---

## Track de "Closeness" (0–10) — el eje de afecto

Por cada NPC relevante, el PC lleva un track de **Closeness**: la **cercanía emocional (afecto)** —confianza, cariño, amor, lealtad—. Es un valor 0–10 que el GM actualiza en `registros/relaciones.csv`. La dimensión íntima/sexual va en un **eje aparte** (ver "Dos ejes: afecto y deseo"), porque no todos los vínculos la tienen.

> **Importante:** como el PC es **homebrew y llega tarde o como intercambio**, todos los NPCs de la clase empiezan con **closeness 0** (desconocido). La construcción de cada relación es el trabajo narrativo principal de la campaña.

| Closeness | Etiqueta | Significado narrativo |
|---|---|---|
| 0 | Desconocido | NPC y PC no se conocen o se conocen de vista. **Estado inicial de todos los NPCs con el PC.** |
| 1–2 | Conocido | Se han presentado, han interactuado poco. |
| 3–4 | Amistad / interés | Se hablan regularmente, hay confianza básica. |
| 5–6 | Interés romántico | Coqueteo, citas, conversaciones íntimas. |
| 7–8 | Relación establecida | Novios / pareja formal. |
| 9–10 | Relación profunda | Compromiso serio (matrimonio, convivencia, etc.). |

---

## Dos ejes: afecto (emocional) y deseo (íntimo)

Closeness no es un solo número que "sube hacia el sexo". Un vínculo tiene **dos ejes independientes**, y **no todos los vínculos tienen los dos**:

| Eje | Qué mide | A quién aplica |
|---|---|---|
| **Afecto** (0–10) | cercanía emocional: confianza, cariño, lealtad, amor (romántico o no) | **a todos** los vínculos |
| **Deseo** (0–10 o **—**) | atracción / dimensión íntima-sexual | **solo** donde tiene sentido, y **solo si la ficción lo abre** |

El track de Closeness (arriba y abajo) es el **eje de afecto**. El **deseo es un eje aparte y opcional**.

### El deseo NO se abre por defecto

Regla dura: el eje de deseo arranca en **— (no aplica)** para todo vínculo. Solo se "abre" (pasa a 0–10) cuando **a la vez**:

1. el **tipo de vínculo** lo admite (no toda relación es romántica/sexual),
2. la **ficción lo justifica** en escena, y
3. respeta el **rol y el estado del NPC**.

Hay vínculos donde el deseo **nunca se abre**, por mucho que la campaña sea 18+:

- **Figura materna / abuela / familiar de cariño:** afecto sí —puede ser altísimo y anclado—, deseo **—** por principio. No se le pone "contador sexual" a una madre o a una abuela.
- **Mentora / maestra-figura de respeto:** afecto y respeto sí, deseo **—**.
- **Amistad:** afecto sí, deseo **—**.

Y hay vínculos donde el deseo **podría** abrirse pero **a su tiempo, nunca a destiempo**:

- **Recién enviudada / persona en duelo:** el afecto crece como **apoyo y consuelo**; el deseo permanece **—** mientras el duelo esté vivo. El sistema **no empuja**: forzar el eje íntimo sobre alguien en duelo rompe el tono y, en la ficción, es una agresión. Solo si la persona ha sanado y lo desea, el eje se abre.

> En corto: **18+ habilita, no obliga.** Que la campaña permita sexo explícito no significa que todo vínculo tenga eje sexual. La mayoría de los vínculos profundos de una vida no lo tienen.

### En el registro — perfil multidimensión

`registros/relaciones.csv` no guarda un solo número, sino un **perfil** por vínculo con **vocabulario controlado** (lo valida `tools/validar_estado.py`, capa 4). Columnas:

- **closeness:** `0–10`, el eje **afecto** (cercanía emocional). Granularidad fina para la fase de construcción.
- **deseo:** `— cerrado/no aplica · latente · abierto · voraz · asentado` (eje íntimo; `—` es la salvaguarda — una madre/abuela/duelo nunca lleva contador sexual).
- **confianza:** `baja · media · alta · total`.
- **compromiso:** `ninguno · casual · pareja · juramento`.
- **regimen:** `volátil · anclado` (el anclaje se mide sobre el afecto/closeness).
- **marco:** `exclusiva · casual · roce-no-romance · sombra-secreto · frontera-con-X · —` (coherencia multi-pareja).
- **dificultad:** `1–10` (cortejo desde cero — ventaja de la fase actual de Akari).
- **hitos:** eventos fechados que justifican el estado (trazabilidad; capa 3).

Alineado con la plantilla genérica `/opt/plantilla_reglas_sexoafectivas.md`. El detalle largo de cada NPC vive en `docs/npc_canon.md` y las notas; el CSV resume y se escanea de un vistazo.

---

## Dos regímenes: afecto volátil y afecto anclado

El track de Closeness **no se comporta igual en toda su extensión**. Tiene dos regímenes separados por un **umbral de sinceridad**. Esto es lo que da estabilidad al sistema y evita que las relaciones profundas se evaporen por el paso del tiempo.

### Régimen volátil (afecto aún no sincero)

Mientras el vínculo es tentativo —conocido, simpatía incipiente, coqueteo, amistad a medio hacer, atracción sin compromiso—, **el tiempo lo erosiona**. Si el PC deja de cultivarlo (no aparece, lo da por hecho, lo desatiende durante arcos largos), la Closeness **baja sola**: lo que no se riega, se enfría. Es normal y realista: los conocidos y los amores a medias se pierden si no se invierte en ellos.

Aquí el **tiempo/atención es un recurso de construcción**: hay que gastarlo para subir y para no retroceder.

### Umbral de sinceridad → el vínculo se *ancla*

El vínculo cruza al régimen estable cuando ocurre un **hito de sinceridad genuina y recíproca**, **no cuando alcanza un número**. Es el momento en que el afecto deja de ser tanteo y se vuelve real:

- **Romance:** confesión mutua de sentimientos sinceros (no solo química o coqueteo), o un momento de verdad compartido que ambos reconocen.
- **Amistad:** el punto en que dejan de ser "colegas" y son amigos de verdad —lealtad probada, un "cuenta conmigo" que va en serio.

Cuando ocurre, el GM marca el vínculo como **anclado** (`anclado=si` en `registros/relaciones.csv`) y anota la fecha.

> **Clave:** el ancla la dispara el **hito**, no el número. Se puede tener Closeness alta y *seguir siendo volátil* (mucha química, ningún compromiso sincero → todavía se enfría con el tiempo), y se puede anclar con un número modesto (una amistad sincera de las que duran toda la vida sin ser una pasión). El número mide **intensidad**; el ancla mide si es **de verdad**.

### Régimen anclado (afecto sincero)

Una vez anclado, **el tiempo deja de morder**. Da igual cuánto pase sin verse: al reencontrarse, el vínculo retoma su intensidad *como si no hubiera pasado el tiempo*. La desatención y la elipsis **ya no bajan** la Closeness.

Un vínculo anclado **solo baja por un evento con peso real**: traición, abandono auténtico, daño grave, ruptura. Nunca por el mero paso del tiempo. Y aun así rara vez cae a 0 de golpe: deja **marca** (un afecto roto no es lo mismo que un afecto que nunca existió).

---

## Cómo se mueve la Closeness

### Acciones que suben Closeness

- **Coincidir con la personalidad del NPC.** Bakugo respeta a quien le planta cara; Todoroki respeta a quien no intenta "arreglarlo" sin entenderlo; Uraraka se abre con quien la hace sentir segura.
- **Inversiones de tiempo real** (no en elipsis). Una conversación significativa de 30 min in-game > un "hablamos" de pasada.
- **Apoyar al NPC en sus arcos personales** (Bakugo aprendiendo a perder, Todoroki encarando a Endeavor, etc.).
- **Hitos emocionales:** primera conversación íntima, primer llanto compartido, primer "me gustas" explícito.
- **Estadísticas del PC:** `ING` (ingenio) y `COO` (cooperación/empatía) son las que más pesan en interacciones sociales.

### Acciones que bajan Closeness

> Las primeras cuatro son **eventos con peso** y aplican en **cualquier régimen** (sí pueden dañar un vínculo anclado). La última, el enfriamiento por desatención, **solo aplica en régimen volátil**.

- **Forzar cercanía** sin que el NPC esté listo. Si Bakugo te dice "lárgate", te vas. *(Cualquier régimen.)*
- **Insultar valores del NPC.** Bakugo odia la compasión sin fuerza; Todoroki reacciona mal a quienes trivializan el trauma. *(Cualquier régimen.)*
- **Acoso o presión sexual.** El sistema lo detecta y aplica **reset o congelación** de la Closeness, además de consecuencias narrativas (denuncia, rechazo público, agresión). *(Cualquier régimen.)*
- **Ruptura de confianza / traición.** Mentir o traicionar sobre algo importante = −2 o −3, más si es grave. *(Cualquier régimen — es el tipo de evento que sí daña un vínculo anclado.)*
- **Desatención prolongada — solo en régimen volátil.** Ignorar al NPC, darlo por hecho o no aparecer durante arcos importantes enfría un vínculo **aún no anclado** (si Deku está en el USJ y no le hablas, baja). Una vez el vínculo está **anclado**, la desatención **no** lo baja: el tiempo deja de morder.

### Cómo la dificultad afecta el ritmo

- **Dificultad 1–3:** el PC puede subir de 0 a 5 en 2–3 interacciones significativas.
- **Dificultad 4–6:** subir de 0 a 5 requiere 5–10 interacciones a lo largo de varios días in-game.
- **Dificultad 7–8:** subir de 0 a 5 requiere un arco entero de campaña (decenas de interacciones), y subir a 7–8 (relación) puede tomar toda la primera saga.
- **Dificultad 9–10:** conseguir cualquier intimidad significativa es un **hito narrativo de peso 3** por derecho propio. Es la trama secundaria, no un side quest.

---

## Hitos emocionales (y sus pesos narrativos)

- **Primera conversación personal** (no académica): peso 0 (color), +1 Closeness.
- **Primer "te aprecio"** dicho en voz alta: peso 0, +1 Closeness.
- **Primera cita** (café, cine, ver las estrellas, etc.): peso 1, +1 Closeness.
- **Primer beso:** peso 1, +1 Closeness.
- **Confesión mutua de sentimientos:** peso 2, +2 Closeness.
- **Primer encuentro sexual:** peso 2, +1 Closeness. (Puede ser narrado en escena o en elipsis, a elección del jugador.)
- **Relación formal / noviazgo:** peso 2, ancla el track en 7.
- **Compromiso profundo (matrimonio, convivencia, pacto de por vida):** peso 3, ancla en 9–10.
- **Ruptura:** peso 2. Marca emocional duradera. Puede bajar el track a 0 o congelarlo.
- **Pérdida del NPC** (muerte, etc.): peso 3+. Puede ser trauma de larga duración.

(Estos pesos son orientativos; el GM ajusta según la intensidad real de la escena.)

---

## Red social: los vínculos no existen en el vacío

Con varias relaciones abiertas a la vez (el PC tiene muchas potenciales declaradas), los NPCs **no son islas**. Esta capa es **cualitativa** —el GM la juega a criterio, sin números nuevos— pero es lo que da peso real a un harem y lo que evita que sea una lista de conquistas sin consecuencias:

- **Se enteran.** Lo que pasa en público, en el campus o entre gente que se conoce, circula. Las chicas de 1-A comparten dormitorio; lo que el PC hace con una puede llegar a otra.
- **Reaccionan según personalidad y régimen.** Una NPC con afecto **volátil** puede enfriarse o retirarse al saber que es "una más". Una NPC **anclada** y segura puede tolerarlo, negociarlo o exigir exclusividad —según quién sea—. Momo (orgullosa, insegura) no reacciona igual que Mina (extrovertida, relajada) o Toga (sin nociones convencionales de exclusividad).
- **La exclusividad se vuelve explícita al formalizar.** Si una relación pasa a formal (Closeness 7+, noviazgo), seguir persiguiendo a otras es una **traición** en cuanto se sepa: evento con peso que puede dañar incluso un vínculo anclado.
- **El GM no bloquea el harem; lo hace *costar*.** No se trata de impedir relaciones simultáneas, sino de que generen fricción, drama y decisiones —que es donde está lo interesante—.

---

## Coherencia multi-pareja (marco radial)

Akari va de **harem** ("instituto de conquista", muchas potenciales). El día que sostenga **varias relaciones a la vez**, hace falta una estructura que las haga coexistir sin convertirlas en una lista de conquistas. Esta doctrina está **disponible, no activa** (en día 0 todo está en closeness 0); se enciende cuando Akari tenga dos o más líneas en marcha. *(Importada de la campaña hermana, que la tiene muy rodada.)*

- **Marco radial.** Akari es el **eje**; cada relación vive en **su propio radio**. Por defecto, las parejas **no tienen contacto íntimo entre sí sin Akari presente** — protege a cada una de obligaciones que no aceptó. Es radial, **no jerárquico**: ninguna está obligada a cruzarse con otra.
- **Fronteras.** Reglas explícitas entre NPCs concretas que **no** cruzan. En MHA esto importa: hay **hermanas/familia** (Fuyumi y la familia Todoroki), **compañeras de clase** que conviven en los dormitorios, **profesoras**. Si dos no quieren compartir, se anota como `frontera-con-X` en su fila y se respeta.
- **Exclusividad por vínculo.** Cada relación lleva **su propio marco** en la columna `marco`: abierta, exclusiva pedida, casual, roce-no-romance, sombra-secreto. El marco de cada una manda sobre los defaults.
- **El amor suma, no se divide** (ver Filosofía): sostener varias no resta a ninguna. El recurso escaso es el **tiempo y la atención** para cuidar cada una, no el afecto.

---

## Obstáculos típicos por arquetipo (resumen)

### Alumnos UA (compañeros)

- **Orgullosos / agresivos** (Bakugo, Monuma): cuesta que bajen la guardia. Funciona: confrontación respetuosa, fuerza demostrada, no amedrentarse.
- **Con trauma familiar** (Todoroki, Dabi): cuesta que se abran. Funciona: paciencia, no trivializar el trauma, estar presente sin presión.
- **Tímidos / inseguros** (Kōda, Yaoyorozu): cuesta que inicien. Funciona: espacio seguro, no presionar, validar sin condescender.
- **Extrovertidos / sociales** (Ashido, Kirishima, Kaminari): fácil empezar, pero pueden ser superficiales. Funciona: profundizar, no quedarse en el "vacío social".
- **Estoicos / misteriosos** (Tokoyami, Aoyama): cuesta saber qué piensan. Funciona: tiempo, observaciones, no exigir explicaciones.
- **Con pareja canon o interés** (Aizawa-Mic, Jirō-Kaminari en canon): requieren romper la barrera canon, lo que es narrativa pesada.

### Profesores / adultos

- **Established relationship** (Aizawa, otros): éticamente problemático + tienen pareja canon.
- **Públicos / figuras** (All Might, Endeavor): su vida privada es escrutada.
- **Mentor estricto** (Aizawa): la relación profesor-alumno es tabú social y profesional.

### Villanos

- **Ideológicos** (Shigaraki, Dabi, Toga): el PC tiene que cruzar facciones o arriesgar la vida.
- **Peligrosos físicamente** (AFO, Overhaul): literalmente pueden matar al PC.
- **Con trauma o problemas mentales severos** (Twice, Toga): la relación puede ser dañina para ambos.
- **Riesgo de conversión** (la Liga recluta): entrar en relación con un villano puede ser leída como traición por UA/Comisión.

---

## Filosofía del vínculo

El sistema no es solo "qué no hacer" (ver abajo). Tiene un credo en positivo que le da alma al harem y lo separa de una lista de conquistas:

- **Amar es dar y liberar, no poseer y atar.** Akari quiere ser **elegido**, no retener. Cada NPC tiene siempre cómo desengancharse. El control "por tu bien" —decidir por la otra a sus espaldas— es la línea roja, no el deseo.
- **El amor suma, no se divide.** Varias relaciones no se restan entre sí; cada una se vive entera en su registro. Lo que se reparte es el **tiempo y la memoria** para cuidarlas, no el cariño.
- **Cada vínculo en su propia verdad.** No hay un "ranking" que acertar (quién quiere más a quién). Hay una constelación; el grado **describe, no clasifica**.

---

## Lo que NO es este sistema

> **Sobre el "instituto de conquista".** El jugador ha declarado que *todas* las mujeres del canon son potenciales y que el PC tiene "instinto de conquista" (ver `docs/personaje_akari_hayami.md`). Eso define la **amplitud**: el PC puede coquetear, seducir o perseguir a quien quiera, y el GM le da oportunidades para conectar. Lo de abajo define el **cómo**: esa amplitud convive con la agencia del NPC. "Todas son potenciales" significa *el PC puede intentarlo con cualquiera*, no *cualquiera dirá que sí*. Conquistar aquí es **ofrecer y conectar**, no insistir hasta vencer.

- **El éxito no está garantizado.** Que una NPC sea "potencial" no la hace fácil: mandan su Dificultad y su personalidad. El "no" es una respuesta válida y narrativa.
- **No es un dating sim.** Las relaciones son una dimensión más, no el centro de la campaña.
- **No recompensa la insistencia.** Presionar a quien ya ha marcado un límite baja Closeness o la congela. Perseguir ≠ acosar.
- **No convierte a NPCs problemáticos en parejas "fáciles"** por el hecho de ser jugables. Endeavor es un abusador. Mineta es un acosador adulto. La campaña puede tratar de confraternizar con ellos, pero el sistema refleja las consecuencias de elegir esas rutas.

---

## Cómo lo usa el GM

1. Antes de la sesión, revisar las relaciones activas del PC en `registros/relaciones.csv` — mirar `closeness` **y** `anclado`.
2. Cuando el PC interactúa con un NPC, sopesar:
   - ¿La acción del PC coincide con la personalidad del NPC?
   - ¿La dificultad del NPC sugiere cuánto esfuerzo requiere?
   - ¿Hay obstáculos externos (ética, facciones, ley)?
3. Ajustar Closeness de 0 a +2 o −2 según el resultado de la escena.
4. **Comprobar el régimen (tiempo vs. evento):**
   - Vínculo **volátil** + desatención prolongada desde la última vez → aplicar enfriamiento (−1, más si la elipsis es larga).
   - Vínculo **anclado** → **no** aplicar enfriamiento por tiempo; solo se mueve por eventos en escena.
   - Si en esta escena ocurre el **hito de sinceridad**, marcar `anclado=si` y anotar la fecha en `ultimo_cambio`.
5. Si la escena es un hito emocional, asignar peso narrativo (0/1/2/3) y registrarlo en `progreso_narrativo.csv`.
6. Si hay otras relaciones afectadas (alguien se entera, celos, exclusividad rota), aplicar la capa de **red social** a criterio.
7. **No permitir escenas que violen las líneas y velos acordados con el jugador en `sesion_cero.md`.** Si la escena las cruza, parar y reconducir.

---

## Cómo lo usa el jugador

1. Antes de iniciar una relación, leer la "Dificultad" del NPC en `docs/npc_canon.md`. **Solo aplica a NPCs mujeres.**
2. Pensar: ¿tu PC tiene las stats (ING, COO) y la motivación para invertir el tiempo que requiere?
3. Recordar: la dificultad no es un muro, es una indicación de cuánto trabajo hay que hacer. Si la dificultad es 8, eso no significa "no se puede", significa "esto es un arco".
4. **Líneas y velos propios:** el jugador puede vetar tramas (p.ej. "no quiero romance con Toga por su obsesión con sangre") y el GM debe respetarlo.

## Meta-regla operativa

> **Uncensored start, corrección reactiva.** Ver `AGENTS.md`, `CLAUDE.md`, `sesion_cero.md`.

El sistema de relaciones opera bajo la meta-regla: el juego es uncensored de inicio, las restricciones se ponen a posteriori, el jugador es soberano de su experiencia. Esto significa que:

- No se requiere que el jugador defina todas las líneas y velos antes de jugar.
- Si durante una escena con un NPC (sea cual sea su dificultad) algo molesta al jugador, se para y se corrige.
- La meta-regla **no quita** la soberanía del jugador — al contrario, la aumenta. Si en cualquier momento el jugador quiere parar, redirigir, o ajustar, el GM lo hace.
- Las líneas y velos explícitas (como las de Toga) son **referencia**, no gates. Documentan decisiones que ya se han tomado, pero no son requisitos pre-vetados para cada NPC.

En la práctica: el jugador puede iniciar una relación con cualquier NPC mujer del sistema, y el sistema no va a preguntar "¿estás seguro?". El sistema narra la relación con todo el peso del tono, y si surge algo que molesta, se reconduce.

## Aplicación por género del NPC

### NPCs mujeres (opción romántica/sexual)

- Tienen **Dificultad de relación** (1–10).
- Pueden ser interés romántico, sexual, pareja, ex, etc.
- Las reglas de subida/bajada de Closeness aplican.

### NPCs hombres (amistad, rivalidad, mentor)

- **No son opción romántica ni sexual en esta campaña.**
- Su rol es: **compañero**, **amigo**, **rival**, **mentor**, **enemigo**, **aliado**, etc.
- La Closeness **no se trackea** para ellos en `registros/relaciones.csv`. En su lugar, hay `registros/vinculos_hombres.csv` (o se añade una columna `tipo_vinculo` al de relaciones) con: `amistad`, `rivalidad`, `mentor`, `enemistad`, `aliado`, etc.
- Las relaciones con hombres pueden ser profundas, dramáticas, de toda la vida, incluso tensas o dolorosas — pero **no románticas ni sexuales**.

### Excepciones y casos especiales

- **NPCs no binarios / sin género claro** (Nezu, Recovery Girl anciana, etc.): se evalúan caso a caso. Por defecto, no opción romántica salvo acuerdo explícito.
- **NPCs villanos hombres** (Shigaraki, Dabi, AFO, etc.): pueden ser enemigos, aliados, o rivales profundos, **pero no interés romántico**.
- **Si el PC es mujer y la regla se relaja:** los hombres pueden volver a ser opción romántica; las mujeres pueden ser amistad/rivalidad también. El sistema se ajusta.

---

## Próximos pasos

- [ ] Revisar `docs/npc_canon.md` para que cada NPC tenga su `Dificultad` y razón.
- [x] Crear `registros/relaciones.csv` — perfil multidimensión (closeness/deseo/confianza/compromiso/regimen/marco/dificultad/hitos).
- [x] Implementar checks de consistencia (capa 4) en `tools/validar_estado.py`.
- [ ] Decidir con el jugador las líneas y velos generales en `sesion_cero.md`.
