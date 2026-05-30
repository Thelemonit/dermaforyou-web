#!/usr/bin/env python3
"""
Updates WooCommerce product 8959 (Skinlayer Test) with design C layout.
"""
import urllib.request, base64, json, ssl

WP_BASE = "https://www.dermaforyou.com/wp-json/wp/v2"
AUTH    = "mcp_server:NXSn 3SGn YXUy YhCU hQBH iGZU"
AUTH_HEADER = "Basic " + base64.b64encode(AUTH.encode()).decode()
HEADERS = {
    "Authorization": AUTH_HEADER,
    "User-Agent":    "curl/8.7.1",
    "Accept":        "*/*",
    "Content-Type":  "application/json",
}
ctx = ssl._create_unverified_context()

# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = """
/* ══ SKINLAYER TEST — PRODUCT PAGE OVERRIDE ══ */

/* 1. Ocultar elementos WooCommerce por defecto */
.single-product .woocommerce-product-gallery,
.single-product .entry-summary,
.single-product .woocommerce-tabs > ul.tabs,
.single-product .related.products,
.single-product .up-sells,
.single-product .woocommerce-breadcrumb,
.single-product .page-title-bar,
.single-product .breadcrumbs-title-block,
.single-product .with-title-bar,
.single-product #main-slideshow { display: none !important; }

/* 2. Layout full-width */
.single-product #main { padding-top: 0 !important; margin-top: 0 !important; }
.single-product #main > .wf-wrap { width: 100% !important; max-width: 100% !important; padding: 0 !important; }
.single-product .wf-container-main { display: block !important; width: 100% !important; }
.single-product #content,
.single-product .content-area { width: 100% !important; max-width: 100% !important; padding: 0 !important; }
.single-product .woocommerce-tabs { margin: 0 !important; padding: 0 !important; }
.single-product .woocommerce-Tabs-panel { padding: 0 !important; border: none !important; box-shadow: none !important; }
.single-product .woocommerce-Tabs-panel--description { display: block !important; }
.single-product .the7-post-entry,
.single-product .wpb-content-wrapper,
.single-product .entry-content { padding: 0 !important; margin: 0 !important; }

/* 3. Diseño C — tokens */
:root {
  --rose: #c03c5c;
  --gold: #deb076;
  --cream: #FBF8F5;
  --cream-2: #f2ede6;
  --dark: #1A1A1A;
  --mid: #5a5a5a;
  --mid-light: #888;
  --light: #e5dfd7;
  --white: #fff;
  --clinical: #f7f5f2;
}

.skl-top-bar {
  background: var(--dark);
  color: rgba(255,255,255,.75);
  text-align: center;
  font-size: 12px;
  letter-spacing: .08em;
  padding: 10px 24px;
  font-family: 'Inter', sans-serif;
}
.skl-top-bar strong { color: var(--gold); }

.skl-breadcrumb-bar {
  padding: 14px 48px;
  background: var(--clinical);
  border-bottom: 1px solid var(--light);
  font-size: 12px;
  color: var(--mid-light);
  letter-spacing: .04em;
  font-family: 'Inter', sans-serif;
}
.skl-breadcrumb-bar a { color: var(--mid-light); text-decoration: none; }
.skl-breadcrumb-bar a:hover { color: var(--rose); }
.skl-breadcrumb-bar span { margin: 0 8px; }

