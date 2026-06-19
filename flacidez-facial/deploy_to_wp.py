#!/usr/bin/env python3
import base64
import json
import re
import warnings
from datetime import datetime
from pathlib import Path

import requests

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
AUTH_SOURCE = ROOT / "producto" / "seo_fix_all.py"
PAGE_ID = 10396
WP_URL = "https://www.dermaforyou.com"
CONTACT_URL = "https://www.dermaforyou.com/pide-cita-contacto/"
TEMPLATE = HERE / "design-1-clinico.html"

SCHEMA = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["MedicalBusiness", "Dermatology"],
      "@id": "https://www.dermaforyou.com/#clinic",
      "name": "Dermaforyou",
      "url": "https://www.dermaforyou.com/",
      "telephone": "+34680635080",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Avenida de la Constitucion 8",
        "addressLocality": "Talavera de la Reina",
        "addressRegion": "Toledo",
        "postalCode": "45600",
        "addressCountry": "ES"
      },
      "areaServed": ["Talavera de la Reina", "Toledo", "Madrid"]
    },
    {
      "@type": "MedicalTherapy",
      "@id": "https://www.dermaforyou.com/flacidez-facial/#service",
      "name": "Tratamiento de flacidez facial",
      "url": "https://www.dermaforyou.com/flacidez-facial/",
      "provider": {"@id": "https://www.dermaforyou.com/#clinic"}
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.dermaforyou.com/flacidez-facial/#faq",
      "mainEntity": [
        {"@type": "Question", "name": "Donde se realiza el tratamiento de flacidez facial?", "acceptedAnswer": {"@type": "Answer", "text": "El tratamiento se realiza en Dermaforyou, Avenida de la Constitución 8, Talavera de la Reina, Toledo."}},
        {"@type": "Question", "name": "Que tratamiento necesito para la flacidez facial?", "acceptedAnswer": {"@type": "Answer", "text": "Depende de si predomina la pérdida de soporte, la calidad de piel o ambas. Por eso la valoración médica previa es imprescindible."}},
        {"@type": "Question", "name": "El resultado se ve natural?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. El objetivo es recuperar definición y firmeza sin inflar el rostro ni modificar los rasgos."}},
        {"@type": "Question", "name": "Puedo combinar tratamientos?", "acceptedAnswer": {"@type": "Answer", "text": "Sí. En muchos casos combinar Triángulo Armónico, Triple Láser u otras técnicas mejora el resultado global."}}
      ]
    }
  ]
}
</script>
"""


def auth_header():
    auth = re.search(r'AUTH\s*=\s*"([^"]+)"', AUTH_SOURCE.read_text()).group(1)
    return "Basic " + base64.b64encode(auth.encode()).decode()


def build_content():
    html = TEMPLATE.read_text()
    style_body = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    page_css = f"""
