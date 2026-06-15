#!/usr/bin/env python3
import base64
import json
import re
import warnings
from datetime import datetime
from pathlib import Path

import requests

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
AUTH_SOURCE = ROOT / "producto" / "seo_fix_all.py"
PAGE_ID = 1123
WP_URL = "https://www.dermaforyou.com"
CONTACT_URL = "https://www.dermaforyou.com/pide-cita-contacto/"


def auth_header():
    auth = re.search(r'AUTH\s*=\s*"([^"]+)"', AUTH_SOURCE.read_text()).group(1)
    return "Basic " + base64.b64encode(auth.encode()).decode()


def build_content():
    html = (HERE / "index.html").read_text()
    style_body = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    style_body += """
body.page-id-1123 #sidebar,
body.page-id-1123 .sidebar,
body.page-id-1123 rs-module-wrap,
body.page-id-1123 sr7-module { display: none !important; }
body.page-id-1123 #content,
body.page-id-1123 .content,
body.page-id-1123 .wf-container-main,
body.page-id-1123 .wf-wrap,
body.page-id-1123 .sidebar-right .content { width: 100% !important; max-width: none !important; }
body.page-id-1123 #main > .wf-wrap { padding-left: 0 !important; padding-right: 0 !important; }
body.page-id-1123 #main { padding-top: 0 !important; }
body.page-id-1123 .wf-container-main { display: block !important; grid-template-columns: 1fr !important; }
body.page-id-1123 .sidebar-right,
body.page-id-1123 .content-sidebar-wrap { display: block !important; }
body.page-id-1123 .dfy-philosophy blockquote { background: transparent !important; border: 0 !important; box-shadow: none !important; padding: 0 !important; margin: 0 !important; color: var(--dfy-ink) !important; font-size: 22px !important; line-height: 1.4 !important; }
body.page-id-1123 .dfy-philosophy blockquote p { background: transparent !important; color: inherit !important; font: inherit !important; line-height: inherit !important; margin: 0 !important; padding: 0 !important; }
body.page-id-1123 .dfy-philosophy p:empty { display: none !important; }
body.page-id-1123 .dfy-checklist { margin: 0 !important; padding: 0 !important; list-style: none !important; }
body.page-id-1123 .dfy-zone p { line-height: 1.25 !important; margin: 0 !important; }
body.page-id-1123 .dfy-zone h3 { line-height: 1.2 !important; margin: 0 0 2px !important; }
body.page-id-1123 .dfy-tag { margin-bottom: 0.3rem !important; }
body.page-id-1123 .dfy-rule { margin: 0.25rem 0 0.9rem !important; }
body.page-id-1123 .dfy-tag + br,
body.page-id-1123 .dfy-rule + p { display: none !important; margin: 0 !important; padding: 0 !important; height: 0 !important; line-height: 0 !important; }
body.page-id-1123 .dfy-stat-num { line-height: 1.05 !important; margin-bottom: 8px !important; }
body.page-id-1123 .dfy-stat-num + br { display: none !important; }
body.page-id-1123 .dfy-stat-label { display: block !important; line-height: 1.2 !important; }
@media (max-width: 768px) {
  body.page-id-1123 .dfy-philosophy { align-items: flex-start !important; gap: 1.1rem !important; padding: 2.1rem 1.5rem !important; }
  body.page-id-1123 .dfy-philosophy-quote,
  body.page-id-1123 .dfy-checklist { width: 100% !important; flex-basis: auto !important; }
  body.page-id-1123 .dfy-philosophy blockquote { font-size: 20px !important; line-height: 1.32 !important; }
  body.page-id-1123 .dfy-checklist { gap: 0.55rem !important; }
  body.page-id-1123 .dfy-checklist li { font-size: 13px !important; line-height: 1.35 !important; align-items: flex-start !important; }
}
"""
    style_body = re.sub(r"/\*.*?\*/", "", style_body, flags=re.S)
    style_body = re.sub(r"\s+", " ", style_body)
    style_body = re.sub(r"\s*([{}:;,>])\s*", r"\1", style_body)
    style = f"<style>{style_body}</style>"
    wrap = re.search(r'(<div class="dfy-wrap">.*?</div>\s*)<!-- SCHEMA FAQ', html, re.S).group(1)
    schema = re.search(r'(<script type="application/ld\+json">.*?</script>)', html, re.S).group(1)
    carousel_body = re.search(r"<script>\s*(\(function \(\).*?)</script>", html, re.S).group(1)
    carousel_body = re.sub(r"\s+", " ", carousel_body)
    carousel = f"<script>{carousel_body}</script>"
    content = "".join([style, wrap, schema, carousel])
    content = content.replace('href="#contacto"', f'href="{CONTACT_URL}"')
    content = content.replace('href="/contacto"', f'href="{CONTACT_URL}"')
    return content


def main():
    headers = {
        "Authorization": auth_header(),
        "Content-Type": "application/json",
        "User-Agent": "DermaforyouNeuromodulacionDeploy/1.0",
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

    content = build_content()
    payload = {
        "content": {"raw": content},
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