.skl-product-section {
  max-width: 1160px;
  margin: 0 auto;
  padding: 56px 48px 64px;
  display: grid;
  grid-template-columns: 480px 1fr;
  gap: 72px;
  align-items: start;
}
.skl-img-panel { position: sticky; top: 80px; }
.skl-img-wrapper {
  background: var(--clinical);
  padding: 24px;
  position: relative;
}
.skl-img-wrapper img {
  width: 100%;
  display: block;
  aspect-ratio: 4/5;
  object-fit: cover;
}
.skl-img-badge {
  position: absolute;
  top: 0;
  right: 0;
  background: var(--dark);
  color: var(--gold);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  padding: 8px 14px;
  font-family: 'Inter', sans-serif;
}
.skl-trust-pills {
  display: flex;
  gap: 8px;
  margin-top: 16px;
  flex-wrap: wrap;
}
.skl-pill {
  background: var(--clinical);
  border: 1px solid var(--light);
  font-size: 11px;
  font-weight: 500;
  color: var(--mid);
  padding: 6px 12px;
  letter-spacing: .04em;
  border-radius: 2px;
  display: flex;
  align-items: center;
  gap: 5px;
  font-family: 'Inter', sans-serif;
}
.skl-content-panel { padding-top: 4px; }
.skl-content-header {
  border-bottom: 1px solid var(--light);
  padding-bottom: 28px;
  margin-bottom: 28px;
}
.skl-category-line {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
}
.skl-cat-tag {
  background: var(--cream);
  border: 1px solid var(--gold);
  color: var(--mid);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: 4px 10px;
  font-family: 'Inter', sans-serif;
}
.skl-cat-divider { flex: 1; height: 1px; background: var(--light); }
.skl-ref-code { font-size: 11px; color: var(--mid-light); font-family: 'Inter', sans-serif; }
.skl-product-title {
  font-family: 'Lora', serif !important;
  font-size: clamp(26px, 2.8vw, 38px) !important;
  font-weight: 500 !important;
  line-height: 1.2 !important;
  margin-bottom: 8px !important;
  color: var(--dark) !important;
}
.skl-product-sub {
  font-size: 14px;
  color: var(--mid);
  line-height: 1.55;
  font-family: 'Inter', sans-serif;
}
.skl-credencial-row {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid var(--light);
  margin-bottom: 28px;
}
.skl-cred-item {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: var(--mid);
  font-family: 'Inter', sans-serif;
}
.skl-cred-icon { font-size: 15px; }
.skl-cred-sep { width: 1px; height: 18px; background: var(--light); }
.skl-price-section {
  background: var(--cream);
  padding: 24px 28px;
  border-left: 4px solid var(--rose);
  margin-bottom: 28px;
}
.skl-price-label {
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mid-light);
  margin-bottom: 8px;
  font-family: 'Inter', sans-serif;
}
.skl-price-number {
  font-family: 'Lora', serif;
  font-size: 42px;
  font-weight: 500;
  color: var(--dark);
  line-height: 1;
  margin-bottom: 10px;
}
.skl-price-number sup { font-size: 20px; vertical-align: super; }
.skl-price-desc {
  font-size: 13px;
  color: var(--mid);
  line-height: 1.55;
  font-family: 'Inter', sans-serif;
}
.skl-price-highlight {
  display: inline-block;
  background: var(--white);
  border: 1px solid var(--gold);
  color: var(--dark);
  font-size: 12px;
  font-weight: 600;
  padding: 3px 8px;
  margin-top: 6px;
}
.skl-indications-block { margin-bottom: 28px; }
.skl-block-title {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mid-light);
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'Inter', sans-serif;
}
.skl-block-title::after { content: ''; flex: 1; height: 1px; background: var(--light); }
.skl-indication-item {
  display: flex;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid var(--light);
  align-items: flex-start;
}
.skl-indication-item:last-child { border-bottom: none; }
.skl-ind-num {
  font-family: 'Lora', serif;
  font-size: 13px;
  color: var(--gold);
  font-style: italic;
  flex-shrink: 0;
  min-width: 20px;
  margin-top: 1px;
}
.skl-indication-item p {
  font-size: 14px;
  color: var(--mid);
  line-height: 1.55;
  font-family: 'Inter', sans-serif;
  margin: 0;
}
.skl-doctor-verified {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  border: 1px solid var(--light);
  padding: 18px 20px;
  background: var(--white);
  margin-bottom: 28px;
}
.skl-dv-badge {
  background: var(--dark);
  color: var(--gold);
  font-size: 9px;
  letter-spacing: .1em;
  text-transform: uppercase;
  font-weight: 700;
  padding: 4px 7px;
  flex-shrink: 0;
  margin-top: 2px;
  font-family: 'Inter', sans-serif;
}
.skl-dv-text { font-size: 13px; color: var(--mid); line-height: 1.55; font-family: 'Inter', sans-serif; }
.skl-dv-text strong { color: var(--dark); display: block; font-size: 14px; margin-bottom: 3px; }
.skl-btn-wrap { display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px; }
.skl-btn-cart {
  background: var(--rose) !important;
  color: #fff !important;
  border: none !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  letter-spacing: .12em !important;
  text-transform: uppercase !important;
  padding: 18px !important;
  text-align: center !important;
  display: block !important;
  text-decoration: none !important;
  transition: background .2s !important;
  cursor: pointer !important;
  border-radius: 0 !important;
}
.skl-btn-cart:hover { background: #a8304c !important; color: #fff !important; }
.skl-btn-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.skl-btn-outline {
  background: transparent !important;
  color: var(--mid) !important;
  border: 1px solid var(--light) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 11px !important;
  font-weight: 500 !important;
  letter-spacing: .1em !important;
  text-transform: uppercase !important;
  padding: 13px !important;
  text-align: center !important;
  display: block !important;
  text-decoration: none !important;
  transition: all .2s !important;
  cursor: pointer !important;
}
.skl-btn-outline:hover { border-color: var(--rose) !important; color: var(--rose) !important; }
.skl-security-row {
  display: flex;
  gap: 0;
  border: 1px solid var(--light);
}
.skl-sec-item {
  flex: 1;
  padding: 12px 16px;
  text-align: center;
  border-right: 1px solid var(--light);
  font-size: 11px;
  color: var(--mid-light);
  line-height: 1.4;
  font-family: 'Inter', sans-serif;
}
.skl-sec-item:last-child { border-right: none; }
.skl-sec-item strong { display: block; font-size: 12px; color: var(--mid); margin-bottom: 2px; font-weight: 600; }
.skl-clinical-process {
  background: var(--dark);
  padding: 80px 48px;
  color: #fff;
  margin-top: 0;
}
.skl-cp-inner { max-width: 1160px; margin: 0 auto; }
.skl-cp-header {
  display: flex;
  align-items: baseline;
  gap: 24px;
  margin-bottom: 56px;
  border-bottom: 1px solid rgba(255,255,255,.1);
  padding-bottom: 28px;
}
.skl-cp-header h2 {
  font-family: 'Lora', serif;
  font-size: 28px;
  font-weight: 400;
  color: #fff;
  margin: 0;
}
.skl-cp-cap {
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 600;
  font-family: 'Inter', sans-serif;
}
.skl-cp-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; }
.skl-step-line {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
.skl-step-n {
  font-family: 'Lora', serif;
  font-size: 12px;
  font-style: italic;
  color: var(--gold);
  background: rgba(222,176,118,.12);
  border: 1px solid rgba(222,176,118,.3);
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.skl-step-bar { flex: 1; height: 1px; background: rgba(255,255,255,.1); }
.skl-cp-step:last-child .skl-step-bar { display: none; }
.skl-cp-step h3 {
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 8px;
  letter-spacing: .02em;
  font-family: 'Inter', sans-serif;
}
.skl-cp-step p {
  font-size: 13px;
  color: rgba(255,255,255,.55);
  line-height: 1.6;
  font-family: 'Inter', sans-serif;
  margin: 0;
}
/* FAQ — Diseño editorial */
.skl-faq-section { background: #fff; padding: 0; }

.skl-faq-band { background: var(--dark); padding: 56px 48px 48px; position: relative; overflow: hidden; }
.skl-faq-band::before { content: 'FAQ'; position: absolute; right: 48px; bottom: -20px; font-family: 'Lora', serif; font-size: 130px; font-style: italic; font-weight: 500; color: rgba(255,255,255,.04); line-height: 1; letter-spacing: -.02em; pointer-events: none; }
.skl-faq-band-inner { max-width: 1100px; margin: 0 auto; }
.skl-faq-eyebrow { font-size: 11px; letter-spacing: .18em; text-transform: uppercase; color: var(--gold); font-weight: 600; font-family: 'Inter', sans-serif; display: block; margin-bottom: 12px; }
.skl-faq-band h2 { font-family: 'Lora', serif; font-size: 32px; font-weight: 400; color: #fff; margin: 0 0 10px; }
.skl-faq-band-sub { font-size: 14px; color: rgba(255,255,255,.45); font-family: 'Inter', sans-serif; margin: 0; }

.skl-faq-body { padding: 0 48px 72px; background: #fff; }
.skl-faq-grid { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: var(--light); border: 1px solid var(--light); position: relative; top: -24px; }

.skl-faq-card { background: #fff; position: relative; overflow: hidden; transition: background .2s; }
.skl-faq-card.is-open { background: var(--cream); }
.skl-faq-card.is-open::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: var(--rose); }
.skl-faq-card::after { content: attr(data-num); position: absolute; right: 14px; top: 18px; font-family: 'Lora', serif; font-size: 56px; font-style: italic; font-weight: 500; color: rgba(222,176,118,.09); line-height: 1; pointer-events: none; transition: color .2s; }
.skl-faq-card.is-open::after { color: rgba(192,60,92,.06); }

.skl-faq-summary { display: flex; align-items: flex-start; gap: 14px; padding: 22px 22px; cursor: pointer; user-select: none; }
.skl-faq-num { font-family: 'Lora', serif; font-size: 12px; font-style: italic; color: var(--gold); flex-shrink: 0; margin-top: 2px; min-width: 22px; line-height: 1.4; }
.skl-faq-qtext { font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 600; color: var(--dark); flex: 1; line-height: 1.45; padding-right: 8px; }
.skl-faq-toggle { flex-shrink: 0; width: 22px; height: 22px; border: 1px solid var(--light); display: flex; align-items: center; justify-content: center; font-size: 16px; line-height: 1; color: var(--gold); transition: transform .25s, background .2s, border-color .2s; margin-top: 1px; font-family: 'Inter', sans-serif; font-weight: 300; }
.skl-faq-toggle::before { content: '+'; }
.skl-faq-card.is-open .skl-faq-toggle { background: var(--rose); border-color: var(--rose); color: #fff; transform: rotate(45deg); }

.skl-faq-answer { max-height: 0; overflow: hidden; transition: max-height .35s cubic-bezier(.4,0,.2,1); }
.skl-faq-answer-inner { padding: 0 22px 22px 50px; font-size: 14px; color: var(--mid); line-height: 1.75; font-family: 'Inter', sans-serif; }
.skl-faq-answer-inner a { color: var(--rose); text-decoration: none; }
.skl-faq-answer-inner a:hover { text-decoration: underline; }

@media (max-width: 900px) {
  .skl-product-section { grid-template-columns: 1fr; gap: 40px; padding: 36px 24px; }
  .skl-img-panel { position: static; }
  .skl-cp-steps { grid-template-columns: 1fr 1fr; }
  .skl-breadcrumb-bar { padding: 12px 24px; }
  .skl-clinical-process { padding: 56px 24px; }
}
@media (max-width: 800px) { .skl-faq-grid { grid-template-columns: 1fr; } .skl-faq-band { padding: 40px 24px 36px; } .skl-faq-body { padding: 0 24px 56px; } }
@media (max-width: 560px) {
  .skl-cp-steps { grid-template-columns: 1fr; }
  .skl-btn-row { grid-template-columns: 1fr; }
  .skl-security-row { flex-direction: column; }
  .skl-sec-item { border-right: none; border-bottom: 1px solid var(--light); }
  .skl-sec-item:last-child { border-bottom: none; }
  .skl-faq-band::before { display: none; }
}
"""

# ── HTML ─────────────────────────────────────────────────────────────────────
HTML = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<!-- TOP BAR -->
<div class="skl-top-bar">
  Envío gratis · Resultado digital en <strong>48–72 h</strong> · Prescripción médica certificada
</div>

<!-- BREADCRUMB -->
<div class="skl-breadcrumb-bar">
  <a href="https://www.dermaforyou.com/">Inicio</a><span>›</span>
  <a href="https://www.dermaforyou.com/product-category/consulta-online/">Consulta Online</a><span>›</span>
  Skinlayer Test
</div>

<!-- PRODUCTO -->
<section class="skl-product-section">

  <!-- IMAGEN -->
  <div class="skl-img-panel">
    <div class="skl-img-wrapper">
      <img src="https://www.dermaforyou.com/wp-content/uploads/2024/10/formulario-cosmetica-dermaforyou-jpg.webp"
           alt="Skinlayer Test — Formulario cosmética médica Dermaforyou"
           width="480" height="600" loading="eager">
      <div class="skl-img-badge">Prescripción<br>médica</div>
    </div>
    <div class="skl-trust-pills">
      <div class="skl-pill">🔬 Dermatóloga colegiada</div>
      <div class="skl-pill">📋 Diagnóstico personalizado</div>
      <div class="skl-pill">💊 Cosmética activa</div>
    </div>
  </div>

  <!-- CONTENIDO -->
  <div class="skl-content-panel">

    <div class="skl-content-header">
      <div class="skl-category-line">
        <div class="skl-cat-tag">Cosmética médica</div>
        <div class="skl-cat-divider"></div>
        <span class="skl-ref-code">SKL-TEST-001</span>
      </div>
      <h1 class="skl-product-title">Skinlayer Test</h1>
      <p class="skl-product-sub">Análisis y prescripción personalizada de cosmética médica elaborada por la Dra. Carmen Galera, dermatóloga especialista.</p>
    </div>

    <!-- CREDENCIALES -->
    <div class="skl-credencial-row">
      <div class="skl-cred-item"><span class="skl-cred-icon">⭐</span> Prescripción médica real</div>
      <div class="skl-cred-sep"></div>
      <div class="skl-cred-item"><span class="skl-cred-icon">🔒</span> Datos protegidos</div>
      <div class="skl-cred-sep"></div>
      <div class="skl-cred-item"><span class="skl-cred-icon">📦</span> Entrega digital</div>
    </div>

    <!-- PRECIO -->
    <div class="skl-price-section">
      <div class="skl-price-label">Precio</div>
      <div class="skl-price-number">100<sup>€</sup></div>
      <p class="skl-price-desc">
        Pago único · Resultado dermatológico completo
        <span class="skl-price-highlight">— 30 € en tu primer pedido de productos &gt; 200 €</span>
      </p>
    </div>

    <!-- INDICACIONES -->
    <div class="skl-indications-block">
      <div class="skl-block-title">Indicado para</div>
      <div class="skl-indication-item">
        <span class="skl-ind-num">01</span>
        <p>Pacientes que valoran la prescripción de cosmética médica por dermatóloga, no por un escaparate.</p>
      </div>
      <div class="skl-indication-item">
        <span class="skl-ind-num">02</span>
        <p>Quienes buscan una rutina fundamentada en activos de eficacia probada y concentración correcta.</p>
      </div>
      <div class="skl-indication-item">
        <span class="skl-ind-num">03</span>
        <p>Personas que quieren optimizar su inversión en cosmética eligiendo solo lo que su piel necesita.</p>
      </div>
    </div>

    <!-- DOCTOR VERIFIED -->
    <div class="skl-doctor-verified">
      <div class="skl-dv-badge">Médica</div>
      <div class="skl-dv-text">
        <strong>Dra. Carmen Galera — Dermatóloga</strong>
        Especialista en cosmética médica y creadora del sistema SkinLayer. Colegiada y con formación continua en dermatología clínica y estética.
      </div>
    </div>

    <!-- BOTONES -->
    <div class="skl-btn-wrap">
      <a href="?add-to-cart=8959" class="skl-btn-cart">Añadir al carrito — 100 €</a>
      <div class="skl-btn-row">
        <a href="https://www.dermaforyou.com/consulta-dermatologica-online/" class="skl-btn-outline">Consulta online</a>
        <a href="#skl-faq" class="skl-btn-outline">Preguntas frecuentes</a>
      </div>
    </div>

    <!-- SEGURIDAD -->
    <div class="skl-security-row">
      <div class="skl-sec-item"><strong>Pago seguro</strong>SSL certificado</div>
      <div class="skl-sec-item"><strong>Privacidad</strong>Datos RGPD</div>
      <div class="skl-sec-item"><strong>Soporte</strong>carmengalera@dermaforyou.com</div>
    </div>
  </div>
</section>

<!-- PROCESO CLÍNICO -->
<section class="skl-clinical-process">
  <div class="skl-cp-inner">
    <div class="skl-cp-header">
      <span class="skl-cp-cap">Protocolo</span>
      <h2>Cómo funciona el Skinlayer Test</h2>
    </div>
    <div class="skl-cp-steps">
      <div class="skl-cp-step">
        <div class="skl-step-line">
          <div class="skl-step-n">1</div>
          <div class="skl-step-bar"></div>
        </div>
        <h3>Compra el test</h3>
        <p>Acceso inmediato al formulario de evaluación dermatológica.</p>
      </div>
      <div class="skl-cp-step">
        <div class="skl-step-line">
          <div class="skl-step-n">2</div>
          <div class="skl-step-bar"></div>
        </div>
        <h3>Cumplimenta el formulario</h3>
        <p>Describe tu piel, hábitos, preocupaciones y objetivos.</p>
      </div>
      <div class="skl-cp-step">
        <div class="skl-step-line">
          <div class="skl-step-n">3</div>
          <div class="skl-step-bar"></div>
        </div>
        <h3>Análisis médico</h3>
        <p>La Dra. Carmen Galera estudia tu caso en profundidad.</p>
      </div>
      <div class="skl-cp-step">
        <div class="skl-step-line">
          <div class="skl-step-n">4</div>
          <div class="skl-step-bar"></div>
        </div>
        <h3>Tu prescripción</h3>
        <p>Recibes tu rutina personalizada con productos y pauta de uso.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="skl-faq-section" id="skl-faq">
  <div class="skl-faq-band">
    <div class="skl-faq-band-inner">
      <span class="skl-faq-eyebrow">Preguntas frecuentes</span>
      <h2>Todo lo que necesitas saber</h2>
      <p class="skl-faq-band-sub">Resolvemos las dudas más habituales sobre el Skinlayer Test.</p>
    </div>
  </div>
  <div class="skl-faq-body">
    <div class="skl-faq-grid">

      <div class="skl-faq-card" data-num="01">
        <div class="skl-faq-summary">
          <span class="skl-faq-num">01</span>
          <span class="skl-faq-qtext">¿Cuándo recibiré mi prescripción?</span>
          <div class="skl-faq-toggle"></div>
        </div>
        <div class="skl-faq-answer"><div class="skl-faq-answer-inner">El resultado digital llega en un plazo de 48 a 72 horas laborables desde que envíes el formulario completo.</div></div>
      </div>

      <div class="skl-faq-card" data-num="02">
        <div class="skl-faq-summary">
          <span class="skl-faq-num">02</span>
          <span class="skl-faq-qtext">¿El descuento de 30 € se aplica automáticamente?</span>
          <div class="skl-faq-toggle"></div>
        </div>
        <div class="skl-faq-answer"><div class="skl-faq-answer-inner">Sí. Si decides comprar los productos recomendados en la web y el pedido supera los 200 €, los 30 € de descuento se aplican automáticamente al finalizar la compra.</div></div>
      </div>

      <div class="skl-faq-card" data-num="03">
        <div class="skl-faq-summary">
          <span class="skl-faq-num">03</span>
          <span class="skl-faq-qtext">¿La prescripción es válida para cualquier tipo de piel?</span>
          <div class="skl-faq-toggle"></div>
        </div>
        <div class="skl-faq-answer"><div class="skl-faq-answer-inner">El test está diseñado para adaptarse a todos los tipos de piel: seca, grasa, mixta, sensible o con patologías específicas como rosácea o acné.</div></div>
      </div>

      <div class="skl-faq-card" data-num="04">
        <div class="skl-faq-summary">
          <span class="skl-faq-num">04</span>
          <span class="skl-faq-qtext">¿Puedo consultar dudas después de recibir la prescripción?</span>
          <div class="skl-faq-toggle"></div>
        </div>
        <div class="skl-faq-answer"><div class="skl-faq-answer-inner">Sí. Para dudas adicionales puedes escribir a <a href="mailto:carmengalera@dermaforyou.com">carmengalera@dermaforyou.com</a> o solicitar una consulta online.</div></div>
      </div>

    </div>
  </div>
</section>

<script>
(function(){
  var cards = document.querySelectorAll('.skl-faq-card');
  cards.forEach(function(card) {
    card.querySelector('.skl-faq-summary').addEventListener('click', function() {
      var answer = card.querySelector('.skl-faq-answer');
      var inner  = card.querySelector('.skl-faq-answer-inner');
      var isOpen = card.classList.contains('is-open');
      cards.forEach(function(c) {
        c.classList.remove('is-open');
        c.querySelector('.skl-faq-answer').style.maxHeight = '0';
      });
      if (!isOpen) {
        card.classList.add('is-open');
        answer.style.maxHeight = inner.scrollHeight + 'px';
      }
    });
  });
})();
</script>"""

# ── CONTENT BLOCK ─────────────────────────────────────────────────────────────
WP_CONTENT = f"""<!-- wp:html -->
<style>
{CSS}
</style>
{HTML}
<!-- /wp:html -->"""

# ── PUSH TO WORDPRESS ─────────────────────────────────────────────────────────
payload = json.dumps({
    "content": WP_CONTENT,
    "status":  "publish",
}).encode()

req = urllib.request.Request(
    f"https://www.dermaforyou.com/wp-json/wp/v2/product/8959",
    data=payload,
    headers=HEADERS,
    method="POST"
)
with urllib.request.urlopen(req, context=ctx) as r:
    resp = json.loads(r.read())
    print(f"Status: {resp['status']}")
    print(f"Link:   {resp['link']}")
    print(f"Modified: {resp['modified']}")