body.page-id-{PAGE_ID} #sidebar,
body.page-id-{PAGE_ID} .sidebar,
body.page-id-{PAGE_ID} rs-module-wrap,
body.page-id-{PAGE_ID} sr7-module,
body.page-id-{PAGE_ID} #main-slideshow,
body.page-id-{PAGE_ID} .page-title-bar,
body.page-id-{PAGE_ID} h1.entry-title,
body.page-id-{PAGE_ID} .breadcrumbs {{ display: none !important; }}
body.page-id-{PAGE_ID} #content,
body.page-id-{PAGE_ID} .content,
body.page-id-{PAGE_ID} .entry-content,
body.page-id-{PAGE_ID} .post-content,
body.page-id-{PAGE_ID} article.page,
body.page-id-{PAGE_ID} .wf-container-main,
body.page-id-{PAGE_ID} .wf-wrap,
body.page-id-{PAGE_ID} .sidebar-right .content {{ width: 100% !important; max-width: none !important; }}
body.page-id-{PAGE_ID} #main > .wf-wrap {{ padding-left: 0 !important; padding-right: 0 !important; }}
body.page-id-{PAGE_ID} #main {{ padding-top: 0 !important; padding-bottom: 0 !important; }}
body.page-id-{PAGE_ID} .wf-container-main {{ display: block !important; grid-template-columns: 1fr !important; }}
body.page-id-{PAGE_ID} .sidebar-right,
body.page-id-{PAGE_ID} .content-sidebar-wrap {{ display: block !important; }}
body.page-id-{PAGE_ID} .dfy-wrap .dfy-hero .dfy-hero__content p {{ color: #fff !important; }}
body.page-id-{PAGE_ID} .dfy-wrap .philosophy blockquote {{ background: transparent !important; border: 0 !important; box-shadow: none !important; padding: 0 !important; margin: 0 !important; color: var(--ink) !important; font-size: 31px !important; line-height: 1.24 !important; font-weight: 700 !important; font-family: Georgia, serif !important; }}
body.page-id-{PAGE_ID} .dfy-wrap .philosophy blockquote::before,
body.page-id-{PAGE_ID} .dfy-wrap .philosophy blockquote::after {{ display: none !important; }}
body.page-id-{PAGE_ID} .dfy-wrap .cta a.btn,
body.page-id-{PAGE_ID} .dfy-wrap .cta a.btn:visited,
body.page-id-{PAGE_ID} .dfy-wrap .cta a.btn:hover,
body.page-id-{PAGE_ID} .dfy-wrap .cta a.btn:focus {{ background: var(--rose) !important; color: #fff !important; border: 0 !important; text-decoration: none !important; }}
body.page-id-{PAGE_ID} .checklist {{ margin: 0 !important; padding: 0 !important; list-style: none !important; }}
body.page-id-{PAGE_ID} .stat strong {{ line-height: 1.05 !important; margin-bottom: 8px !important; }}
body.page-id-{PAGE_ID} .stat span {{ display: block !important; line-height: 1.2 !important; }}
@media (max-width: 768px) {{
  body.page-id-{PAGE_ID} .philosophy {{ align-items: flex-start !important; gap: 1.1rem !important; padding: 2.1rem 1.5rem !important; }}
  body.page-id-{PAGE_ID} .checklist li {{ font-size: 13px !important; line-height: 1.35 !important; }}
}}
"""
    style_body += page_css
    style_body = re.sub(r"/\*.*?\*/", "", style_body, flags=re.S)
    style_body = re.sub(r"\s+", " ", style_body)
    style_body = re.sub(r"\s*([{}:;,>])\s*", r"\1", style_body)
    style = f"<style>{style_body}</style>"
    wrap = re.search(r'(<div class="dfy-wrap">.*</div>)\s*</body>', html, re.S).group(1)
    cleaner = """
<script>
(function () {
  document.querySelectorAll('link[href*="/revslider/"], script[src*="/revslider/"], link[id*="sr7"], script[id*="sr7"], script[id*="tp-tools"], sr7-module, rs-module-wrap').forEach(function (node) {
    node.remove();
  });
})();
</script>
"""
    content = "".join([style, wrap, SCHEMA, cleaner])
    content = content.replace('href="#contacto"', f'href="{CONTACT_URL}"')
    content = content.replace('href="/contacto"', f'href="{CONTACT_URL}"')
    return content


def main():
    headers = {
        "Authorization": auth_header(),
        "Content-Type": "application/json",
        "User-Agent": "DermaforyouFlacidezDeploy/1.0",
    }

    current = requests.get(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit",
        headers=headers,
        verify=False,
        timeout=30,
    )
    current.raise_for_status()
    page = current.json()

    backup_dir = HERE / "backups"
    backup_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = backup_dir / f"page-{PAGE_ID}-{stamp}.json"
    backup_path.write_text(json.dumps(page, ensure_ascii=False, indent=2))

    payload = {
        "content": {"raw": build_content()},
        "template": "",
        "status": "publish",
    }
    updated = requests.post(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        headers=headers,
        json=payload,
        verify=False,
        timeout=45,
    )
    print("backup", backup_path)
    print("status", updated.status_code)
    print(updated.text[:1000])
    updated.raise_for_status()


if __name__ == "__main__":
    main()
