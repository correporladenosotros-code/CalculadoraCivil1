# ============================================================
# PANTALLA.PY - Crea y gestiona la pantalla de la calculadora
# Adaptado para pantallas pequeñas de celular
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE (cambia estos valores para ajustar la pantalla)
COLOR_FONDO_PANTALLA = "#81C4F1"        # ← Color de fondo de la pantalla
COLOR_TEXTO_EXPRESION = "#455A64"       # ← Color del texto de la expresión
COLOR_TEXTO_RESULTADO = "#000000"       # ← Color del texto del resultado
TAMANO_FUENTE_EXPRESION = 32            # ← Tamaño reducido para pantallas pequeñas
TAMANO_FUENTE_RESULTADO = 50            # ← Tamaño grande para legibilidad
ALTURA_PANTALLA = None                  # ← None = altura automática (responsive)
PADDING_INTERNO_PANTALLA = 15           # ← Menos padding para ahorrar espacio
BORDER_RADIUS_PANTALLA = 16             # ← Bordes menos redondeados (más espacio)
ESPACIO_ENTRE_TEXTOS = 3                # ← Menos espacio entre expresión y resultado


import flet as ft


def crear_pantalla(page):
    # --------------------------------------------------------
    # CREAR TEXTO PARA LA EXPRESIÓN
    # --------------------------------------------------------
    expresion = ft.Text(
        value="",
        size=TAMANO_FUENTE_EXPRESION,
        color=COLOR_TEXTO_EXPRESION,
        text_align=ft.TextAlign.RIGHT,
        expand=True,
        max_lines=1,
        overflow=ft.TextOverflow.FADE
    )
    
    # --------------------------------------------------------
    # CREAR TEXTO PARA EL RESULTADO
    # --------------------------------------------------------
    resultado = ft.Text(
        value="0",
        size=TAMANO_FUENTE_RESULTADO,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TEXTO_RESULTADO,
        text_align=ft.TextAlign.RIGHT,
        expand=True,
        max_lines=1,
        overflow=ft.TextOverflow.FADE
    )
    
    # --------------------------------------------------------
    # CREAR CONTENEDOR DE LA PANTALLA - RESPONSIVE
    # --------------------------------------------------------
    contenedor = ft.Container(
        content=ft.Column(
            controls=[expresion, resultado],
            spacing=ESPACIO_ENTRE_TEXTOS,
            alignment=ft.MainAxisAlignment.END,
            expand=True
        ),
        bgcolor=COLOR_FONDO_PANTALLA,
        border_radius=BORDER_RADIUS_PANTALLA,
        padding=PADDING_INTERNO_PANTALLA,
        height=ALTURA_PANTALLA,  # ← None = altura automática según contenido
        alignment=ft.alignment.center_right,
        expand=True  # ← Expandirse para ocupar espacio disponible
    )
    
    # --------------------------------------------------------
    # DEVOLVER REFERENCIAS
    # --------------------------------------------------------
    return contenedor, expresion, resultado