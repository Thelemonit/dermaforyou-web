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

---

## Sesión 2026-05-27 — Página Equipo + Perfiles Médicos

### Archivos añadidos
- `equipo/equipo.html` — Rediseño completo página `/equipo-dermaforyou/` (Diseño E, versión final)
- `equipo/perfiles/perfil-carmen-galera.html` — Perfil individual Dra. Carmen Galera
- `equipo/perfiles/perfil-blas-gomez.html` — Perfil individual Dr. Blas Gómez
- `equipo/perfiles/perfil-ignacio-capdevila.html` — Perfil individual Dr. Ignacio Capdevila
- `equipo/perfiles/perfil-teresa-calderon.html` — Perfil individual Dra. Teresa Calderón

### WordPress IDs
| Archivo | WP ID | URL |
|---|---|---|
| equipo.html | page 2804 | `/equipo-dermaforyou/` |
| perfil-carmen-galera.html | dt_team 5564 | `/equipo/carmen-galera-dermatologa-equipo-dermaforyou/` |
| perfil-blas-gomez.html | dt_team 5560 | `/equipo/blas-gomez-dermatologo-equipo-dermaforyou/` |
| perfil-ignacio-capdevila.html | dt_team 5565 | `/equipo/ignacio-capdevila-cirujano-plastico-equipo-dermaforyou/` |
| perfil-teresa-calderon.html | dt_team 5562 | `/equipo/teresa-calderon-duque-estetica-equipo-dermaforyou/` |

### Cambios técnicos
- Template equipo: `template-team.php` → `''` (default) — elimina Revolution Slider y grid antiguo
- CSS desplegado en Gutenberg `<!-- wp:html -->` para evitar wpautop
- Override CSS en `#main>.wf-wrap` (scoped) para no romper el footer
- Footer global: CSS escrito en `presscore_custom_css` — columnas del footer apiladas en móvil
- SEO/AEO: JSON-LD `MedicalOrganization` + `Physician` + `FAQPage`, meta description, sección FAQ visible

### Diseño equipo (equipo.html)
- Hero: foto `carmen-portada-dermaforyou-scaled.jpg`, texto izquierda (desktop) / centrado (móvil)
- Sección Dra. Carmen con badge "+20 años" visible (sin overflow:hidden que lo cortaba)
- Grid médicos: `align-items:start` — sin espacio vacío entre cards
- FAQ: grid 2 columnas, tarjetas rectangulares
- Responsive completo: 1024 / 768 / 480px
