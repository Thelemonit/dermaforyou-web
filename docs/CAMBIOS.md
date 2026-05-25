# Historial de cambios — Dermaforyou Web

## v5 — Mayo 2026 (actual)

### Homepage premium rediseñada
- Diseño premium completo con 10 secciones
- Hero con imagen, estadísticas flotantes y animaciones
- Marquee de confianza (certificaciones, años de experiencia)
- Sección especialidad (flacidez facial)
- Técnica Triángulo Armónico® con 3 pasos
- Grid de 6 tratamientos (Flacidez, Neuromoduladores, Ácido Hialurónico, Láser CO2/IPL, Hilos Tensores, Acné)
- Testimonios reales
- Método Skin Layer (4 fases)
- Blog dinámico (carga automática últimos posts vía WP REST API)
- Bio Dra. Carmen Galera
- CTA final con gradiente

### Correcciones técnicas
- **Footer oscuro** (#1A1A1A) con texto en blanco y links en dorado al hover
- **Tratamiento de tarjetas** con `<div>` + `<a class="treat-card-link">` overlay para evitar que wpautop rompa el grid
- **Contenido enviado como `raw`** para bypassar el filtro wpautop de WordPress
- **CSS creado vía XML-RPC** (el tipo `custom_css` no está expuesto en la REST API)
- **theme_mods persistidos como dict** (no como JSON string) via WC Admin API
- **nav_menu_locations** fijado a `{primary: 5674, mobile: 5674}` (Menú Principal v2)

### Stack técnico
- WordPress + The7 Theme (dt-the7)
- WooCommerce Admin API para theme_mods
- LiteSpeed Cache (purgar después de cada deploy)
- Custom CSS via `custom_css` post type
- JavaScript vanilla para blog dinámico (fetch + IntersectionObserver)

---

## Palabras prohibidas
- ❌ `botox` / `bótox` / `toxina botulínica`
- ✅ Usar siempre: `neuromodulador` / `neuromoduladores`
