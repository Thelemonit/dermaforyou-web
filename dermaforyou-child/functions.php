<?php
/**
 * Dermaforyou Child Theme — functions.php
 * Tema hijo de dt-the7 para dermaforyou.com
 *
 * Añadir aquí funciones PHP personalizadas a medida que se vayan necesitando.
 * El CSS personalizado va en style.css (o en archivos encolados desde aquí).
 */

// Cargar stylesheet del tema padre y del hijo
add_action( 'wp_enqueue_scripts', function() {
    // Stylesheet del tema padre
    wp_enqueue_style(
        'parent-style',
        get_template_directory_uri() . '/style.css'
    );
    // Stylesheet del hijo (se carga después, tiene prioridad)
    wp_enqueue_style(
        'dermaforyou-child-style',
        get_stylesheet_directory_uri() . '/style.css',
        [ 'parent-style' ],
        '1.0.0'
    );
}, 20 );
