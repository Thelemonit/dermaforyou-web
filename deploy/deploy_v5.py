#!/usr/bin/env python3
"""
Deploy completo homepage v5 — Dermaforyou
CSS limpio + contenido correcto + footer oscuro + blog dinámico
Despliega directamente a WordPress via REST API y XML-RPC
"""

import requests, base64, warnings, json, re, time
warnings.filterwarnings('ignore')

WP_URL  = 'https://www.dermaforyou.com'
WP_USER = 'mcp_server'
WP_PASS = '<WORDPRESS_APP_PASSWORD>'  # Reemplazar con contraseña real

creds_b64    = base64.b64encode(f'{WP_USER}:{WP_PASS}'.encode()).decode()
REST_HEADERS = {
    'Authorization': f'Basic {creds_b64}',
    'Content-Type': 'application/json'
}

# CSS y CONTENT se cargan desde los archivos del repositorio
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'css', 'homepage.css')) as f:
    CSS = f.read()

with open(os.path.join(BASE_DIR, 'homepage', 'content.html')) as f:
    CONTENT = f.read()

# ── PASO 1: Crear custom_css post vía XML-RPC ──────────────────────────────
print('Paso 1: Creando post CSS vía XML-RPC…')
css_escaped = CSS.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
xml_body = f"""<?xml version="1.0"?>
<methodCall>
  <methodName>wp.newPost</methodName>
  <params>
    <param><value><int>1</int></value></param>
    <param><value><string>{WP_USER}</string></value></param>
    <param><value><string>{WP_PASS}</string></value></param>
    <param><value><struct>
      <member><name>post_type</name><value><string>custom_css</string></value></member>
      <member><name>post_status</name><value><string>publish</string></value></member>
      <member><name>post_title</name><value><string>dermaforyou-homepage</string></value></member>
      <member><name>post_name</name><value><string>dt-the7</string></value></member>
      <member><name>post_content</name><value><string>{css_escaped}</string></value></member>
    </struct></value></param>
  </params>
</methodCall>"""

r1 = requests.post(f'{WP_URL}/xmlrpc.php', data=xml_body.encode('utf-8'),
    headers={'Content-Type':'text/xml; charset=utf-8'}, verify=False, timeout=30)
m = re.search(r'<string>(\d+)</string>', r1.text)
if not m:
    print('ERROR creando CSS post:', r1.text[:300]); exit(1)
css_post_id = int(m.group(1))
print(f'  CSS post ID: {css_post_id}')

# ── PASO 2: Actualizar página 1100 ────────────────────────────────────────
print('\nPaso 2: Actualizando página 1100…')
r2 = requests.post(f'{WP_URL}/wp-json/wp/v2/pages/1100',
    headers=REST_HEADERS, json={'content': {'raw': CONTENT}},
    verify=False, timeout=30)
print(f'  Status: {r2.status_code}')

# ── PASO 3: Actualizar theme_mods ─────────────────────────────────────────
print('\nPaso 3: Actualizando theme_mods…')
mods = {'custom_css_post_id': css_post_id, 'nav_menu_locations': {'primary': 5674, 'mobile': 5674}}
requests.post(f'{WP_URL}/wp-json/wc-admin/options',
    headers=REST_HEADERS, json={'theme_mods_dt-the7': mods}, verify=False)

time.sleep(3)
print('✅ Deploy completado — purga LiteSpeed Cache y recarga en incógnito')
