# ============================================================
# MAIN.PY - Punto de entrada de la aplicación
# Adaptado para pantalla completa en celular
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE - Dimensiones y estilo general
TITULO_APP = "Calculadora Flet"   # ← Título que aparece en la barra de la ventana
COLOR_FONDO_APP = "#ECEFF1"       # ← Color de fondo general de la app
PADDING_GENERAL = 0               # ← Sin padding en celular (usa toda la pantalla)
ESPACIO_SUPERIOR = 0              # ← Sin espacio superior en modo móvil
ESPACIO_ENTRE_PANTALLA_BOTONES = 0  # ← Sin espacio entre pantalla y botones


import flet as ft
from logica import Calculadora
from pantalla import crear_pantalla
from botones import crear_botones
from historial import Historial


def main(page: ft.Page):
    # --------------------------------------------------------
    # CONFIGURAR PROPIEDADES DE LA PÁGINA PARA CELULAR
    # --------------------------------------------------------
    page.title = TITULO_APP
    page.window_width = None      # ← None = pantalla completa en celular
    page.window_height = None     # ← None = pantalla completa en celular
    page.window_resizable = True  # ← Permitir redimensionamiento (celular lo maneja)
    page.padding = PADDING_GENERAL
    page.bgcolor = COLOR_FONDO_APP
    page.scroll = ft.ScrollMode.AUTO  # ← Scroll automático si el contenido no cabe
    
    # --------------------------------------------------------
    # CREAR INSTANCIAS DE LOS MÓDULOS
    # --------------------------------------------------------
    calc = Calculadora()
    historial = Historial()
    
    # --------------------------------------------------------
    # CREAR PANTALLA Y OBTENER REFERENCIAS
    # --------------------------------------------------------
    contenedor_pantalla, txt_expresion, txt_resultado = crear_pantalla(page)
    
    # --------------------------------------------------------
    # DEFINIR CALLBACK: Función que responde a presionar botones
    # --------------------------------------------------------
    def al_presionar(valor):
        if valor == "calcular":
            res = calc.calcular()
            txt_expresion.value = ""
            txt_resultado.value = res
            
            if not res.startswith("Error"):
                expr_guardar = txt_resultado.value if txt_expresion.value == "" else calc.obtener_expresion()
                historial.agregar(expr_guardar, res)
        
        elif valor == "borrar":
            calc.borrar_ultimo()
            txt_expresion.value = calc.obtener_expresion()
            if not txt_expresion.value:
                txt_resultado.value = "0"
        
        elif valor == "C":
            calc.limpiar()
            txt_expresion.value = ""
            txt_resultado.value = "0"
        
        else:
            calc.agregar(valor)
            txt_expresion.value = calc.obtener_expresion()
            txt_resultado.value = "0" if calc.obtener_expresion() == "" else ""
        
        page.update()
    
    # --------------------------------------------------------
    # CREAR BOTONES PASANDO EL CALLBACK
    # --------------------------------------------------------
    filas_botones = crear_botones(page, al_presionar)
    
    # --------------------------------------------------------
    # ENSAMBLAR LAYOUT COMPLETO - RESPONSIVE PARA CELULAR
    # --------------------------------------------------------
    layout = ft.Column(
        controls=[
            ft.Container(height=ESPACIO_SUPERIOR),
            contenedor_pantalla,
            ft.Container(height=ESPACIO_ENTRE_PANTALLA_BOTONES),
        ] + filas_botones,
        spacing=5,  # ← Menos espacio entre filas para ahorrar espacio
        alignment=ft.MainAxisAlignment.START,
        expand=True  # ← Expandirse para ocupar toda la pantalla disponible
    )
    
    # --------------------------------------------------------
    # AGREGAR TODO A LA PÁGINA
    # --------------------------------------------------------
    page.add(layout)
    
    # --------------------------------------------------------
    # ESTADO INICIAL
    # --------------------------------------------------------
    txt_resultado.value = "0"
    page.update()


# --------------------------------------------------------
# PUNTO DE ENTRADA
# --------------------------------------------------------
if __name__ == "__main__":
    ft.app(target=main)