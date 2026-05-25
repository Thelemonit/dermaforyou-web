# Dermaforyou — Web

Repositorio con el código frontend de [dermaforyou.com](https://www.dermaforyou.com) — clínica dermatológica de la Dra. Carmen Galera en Talavera de la Reina.

## Estructura

```
dermaforyou-web/
├── homepage/
│   ├── index.html       # Preview standalone (HTML + CSS embebido)
│   └── content.html     # Contenido de página que se sube a WordPress
├── css/
│   └── homepage.css     # Estilos del diseño premium v5
├── deploy/
│   └── deploy_v5.py     # Script de deploy a WordPress
└── docs/
    └── CAMBIOS.md       # Historial de cambios
```

## Cómo deployar

1. Configura las credenciales en `deploy/deploy_v5.py`
2. Ejecuta: `python3 deploy/deploy_v5.py`
3. Purga LiteSpeed Cache: WP Admin → LiteSpeed Cache → Toolbox → Purge All

## Stack

- **CMS**: WordPress + The7 Theme
- **CSS**: Custom Additional CSS via `custom_css` post type
- **API**: WordPress REST API + XML-RPC + WooCommerce Admin API
- **Cache**: LiteSpeed Cache

## Diseño

- Tipografías: Lora (serif, para títulos) + Inter (sans-serif, para cuerpo)
- Paleta: `--deep-rose: #c03c5c` · `--gold: #deb076` · `--cream: #FBF8F5` · `--dark: #1A1A1A`
- Secciones: Hero · Marquee · Especialidad · Triángulo Armónico® · Tratamientos · Testimonios · Método · Blog · Bio · CTA

## Nota importante

> **Nunca usar** `botox`, `bótox` ni `toxina botulínica`.  
> Sustituir siempre por `neuromodulador` / `neuromoduladores`.
