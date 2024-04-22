from django.shortcuts import render
from .models import Recipe
from rec_app.settings import BASE_DIR

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes, 'BASE_DIR': BASE_DIR})

def add_recipe(request):
    if request.method == 'POST':
        recipe = Recipe()
        recipe.title = request.POST.get("recipe_title", False)
        recipe.description = request.POST.get("recipe_description", False)
        recipe.ingredients = request.POST.get("recipe_ingredients", False)
        recipe.instructions = request.POST.get("recipe_instructions", False)
        recipe.prep_time = request.POST.get("recipe_prep_time", False)
        recipe.cook_time = request.POST.get("recipe_cook_time", False)
        recipe.servings = request.POST.get("recipe_servings", False)
        recipe.save()
    
    return render(request, 'add_recipe.html')

