# ============================================================
# HISTORIAL.PY - Almacena y gestiona los cálculos realizados
# ============================================================
# ✏️ CONFIGURACIÓN EDITABLE (cambia estos valores para ajustar historial)
LIMITE_HISTORIAL = 20  # ← Máximo de cálculos guardados en memoria


class Historial:
    # --------------------------------------------------------
    # __init__: Constructor de la clase Historial
    # --------------------------------------------------------
    def __init__(self, limite=LIMITE_HISTORIAL):
        self.registros = []
        self.limite = limite
    
    # --------------------------------------------------------
    # agregar: Guarda un nuevo cálculo en el historial
    # --------------------------------------------------------
    def agregar(self, expresion, resultado):
        if expresion.strip() and resultado.strip():
            registro = {
                "expresion": expresion,
                "resultado": resultado
            }
            self.registros.append(registro)
            self._aplicar_limite()
            return True
        return False
    
    # --------------------------------------------------------
    # _aplicar_limite: Método PRIVADO para mantener el límite
    # --------------------------------------------------------
    def _aplicar_limite(self):
        if len(self.registros) > self.limite:
            self.registros.pop(0)
    
    # --------------------------------------------------------
    # obtener_todos: Devuelve COPIA de todos los registros
    # --------------------------------------------------------
    def obtener_todos(self):
        return self.registros.copy()
    
    # --------------------------------------------------------
    # obtener_ultimo: Devuelve el cálculo más reciente
    # --------------------------------------------------------
    def obtener_ultimo(self):
        if self.registros:
            return self.registros[-1]
        return None
    
    # --------------------------------------------------------
    # limpiar: Borra TODOS los registros
    # --------------------------------------------------------
    def limpiar(self):
        self.registros.clear()
    
    # --------------------------------------------------------
    # cantidad: Devuelve el número actual de registros
    # --------------------------------------------------------
    def cantidad(self):
        return len(self.registros)
    
    # --------------------------------------------------------
    # esta_vacio: Verifica si el historial está vacío
    # --------------------------------------------------------
    def esta_vacio(self):
        return len(self.registros) == 0