import requests
from deep_translator import GoogleTranslator

def buscar_recetas_por_ingrediente(ingrediente_es):
    # Traducir el ingrediente de Español a Inglés para la API
    traductor_en = GoogleTranslator(source='es', target='en')
    ingredient_en = traductor_en.translate(ingrediente_es)
    
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient_en}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["meals"]:
            # Obtener nombres originales
            nombres_en = [meal["strMeal"] for meal in data["meals"]]
            
            # Traducir la lista de resultados de Inglés a Español
            traductor_es = GoogleTranslator(source='en', target='es')
            # Traducimos todos de golpe (puedes limitar a los primeros 5 para ir más rápido)
            recetas_es = [traductor_es.translate(nombre) for nombre in nombres_en[:10]]
            
            return recetas_es
        else:
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    ingrediente = "pollo" # Ya puedes escribir en español
    recipes = buscar_recetas_por_ingrediente(ingrediente)
    
    print(f"Recetas con {ingrediente}:")
    for recipe in recipes:
        print(f"- {recipe}")