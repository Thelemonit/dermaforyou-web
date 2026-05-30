#!/usr/bin/env python3
"""
SEO/AEO fixes for all 3 product pages:
1. Fix Skinlayer meta description (CSS was leaking into excerpt)
2. Add FAQPage schema (JSON-LD) to all 3 pages
3. Add Physician schema (JSON-LD) to all 3 pages
"""
import urllib.request, base64, json, ssl, re

AUTH = "mcp_server:NXSn 3SGn YXUy YhCU hQBH iGZU"
AUTH_HEADER = "Basic " + base64.b64encode(AUTH.encode()).decode()
HEADERS = {
    "Authorization": AUTH_HEADER,
    "User-Agent":    "curl/8.7.1",
    "Accept":        "*/*",
    "Content-Type":  "application/json",
}
ctx = ssl._create_unverified_context()

PHYSICIAN_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Physician",
    "name": "Dra. Carmen Galera",
    "description": "Dermatóloga especialista en dermatología clínica, estética y cosmética médica. Fundadora de Dermaforyou.",
    "medicalSpecialty": "Dermatology",
    "url": "https://www.dermaforyou.com",
    "worksFor": {
        "@type": "MedicalBusiness",
        "name": "Dermaforyou",
        "url": "https://www.dermaforyou.com",
        "telephone": "+34601370561",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Avda. Constitución 8",
            "addressLocality": "Talavera de la Reina",
            "postalCode": "45600",
            "addressCountry": "ES"
        }
    }
}

PAGES = {
    "Skinlayer Test": {
        "id": 8959,
        "excerpt": "Análisis y prescripción personalizada de cosmética médica elaborada por la Dra. Carmen Galera, dermatóloga especialista. Resultado digital en 48–72 h laborables. Incluye 30 € de descuento en tu primer pedido de productos superior a 200 €.",
        "faq": [
            ("¿Cuándo recibiré mi prescripción?",
             "El resultado digital llega en un plazo de 48 a 72 horas laborables desde que envíes el formulario completo."),
            ("¿El descuento de 30 € se aplica automáticamente?",
             "Sí. Si decides comprar los productos recomendados en la web y el pedido supera los 200 €, los 30 € de descuento se aplican automáticamente al finalizar la compra."),
            ("¿La prescripción es válida para cualquier tipo de piel?",
             "El test está diseñado para adaptarse a todos los tipos de piel: seca, grasa, mixta, sensible o con patologías específicas como rosácea o acné."),
            ("¿Puedo consultar dudas después de recibir la prescripción?",
             "Sí. Para dudas adicionales puedes escribir a carmengalera@dermaforyou.com o solicitar una consulta online."),
        ]
    },
    "Consulta Dermatológica Diferida": {
        "id": 8443,
        "excerpt": None,  # already correct, don't overwrite
        "faq": [
            ("¿En cuánto tiempo recibiré respuesta?",
             "La Dra. Carmen Galera se compromete a contestar tu consulta en un plazo máximo de 2 días laborables, a excepción de enfermedad, períodos vacacionales o festivos."),
            ("¿Dónde recibiré la respuesta a mi consulta?",
             "La recibirás al WhatsApp del teléfono que facilites cuando cumplimentes el formulario."),
            ("¿Puedo obtener una receta médica a través de esta consulta?",
             "Sí. Si la doctora considera oportuno recetar algún tipo de tratamiento, te mandará las recetas electrónicas junto con tu informe por WhatsApp."),
            ("¿Puedo renovar la receta de algún medicamento?",
             "Sí, previo abono de la consulta."),
            ("¿La consulta diferida sustituye a la visita presencial?",
             "Depende del motivo de consulta. En cualquier caso ayudará a resolver problemas cutáneos menores, proporcionar orientación de tratamiento, hacer seguimiento de patologías ya diagnosticadas y realizar una primera valoración de patologías sin diagnosticar."),
            ("¿Sustituye a un servicio de urgencias?",
             "No. Este tipo de consulta no sustituye a un servicio de urgencias."),
            ("¿El importe se deduce del coste de un procedimiento posterior?",
             "No, el importe no se deduce del coste del procedimiento."),
            ("¿Siempre atenderá mi consulta la Dra. Carmen Galera?",
             "Sí."),
            ("¿Cómo se efectúa el pago?",
             "El pago de la consulta se realiza a través de la pasarela de pago segura de esta web."),
            ("¿Mi privacidad está garantizada?",
             "Sí. Dermaforyou aplica de forma estricta todas las disposiciones legales de la ley de protección de datos."),
            ("¿Puedo utilizar mi compañía de seguros médicos?",
             "No, no atendemos con compañías de seguros médicos, solo reembolsos."),
            ("Si tengo más dudas, ¿a quién puedo contactar?",
             "Puedes escribirnos un WhatsApp al (+34) 601 370 561."),
        ]
    },
    "Consulta Dermatológica por Videollamada": {
        "id": 8523,
        "excerpt": None,
        "faq": [
            ("¿En cuánto tiempo recibiré respuesta tras el pago?",
             "La Dra. Carmen Galera se compromete a contestar tu consulta en un plazo máximo de 2 días laborables, a excepción de enfermedad, de períodos vacacionales o de festivos."),
            ("¿Dónde recibiré la respuesta a mi consulta?",
             "La recibirás al WhatsApp del teléfono que facilites cuando cumplimentes el formulario."),
            ("¿A través de este tipo de consulta puedo obtener una receta médica?",
             "Sí. Si la doctora considera oportuno recetar algún tipo de tratamiento, te mandará las recetas electrónicas junto con tu informe por WhatsApp."),
            ("¿Puedo renovar la receta de algún medicamento a través de la consulta?",
             "Sí, previo abono de la consulta."),
            ("¿La consulta por videollamada sustituye a la visita presencial?",
             "Depende del motivo de consulta. Ayudará a resolver problemas cutáneos menores, proporcionar orientación de tratamiento, hacer seguimiento de patologías diagnosticadas, realizar una primera valoración de patologías sin diagnosticar e informar del método terapéutico indicado."),
            ("¿La consulta por videollamada sustituye a un servicio de urgencias?",
             "No. Este tipo de consulta no sustituye a un servicio de urgencias."),
            ("¿El importe de la consulta se deduce del coste de un procedimiento posterior?",
             "No, el importe no se deduce del coste del procedimiento."),
            ("¿Siempre atenderá mi consulta la Dra. Carmen Galera?",
             "Sí."),
            ("¿Cómo se efectúa el pago?",
             "El pago de la consulta se realiza por medio de transferencia bancaria."),
            ("¿Mi privacidad está garantizada?",
             "Sí. Dermaforyou aplica de forma estricta todas las disposiciones legales que ordena la ley de protección de datos."),
            ("¿Puedo utilizar mi compañía de seguros médicos?",
             "No, no atendemos con compañías de seguros médicos, solo reembolsos."),
            ("Si tengo más dudas, ¿a quién puedo contactar?",
             "Puedes escribirnos un WhatsApp al (+34) 601 370 561."),
        ]
    }
}

