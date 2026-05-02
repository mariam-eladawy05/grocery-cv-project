import requests

API_KEY = "DvjX8jxdROK4x0qPrFpmmkUuknvwMiiDcqTzFXG3"

def get_nutrition(food_name):
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    
    params = {
        "query": food_name,
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        food = data["foods"][0]

        nutrients = food["foodNutrients"]

        nutrition_data = {
            "calories": None,
            "protein": None,
            "fat": None,
            "carbs": None
        }

        for n in nutrients:
            name = n["nutrientName"]

            if name == "Energy":
                nutrition_data["calories"] = n["value"]
            elif name == "Protein":
                nutrition_data["protein"] = n["value"]
            elif name == "Total lipid (fat)":
                nutrition_data["fat"] = n["value"]
            elif name == "Carbohydrate, by difference":
                nutrition_data["carbs"] = n["value"]

        return nutrition_data

    except:
        return "Food not found"