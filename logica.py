# ============================================================
# LOGICA.PY - Motor matemático de la calculadora
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE (cambia estos valores para ajustar comportamiento)
MAX_LONGITUD_EXPRESION = 50  # ← Máximo de caracteres permitidos en la expresión


class Calculadora:
    # --------------------------------------------------------
    # __init__: Constructor de la clase Calculadora
    # --------------------------------------------------------
    def __init__(self):
        self.expresion = ""
        self.resultado = ""
    
    # --------------------------------------------------------
    # agregar: Añade un valor a la expresión actual
    # --------------------------------------------------------
    def agregar(self, valor):
        valor_str = str(valor)
        if len(self.expresion) < MAX_LONGITUD_EXPRESION:
            self.expresion += valor_str
        return self.expresion
    
    # --------------------------------------------------------
    # calcular: Evalúa la expresión matemática
    # --------------------------------------------------------
    def calcular(self):
        try:
            resultado_numerico = eval(self.expresion)
            self.resultado = str(resultado_numerico)
            self.expresion = self.resultado
            return self.resultado
        except ZeroDivisionError:
            self.resultado = "Error: Div/0"
            self.expresion = ""
            return self.resultado
        except:
            self.resultado = "Error"
            self.expresion = ""
            return self.resultado
    
    # --------------------------------------------------------
    # borrar_ultimo: Elimina el último carácter
    # --------------------------------------------------------
    def borrar_ultimo(self):
        if self.expresion:
            self.expresion = self.expresion[:-1]
        return self.expresion
    
    # --------------------------------------------------------
    # limpiar: Borra TODO
    # --------------------------------------------------------
    def limpiar(self):
        self.expresion = ""
        self.resultado = ""
        return self.expresion
    
    # --------------------------------------------------------
    # obtener_expresion: Devuelve la expresión actual
    # --------------------------------------------------------
    def obtener_expresion(self):
        return self.expresion
    
    # --------------------------------------------------------
    # obtener_resultado: Devuelve el resultado actual
    # --------------------------------------------------------
    def obtener_resultado(self):
        return self.resultado