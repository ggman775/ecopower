# Leads de negocios sin sitio web — Romeral, Región del Maule

Fecha del escaneo: 2026-09-23

## Metodología

1. **Búsqueda dirigida por rubro**: se realizaron más de 15 búsquedas segmentadas por categoría
   de negocio (minimarkets, restaurantes, ferreterías, agro/packing, turismo rural, viñas,
   salud, educación inicial, transporte, etc.) combinando "Romeral" + "Maule"/"Curicó" con cada
   rubro, para cubrir el comercio local más allá de lo que aparece en una sola búsqueda genérica.
2. **Detección de "sin sitio propio"**: se consideró lead cuando el negocio solo aparece en:
   - Página/perfil de Facebook o Instagram (sin dominio propio),
   - Directorios agregadores de terceros (ude.cl, mundochileno.com, ferreteriaschile.one,
     citiservi.cl, starofservice.cl, Páginas Amarillas), donde el negocio no controla el
     contenido ni la imagen,
   - Mini-sitios gratuitos tipo Google Business Site sin diseño propio.
3. **Detección de "sitio antiguo"**: se buscó evidencia indirecta (antigüedad del negocio,
   tipo de sitio, menciones) para priorizar candidatos a revisión manual.
4. **Búsqueda de teléfono/email** (actualización 2026-09-23): se evaluó usar Apollo.io, pero
   se descartó — Apollo enriquece contactos corporativos vía LinkedIn (cargos, emails de
   empresas con dominio propio) y no tiene cobertura de comercio local chico sin presencia
   corporativo/LinkedIn, que es la mayoría de esta lista. No hay conector de Apollo ni de
   Google Maps/Places disponible en este entorno. En su lugar se hicieron búsquedas dirigidas
   por negocio (nombre + "teléfono"/"contacto"/"whatsapp") para extraer el dato directamente
   de snippets de Facebook, Instagram y directorios locales (Páginas Amarillas, Citiservi,
   ude.cl), que es donde efectivamente circulan los teléfonos de este tipo de negocio.

## Limitación importante de este entorno

El contenedor donde corrió este escaneo tiene el acceso de red restringido a una lista
permitida de dominios (bloqueó, por ejemplo, `overpass-api.de` de OpenStreetMap,
`muniromeral.cl`, y los directorios encontrados). Esto significa que **no pude**:

- Consultar la API de OpenStreetMap (Overpass) para obtener el listado más completo y
  estructurado de comercios de la comuna.
- Abrir directamente cada sitio web candidato para inspeccionar su HTML (SSL, diseño
  responsive, año de copyright, tecnología usada) y confirmar objetivamente si es "viejo".
- Acceder al listado de patentes comerciales de la Municipalidad de Romeral
  (`muniromeral.cl`), que sería la fuente más completa y oficial.

Por eso esta lista es un **primer barrido basado en visibilidad en buscadores** (desk research),
no un catastro exhaustivo. Para una segunda pasada mucho más completa y con verificación
directa de cada sitio, conviene ampliar el "Network access" del entorno (se puede cambiar en
la configuración de la sesión) y correr el script incluido en `tools/lead_scanner/`.

## Resultados: 16 negocios identificados (+1 hallazgo adicional)

Ver [`leads_2026-09-23.csv`](./leads_2026-09-23.csv) para el detalle completo, con columnas de
teléfono, email y si el contacto está verificado (`contacto_verificado`).

**Corrección respecto al primer barrido**: "Jardines de Quilvo" se sacó de la lista — al
buscar su teléfono se descubrió que es una villa/barrio de Romeral, no un negocio de
jardinería. Se agregó en su lugar un hallazgo nuevo: **Restaurant Colo Colo Romeral**, con
teléfono y WhatsApp confirmados.

- **8 negocios con teléfono/email confirmado** vía búsqueda dirigida:
  1. Minimarket Las Brisas de Romeral — +56 9 8645 8615 / franciscocontruccion68@gmail.com
  2. Ferretería FyD Romeral — +56 9 7331 4133 / ferreteriafydchile@gmail.com
  3. Mermeladas María Altamira — +56 9 9884 7914
  4. Jardín Infantil Paso a Pasito — (75) 544296
  5. Restaurant Colo Colo Romeral — (75) 243 1036 / WhatsApp +56 9 9305 6700
  6. Agrofrío Central (grupo Alsu) — +56 9 7588 7846 / contacto@alsu.cl
  7. Silos de Romeral — (75) 238 1660 / +56 9 9887 4019 / silosromeral@tie.cl
  8. Provemat — +56 9 8992 6812 / info@provemat.cl
