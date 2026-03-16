# ============================================================
# BOTONES.PY - Crea y organiza todos los botones de la calculadora
# Adaptado para pantallas táctiles (mínimo 70x70px por estándar de usabilidad)
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE - Colores
COLOR_NUMERO_FONDO = "#CFD8DC"    # ← Fondo botones numéricos
COLOR_NUMERO_TEXTO = "#000000"    # ← Texto botones numéricos
COLOR_OPERADOR_FONDO = "#90CAF9"  # ← Fondo botones operadores
COLOR_OPERADOR_TEXTO = "#FFFFFF"  # ← Texto botones operadores
COLOR_IGUAL_FONDO = "#4CAF50"     # ← Fondo botón "="
COLOR_IGUAL_TEXTO = "#FFFFFF"     # ← Texto botón "="
COLOR_BORRAR_FONDO = "#F48FB1"    # ← Fondo botones "C" y "←"
COLOR_BORRAR_TEXTO = "#FFFFFF"    # ← Texto botones "C" y "←"

# ✏️ CONFIGURACIÓN EDITABLE - Tamaños y espaciado (adaptado para celular)
ANCHO_BOTON = 70                  # ← Mínimo 70px para tocar fácilmente
ALTO_BOTON = 70                   # ← Mínimo 70px para tocar fácilmente
ALTO_BOTON_IGUAL = 145            # ← Altura doble del botón "="
BORDER_RADIUS_BOTON = 12          # ← Bordes redondeados para mejor UX táctil
ESPACIADO_ENTRE_BOTONES = 5       # ← Menos espacio horizontal para ahorrar espacio
ESPACIADO_ENTRE_FILAS = 5         # ← Menos espacio vertical para ahorrar espacio

# ✏️ CONFIGURACIÓN EDITABLE - Layout
FILA1_BOTONES = ["C", "←", "/", "*"]
FILA2_BOTONES = ["7", "8", "9", "-"]
FILA3_BOTONES = ["4", "5", "6", "+"]
FILA4_BOTONES = ["1", "2", "3", "="]
FILA5_BOTONES = ["ESPACIO", "0", ".", "ESPACIO"]


import flet as ft


def crear_botones(page, al_presionar):
    # --------------------------------------------------------
    # ESTILOS REUTILIZABLES - OPTIMIZADOS PARA CELULAR
    # --------------------------------------------------------
    ESTILO_NUMERO = {
        "bgcolor": COLOR_NUMERO_FONDO,
        "color": COLOR_NUMERO_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    ESTILO_OPERADOR = {
        "bgcolor": COLOR_OPERADOR_FONDO,
        "color": COLOR_OPERADOR_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    ESTILO_IGUAL = {
        "bgcolor": COLOR_IGUAL_FONDO,
        "color": COLOR_IGUAL_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON_IGUAL,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    ESTILO_BORRAR = {
        "bgcolor": COLOR_BORRAR_FONDO,
        "color": COLOR_BORRAR_TEXTO,
        "width": ANCHO_BOTON,
        "height": ALTO_BOTON,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS_BOTON))
    }
    
    # --------------------------------------------------------
    # FUNCIÓN AUXILIAR: Crea un botón reutilizable
    # --------------------------------------------------------
    def boton(texto, valor=None, estilo=None):
        if valor is None:
            valor = texto
        return ft.ElevatedButton(
            text=texto,
            on_click=lambda e: al_presionar(valor),
            **estilo
        )
    
    # --------------------------------------------------------
    # ESPACIO VACÍO PARA MANTENER ALINEACIÓN
    # --------------------------------------------------------
    ESPACIO_VACIO = ft.Container(
        width=ANCHO_BOTON,
        height=ALTO_BOTON,
        opacity=0
    )
    
    # --------------------------------------------------------
    # CREAR FILAS DE BOTONES
    # --------------------------------------------------------
    fila1_botones = []
    for btn_texto in FILA1_BOTONES:
        if btn_texto == "C" or btn_texto == "←":
            fila1_botones.append(boton(btn_texto, "C" if btn_texto == "C" else "borrar", ESTILO_BORRAR))
        elif btn_texto == "/" or btn_texto == "*":
            fila1_botones.append(boton(btn_texto, btn_texto, ESTILO_OPERADOR))
    
    fila1 = ft.Row(
        controls=fila1_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True  # ← Expandirse horizontalmente
    )
    
    fila2_botones = []
    for btn_texto in FILA2_BOTONES:
        if btn_texto in ["7", "8", "9"]:
            fila2_botones.append(boton(btn_texto, btn_texto, ESTILO_NUMERO))
        elif btn_texto == "-":
            fila2_botones.append(boton(btn_texto, btn_texto, ESTILO_OPERADOR))
    
    fila2 = ft.Row(
        controls=fila2_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True
    )
    
    fila3_botones = []
    for btn_texto in FILA3_BOTONES:
        if btn_texto in ["4", "5", "6"]:
            fila3_botones.append(boton(btn_texto, btn_texto, ESTILO_NUMERO))
        elif btn_texto == "+":
            fila3_botones.append(boton(btn_texto, btn_texto, ESTILO_OPERADOR))
    
    fila3 = ft.Row(
        controls=fila3_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True
    )
    
    fila4_botones = []
    for btn_texto in FILA4_BOTONES:
        if btn_texto in ["1", "2", "3"]:
            fila4_botones.append(boton(btn_texto, btn_texto, ESTILO_NUMERO))
        elif btn_texto == "=":
            fila4_botones.append(boton("=", "calcular", ESTILO_IGUAL))
    
    fila4 = ft.Row(
        controls=fila4_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True
    )
    
    fila5_botones = []
    for btn_texto in FILA5_BOTONES:
        if btn_texto == "ESPACIO":
            fila5_botones.append(ESPACIO_VACIO)
        elif btn_texto == "0":
            fila5_botones.append(boton("0", "0", ESTILO_NUMERO))
        elif btn_texto == ".":
            fila5_botones.append(boton(".", ".", ESTILO_NUMERO))
    
    fila5 = ft.Row(
        controls=fila5_botones,
        spacing=ESPACIADO_ENTRE_BOTONES,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True
    )
    
    # --------------------------------------------------------
    # DEVOLVER LISTA DE FILAS
    # --------------------------------------------------------
    return [fila1, fila2, fila3, fila4, fila5]