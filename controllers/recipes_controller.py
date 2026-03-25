from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QMessageBox
from api import buscar_recetas_por_ingrediente
from deep_translator import GoogleTranslator

# Listas de ingredientes permitidos (en español, ya que el usuario ingresa en español)
INGREDIENTES_VEGANOS = [
    "manzana", "plátano", "naranja", "arroz", "pasta", "pan", "patata", "tomate", "cebolla", "ajo",
    "zanahoria", "lechuga", "espinaca", "brócoli", "tofu", "judías", "lentejas", "garbanzos", "quinoa",
    "avena", "almendras", "cacahuetes", "coco", "aceite de oliva", "salsa de soja", "vinagre", "hierbas", "especias"
]

INGREDIENTES_VEGETARIANOS = INGREDIENTES_VEGANOS + [
    "leche", "queso", "yogur", "mantequilla", "huevos", "miel"
]

class RecipesController:
    def __init__(self, ui, window, user_options):
        self.ui = ui
        self.window = window
        self.user_options = user_options
        self.model = QStringListModel()
        self.ui.lst_Recipes.setModel(self.model)
        self.ui.btn_Recipes.clicked.connect(self.buscar_recetas)

    def buscar_recetas(self):
        """Busca recetas basadas en el ingrediente ingresado."""
        ingredient = self.ui.txt_Recipes.toPlainText().strip()
        if not ingredient:
            QMessageBox.warning(self.window, "Campo vacío", "Por favor, ingrese un ingrediente.")
            return

        # Traducir ingrediente a español para validación
        traductor_es = GoogleTranslator(source='auto', target='es')
        ingredient_es = traductor_es.translate(ingredient).lower()

        # Validar según opciones del usuario
        if not self.validar_ingrediente(ingredient_es):
            QMessageBox.warning(self.window, "Ingrediente no permitido", 
                               f"El ingrediente '{ingredient}' no está permitido según tus preferencias de dieta.")
            return

        recipes = buscar_recetas_por_ingrediente(ingredient)
        if recipes:
            self.model.setStringList(recipes)
        else:
            QMessageBox.information(self.window, "Sin resultados", f"No se encontraron recetas con el ingrediente '{ingredient}'.")
            self.model.setStringList([])

    def validar_ingrediente(self, ingredient_es):
        """Valida si el ingrediente está permitido según las opciones del usuario."""
        if self.user_options['dieta']:
            return True  # Puede buscar cualquier cosa
        elif self.user_options['vegano']:
            return ingredient_es in INGREDIENTES_VEGANOS
        elif self.user_options['vegetariano']:
            return ingredient_es in INGREDIENTES_VEGETARIANOS
        else:
            return True  # Si no marca nada, permitir todo (por defecto)