- **8 negocios sin teléfono confirmado por búsqueda** (hay que sacarlo de su Facebook
  directamente, o visitarlos/llamarlos en terreno): Restaurante El Romeral, Ferretería y
  Construcción ELOI, Panadería Romeral, Punto Romeral Supermarket, Confecciones Romeral,
  Productos Santa Bertina, Jardín Infantil Ñuke Mapu, Frío Frío. En varios casos la búsqueda
  se contaminó con negocios homónimos en España/Argentina (mismo nombre, otro país), así que
  no se quiso inventar un número solo para completar la fila.

### Priorización sugerida (para primer contacto)

**Alta prioridad y con contacto ya confirmado** — empezar por acá:
1. Ferretería FyD Romeral
2. Minimarket Las Brisas de Romeral
3. Restaurant Colo Colo Romeral
4. Mermeladas María Altamira

**Alta prioridad pero sin teléfono confirmado** (contactar por Facebook/Instagram mientras se
verifica el teléfono): Restaurante El Romeral, Ferretería y Construcción ELOI, Productos Santa
Bertina, Punto Romeral Supermarket.

**Baja prioridad**: Agrofrío Central (pertenece al grupo Alsu, que ya tiene sitio web propio —
el decisor real probablemente ya gestiona su imagen web a nivel de grupo), Jardín Infantil
Ñuke Mapu (es un jardín JUNJI público, no un negocio privado).

## Próximos pasos recomendados

1. **Ampliar cobertura**: habilitar acceso de red más amplio en este entorno (o correr el
   script de `tools/lead_scanner/` desde una máquina con internet abierto) para:
   - Consultar Overpass API / OpenStreetMap y obtener un listado más exhaustivo con
     coordenadas y teléfonos.
   - Visitar el listado de patentes comerciales de la Municipalidad de Romeral.
   - Inspeccionar el HTML real de Silos de Romeral y Provemat para confirmar si son sitios
     desactualizados.
2. **Verificar contactos en terreno**: varios teléfonos/direcciones deben confirmarse
   llamando o visitando (esta lista viene de snippets de búsqueda, no de una fuente única
   verificada). Para los 8 negocios sin teléfono confirmado, la vía más rápida es escribirles
   directo por Facebook/Instagram (link en el CSV) y pedir el teléfono o WhatsApp ahí mismo.
3. **Primer contacto**: usar las plantillas de abajo, personalizando el nombre del negocio.

## Plantillas de contacto (WhatsApp / Instagram DM)

**Versión corta (WhatsApp/Instagram):**

> Hola! Vi que [NOMBRE_NEGOCIO] está en Romeral y no tiene página web propia (solo
> [Facebook/Instagram]). Hago sitios web modernos, rápidos y a buen precio para negocios
> locales del Maule — con tu info, fotos, ubicación y botón directo de WhatsApp para que te
> contacten más fácil. ¿Te interesa que te muestre un ejemplo gratis de cómo se vería?

**Versión email (más formal, para empresas como Silos de Romeral / Provemat):**

> Asunto: Propuesta de actualización web para [NOMBRE_EMPRESA]
>
> Estimados,
>
> Mi nombre es [TU_NOMBRE]. Me dedico a diseñar y desarrollar sitios web modernos para
> empresas de la Región del Maule. Al revisar la presencia web de [NOMBRE_EMPRESA] noté una
> oportunidad de modernizar su sitio actual (velocidad de carga, diseño responsive para
> celular, y mejor posicionamiento en Google), lo que puede ayudar a captar más clientes y
> transmitir una imagen más profesional.
>
> Me encantaría mostrarles una propuesta breve sin costo ni compromiso. ¿Tienen 15 minutos
> esta semana para una llamada?
>
> Saludos,
> [TU_NOMBRE / TU_EMPRESA]
> [TU_CONTACTO]
