import json
from flask import Flask, render_template

app = Flask(__name__)

def get_all_recipes():
    with open('/templates/recipes.json', 'r') as f:
        recipes = json.load(f)
    return recipes

def get_recipe_by_id(recipe_id):
    recipes = get_all_recipes()
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            return recipe
    return None

@app.route('/recipe.html/<int:id>')
def recipe(id):
    recipe = get_recipe_by_id(id)
    if recipe:
        return render_template('/templates/recipe.html', recipe=recipe)
    else:
        return "Recipe not found", 404

@app.route('/recipes')
def recipes():
    recipes = get_all_recipes()
    return render_template('/templates/recipes.html', recipes=recipes)

if __name__ == '_main_':
    app.run(debug=True)