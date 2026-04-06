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
            # Obtener nombres y IDs
            meals = data["meals"][:10]  # Limitar a 10
            
            # Traducir nombres a español
            traductor_es = GoogleTranslator(source='en', target='es')
            recetas = []
            for meal in meals:
                nombre_es = traductor_es.translate(meal["strMeal"])
                recetas.append({"nombre": nombre_es, "id": meal["idMeal"]})
            
            return recetas
        else:
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def obtener_receta_completa(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["meals"]:
            meal = data["meals"][0]
            
            # Traducir nombre e instrucciones a español
            traductor_es = GoogleTranslator(source='en', target='es')
            nombre_es = traductor_es.translate(meal["strMeal"])
            instrucciones_es = traductor_es.translate(meal["strInstructions"])
            
            # Obtener ingredientes
            ingredientes = []
            for i in range(1, 21):
                ing = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")
                if ing and ing.strip():
                    full_ing = f"{measure} {ing}".strip()
                    # Traducir el ingrediente completo
                    ing_es = traductor_es.translate(full_ing)
                    ingredientes.append(ing_es)
            
            return {
                "nombre": nombre_es,
                "instrucciones": instrucciones_es,
                "ingredientes": ingredientes,
                "categoria": meal.get("strCategory", ""),
                "area": meal.get("strArea", ""),
                "imagen": meal.get("strMealThumb", "")
            }
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    ingrediente = "pollo" # Ya puedes escribir en español
    recipes = buscar_recetas_por_ingrediente(ingrediente)
    
    print(f"Recetas con {ingrediente}:")
    for recipe in recipes:
        print(f"- {recipe}")