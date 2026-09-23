# Lead Scanner

Herramienta para encontrar negocios locales sin sitio web (o con sitios web
desactualizados) en una comuna chilena, usando datos abiertos de OpenStreetMap
(Overpass API).

## Uso

```bash
pip install requests
python scan_region.py --comuna "Romeral" --out leads_romeral.csv
```

Genera un CSV con: nombre, categoría, teléfono, sitio web (si tiene), estado
(`sin_sitio` / `sitio_antiguo` / `sitio_moderno` / `no_accesible`) y el detalle
de las señales detectadas.

## Cómo detecta un "sitio antiguo"

Heurísticas simples sobre el HTML del sitio:
- No usa HTTPS.
- No tiene meta tag `viewport` (no es responsive / mobile-friendly).
- Usa `<frameset>`, menciona Flash, o fue generado con FrontPage/Dreamweaver.
- Tiene un año de copyright de hace más de 10 años.

Estas son señales indicativas, no una auditoría completa — conviene revisar
manualmente los candidatos antes de contactarlos.

## Requisitos de red

Este script necesita salida a internet abierta: consulta `overpass-api.de` y
luego visita cada sitio web candidato directamente. **No funciona** en entornos
con egress restringido a una lista de dominios permitidos (como algunas
sesiones en la nube) — en ese caso, la alternativa usada fue investigación
manual vía búsqueda web (ver `leads/romeral_maule/REPORTE.md`).

## Cobertura de OpenStreetMap

OSM depende de que voluntarios hayan mapeado los negocios, así que en comunas
rurales chicas la cobertura puede ser parcial. Para complementar conviene:
- Cruzar con el listado de patentes comerciales de la municipalidad (portal de
  transparencia o "Rentas" municipal).
- Buscar manualmente en Facebook/Instagram/Google Maps por rubro, ya que
  muchos negocios pequeños solo tienen presencia en redes sociales.
