#!/usr/bin/env python3
"""
Escanea una comuna chilena (via Overpass API / OpenStreetMap) buscando negocios
sin sitio web o con sitios web con señales de estar desactualizados.

Requiere acceso saliente a internet a overpass-api.de y a los sitios encontrados
(no funciona en entornos con egress restringido a una lista de dominios).

Uso:
    python scan_region.py --comuna "Romeral" --out leads.csv

Dependencias:
    pip install requests
"""
import argparse
import csv
import re
import sys
import time
from datetime import datetime, timezone

import requests

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

BUSINESS_TAGS = (
    'node["shop"](area.a);'
    'way["shop"](area.a);'
    'node["amenity"~"restaurant|cafe|bar|pharmacy|bank|fuel|fast_food|'
    'veterinary|dentist|doctors|kindergarten|car_repair"](area.a);'
    'node["craft"](area.a);'
    'node["office"](area.a);'
    'node["tourism"~"hotel|guest_house|hostel|apartment"](area.a);'
)

OLD_SITE_SIGNALS = [
    (re.compile(r"<frameset", re.I), "usa <frameset> (tecnología obsoleta)"),
    (re.compile(r"flash", re.I), "menciona/usa Flash"),
    (re.compile(r"frontpage|dreamweaver", re.I), "generado con FrontPage/Dreamweaver"),
    (re.compile(r"copyright.{0,15}(19[0-9]{2}|200[0-9]|201[0-5])", re.I), "copyright de hace más de 10 años"),
]


def build_query(comuna: str) -> str:
    return f"""
    [out:json][timeout:60];
    area["name"="{comuna}"]["boundary"="administrative"]->.a;
    ({BUSINESS_TAGS});
    out center tags;
    """


def fetch_businesses(comuna: str) -> list[dict]:
    resp = requests.post(OVERPASS_URL, data={"data": build_query(comuna)}, timeout=90)
    resp.raise_for_status()
    return resp.json().get("elements", [])


def check_site(url: str) -> tuple[str, str]:
    """Devuelve (estado, detalle) para un sitio web dado."""
    if not url:
        return "sin_sitio", "No tiene sitio web"
    if not url.startswith("http"):
        url = "https://" + url
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0 (lead-scanner)"})
    except requests.RequestException as e:
        return "no_accesible", f"No se pudo cargar: {e}"

    signals = []
    if not r.url.startswith("https"):
        signals.append("sin HTTPS")
    if "viewport" not in r.text.lower():
        signals.append("sin meta viewport (no responsive)")
    for pattern, label in OLD_SITE_SIGNALS:
        if pattern.search(r.text):
            signals.append(label)

    if signals:
        return "sitio_antiguo", "; ".join(signals)
    return "sitio_moderno", "Sin señales evidentes de sitio antiguo"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comuna", required=True, help='Nombre de la comuna, ej "Romeral"')
    parser.add_argument("--out", default="leads.csv")
    parser.add_argument("--delay", type=float, default=1.0, help="Segundos entre requests a sitios")
    args = parser.parse_args()

    print(f"Consultando Overpass API para comuna={args.comuna!r}...", file=sys.stderr)
    elements = fetch_businesses(args.comuna)
    print(f"{len(elements)} elementos encontrados en OSM.", file=sys.stderr)

    rows = []
    for el in elements:
        tags = el.get("tags", {})
        name = tags.get("name")
        if not name:
            continue
        website = tags.get("website") or tags.get("contact:website")
        phone = tags.get("phone") or tags.get("contact:phone")
        category = tags.get("shop") or tags.get("amenity") or tags.get("craft") or tags.get("office") or tags.get("tourism") or ""

        estado, detalle = check_site(website)
        rows.append({
            "nombre": name,
            "categoria": category,
            "telefono": phone or "",
            "sitio_web": website or "",
            "estado": estado,
            "detalle": detalle,
            "lat": el.get("lat") or (el.get("center") or {}).get("lat", ""),
            "lon": el.get("lon") or (el.get("center") or {}).get("lon", ""),
        })
        if website:
            time.sleep(args.delay)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [
            "nombre", "categoria", "telefono", "sitio_web", "estado", "detalle", "lat", "lon"
        ])
        writer.writeheader()
        writer.writerows(rows)

    leads = [r for r in rows if r["estado"] in ("sin_sitio", "sitio_antiguo")]
    print(f"Guardado {args.out}: {len(rows)} negocios, {len(leads)} leads "
          f"(sin sitio o sitio antiguo). [{datetime.now(timezone.utc).isoformat()}]", file=sys.stderr)


if __name__ == "__main__":
    main()
