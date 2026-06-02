<?php
/**
 * Dermaforyou Child Theme — functions.php
 * Tema hijo de dt-the7 para dermaforyou.com
 *
 * Añadir aquí funciones PHP personalizadas a medida que se vayan necesitando.
 * El CSS personalizado va en style.css (o en archivos encolados desde aquí).
 */

// ============================================================
// 1. STYLESHEETS — Carga el CSS del padre y del hijo
// ============================================================
add_action( 'wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'parent-style',
        get_template_directory_uri() . '/style.css'
    );
    wp_enqueue_style(
        'dermaforyou-child-style',
        get_stylesheet_directory_uri() . '/style.css',
        [ 'parent-style' ],
        '1.0.1'
    );
}, 20 );


// ============================================================
// 2. HERENCIA DE THEME MODS DEL PADRE (dt-the7)
//
// WordPress guarda la configuración del Customizer (logo, colores,
// layout…) en theme_mods_{slug}. Al activar el child theme, esa clave
// cambia a theme_mods_dermaforyou-child y queda vacía.
// Este filtro hace que el child herede los mods del padre mientras
// no tenga los suyos propios guardados.
// ============================================================
add_filter( 'option_theme_mods_dermaforyou-child', function( $value ) {
    $parent_mods = get_option( 'theme_mods_dt-the7', [] );
    if ( ! empty( $parent_mods ) ) {
        if ( ! is_array( $value ) ) {
            $value = [];
        }
        // Base: mods del padre. El child puede sobrescribir encima.
        return array_merge( $parent_mods, $value );
    }
    return $value;
} );


// ============================================================
// 3. EQUIPO MÉDICO (/equipo/) — SEO para el archivo dt_team
//
// La página de equipo es un archivo de CPT `dt_team`.
// El tema The7 genera título "Equipo archivo" y H1 "Team Archive:".
// Aquí sobreescribimos título, meta descripción y schema JSON-LD.
// ============================================================

/**
 * 3a. Override del <title> via RankMath
 */
add_filter( 'rank_math/frontend/title', function( $title ) {
    if ( is_post_type_archive( 'dt_team' ) ) {
        return 'Equipo Médico | Dermaforyou — Dra. Carmen Galera';
    }
    return $title;
} );

/**
 * 3b. Override del <title> via WordPress core (fallback si RankMath no filtra)
 */
add_filter( 'pre_get_document_title', function( $title ) {
    if ( is_post_type_archive( 'dt_team' ) ) {
        return 'Equipo Médico | Dermaforyou — Dra. Carmen Galera';
    }
    return $title;
} );

/**
 * 3c. Override de la meta descripción via RankMath
 */
add_filter( 'rank_math/frontend/description', function( $desc ) {
    if ( is_post_type_archive( 'dt_team' ) ) {
        return 'Conoce al equipo médico de Dermaforyou, liderado por la Dra. Carmen Galera, dermatóloga especializada en cosmética médica y tratamientos personalizados.';
    }
    return $desc;
} );

/**
 * 3d. Schema JSON-LD para el archivo de equipo
 *     Inyectado en <head> con prioridad 99 (después de RankMath)
 */
add_action( 'wp_head', function() {
    if ( ! is_post_type_archive( 'dt_team' ) ) {
        return;
    }
    ?>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "MedicalBusiness",
      "@id": "https://www.dermaforyou.com/#organization",
      "name": "Dermaforyou",
      "url": "https://www.dermaforyou.com",
      "logo": "https://www.dermaforyou.com/wp-content/uploads/logo-dermaforyou.png",
      "description": "Clínica de dermatología y cosmética médica dirigida por la Dra. Carmen Galera, especialista en tratamientos personalizados.",
      "medicalSpecialty": "Dermatology",
      "priceRange": "€€",
      "employee": {
        "@type": "Physician",
        "name": "Dra. Carmen Galera",
        "jobTitle": "Dermatóloga",
        "medicalSpecialty": "Dermatology",
        "worksFor": { "@id": "https://www.dermaforyou.com/#organization" }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Quién es la Dra. Carmen Galera?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "La Dra. Carmen Galera es dermatóloga especializada en cosmética médica y tratamientos personalizados. Es la fundadora y directora médica de Dermaforyou, donde combina el rigor clínico con un enfoque individualizado para cada paciente."
          }
        },
        {
          "@type": "Question",
          "name": "¿Qué especialidad tiene el equipo médico de Dermaforyou?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "El equipo médico de Dermaforyou está especializado en dermatología clínica y cosmética médica, con foco en el diagnóstico cutáneo, la prescripción personalizada de cosmética activa y los tratamientos estéticos médicos."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cómo puedo consultar con la Dra. Carmen Galera?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Puedes consultar con la Dra. Carmen Galera de forma diferida enviando fotos y preguntas por escrito, o mediante videollamada de WhatsApp. Ambas modalidades están disponibles desde la tienda online de Dermaforyou."
          }
        }
      ]
    }
  ]
}
</script>
    <?php
}, 99 );
