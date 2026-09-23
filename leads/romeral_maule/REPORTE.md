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

## Resultados: 17 negocios identificados

Ver [`leads_2026-09-23.csv`](./leads_2026-09-23.csv) para el detalle completo. Resumen:

- **13 negocios sin sitio web propio** (solo Facebook/Instagram o directorios de terceros):
  Minimarket Las Brisas, Restaurante El Romeral, Ferretería FyD, Ferretería y Construcción ELOI,
  Panadería Romeral, Punto Romeral Supermarket, Confecciones Romeral, Productos Santa Bertina,
  Jardín Infantil Ñuke Mapu, Jardín Infantil Paso a Pasito, Agrofrío Central, Jardines de Quilvo,
  Frío Frío.
- **1 negocio con mini-sitio gratuito muy básico**: Mermeladas María Altamira (Google Business Site).
- **2 negocios con dominio propio a revisar** (posible sitio antiguo, requiere inspección manual
  o red ampliada): Silos de Romeral (silosderomeral.cl), Provemat (provemat.cl).

### Priorización sugerida (para primer contacto)

**Alta prioridad** (negocio activo y visible, claramente sin web propia, rubro con buen
potencial de conversión online — venta directa, pedidos, reservas):
1. Restaurante El Romeral
2. Ferretería FyD Romeral
3. Ferretería y Construcción ELOI
4. Minimarket Las Brisas de Romeral
5. Productos Santa Bertina
6. Mermeladas María Altamira
7. Punto Romeral Supermarket

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
   verificada).
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