def build_schema_block(faq_items):
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            }
            for q, a in faq_items
        ]
    }
    return (
        '\n<script type="application/ld+json">\n' +
        json.dumps(faq_schema, ensure_ascii=False, indent=2) +
        '\n</script>\n' +
        '<script type="application/ld+json">\n' +
        json.dumps(PHYSICIAN_SCHEMA, ensure_ascii=False, indent=2) +
        '\n</script>\n'
    )

def get_current_content(product_id):
    url = f"https://www.dermaforyou.com/wp-json/wp/v2/product/{product_id}?context=edit"
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    with urllib.request.urlopen(req, context=ctx) as r:
        return json.loads(r.read())

def patch_product(product_id, schema_block, excerpt=None):
    data = get_current_content(product_id)
    raw_content = data.get("content", {}).get("raw", "")

    # Remove any existing ld+json schema blocks we added (avoid duplicates)
    raw_content = re.sub(
        r'\n?<script type="application/ld\+json">.*?</script>\n?',
        '', raw_content, flags=re.DOTALL
    )

    # Inject schema block just before <!-- /wp:html -->
    if "<!-- /wp:html -->" in raw_content:
        raw_content = raw_content.replace("<!-- /wp:html -->", schema_block + "<!-- /wp:html -->")
    else:
        raw_content += schema_block

    payload = {"content": raw_content}
    if excerpt is not None:
        payload["excerpt"] = excerpt

    req = urllib.request.Request(
        f"https://www.dermaforyou.com/wp-json/wp/v2/product/{product_id}",
        data=json.dumps(payload).encode(),
        headers=HEADERS,
        method="POST"
    )
    with urllib.request.urlopen(req, context=ctx) as r:
        resp = json.loads(r.read())
        return resp.get("status"), resp.get("link"), resp.get("modified")

for name, cfg in PAGES.items():
    print(f"\n── {name} (ID {cfg['id']}) ──")
    schema_block = build_schema_block(cfg["faq"])
    status, link, modified = patch_product(cfg["id"], schema_block, cfg["excerpt"])
    print(f"  Status: {status} | Modified: {modified}")
    print(f"  Link: {link}")

print("\n✅ Done")
