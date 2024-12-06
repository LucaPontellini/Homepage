from Pontellini_011 import (  # type: ignore
    Recipe,
    FirstCourse,
    SecondCourse,
    Dessert,
    check_ingredients,
    print_recipes,
)  # type: ignore

def test_recipe_str():
    recipe = Recipe("Generic", 10, ["Ingredient1"], "Easy")
    assert str(recipe) == "Generic - 10 min - Difficulty: Easy"

def test_first_course_attributes():
    first_course = FirstCourse(
        "Spaghetti Carbonara",
        20,
        ["Spaghetti", "Eggs", "Bacon"],
        "Medium",
        "Spaghetti",
        "Carbonara",
    )
    assert first_course.type_of_pasta == "Spaghetti"
    assert first_course.sauce == "Carbonara"

def test_second_course_attributes():
    second_course = SecondCourse(
        "Florentine Steak",
        30,
        ["Steak", "Salt", "Pepper"],
        "High",
        "Beef",
        "Medium",
    )
    assert second_course.type_of_meat == "Beef"
    assert second_course.cooking == "Medium"

def test_dessert_attributes():
    dessert = Dessert(
        "Tiramisu", 30, ["Mascarpone", "Coffee", "Ladyfingers"], "Medium", 200, "Dessert"
    )
    assert dessert.sugar == 200
    assert dessert.type_of_dessert == "Dessert"

def test_add_ingredient():
    recipe = Recipe("Generic", 10, ["Ingredient1"], "Easy")
    recipe.add_ingredient("Ingredient2")
    assert "Ingredient2" in recipe.ingredients

def test_check_ingredients():
    first_course = FirstCourse(
        "Spaghetti Carbonara",
        20,
        ["Spaghetti", "Eggs", "Bacon"],
        "Medium",
        "Spaghetti",
        "Carbonara",
    )
    second_course = SecondCourse(
        "Florentine Steak",
        30,
        ["Steak", "Salt", "Pepper"],
        "High",
        "Beef",
        "Medium",
    )
    dessert = Dessert(
        "Tiramisu", 30, ["Mascarpone", "Coffee", "Ladyfingers"], "Medium", 200, "Dessert"
    )
    recipes = [first_course, second_course, dessert]
    available_ingredients = [
        "Spaghetti",
        "Eggs",
        "Bacon",
        "Steak",
        "Salt",
        "Pepper",
        "Mascarpone",
        "Coffee",
        "Ladyfingers",
    ]
    possible_recipes = check_ingredients(recipes, available_ingredients)
    assert len(possible_recipes) == 3

def test_print_recipes(capfd):
    first_course = FirstCourse(
        "Spaghetti Carbonara",
        20,
        ["Spaghetti", "Eggs", "Bacon"],
        "Medium",
        "Spaghetti",
        "Carbonara",
    )
    second_course = SecondCourse(
        "Florentine Steak",
        30,
        ["Steak", "Salt", "Pepper"],
        "High",
        "Beef",
        "Medium",
    )
    dessert = Dessert(
        "Tiramisu", 30, ["Mascarpone", "Coffee", "Ladyfingers"], "Medium", 200, "Dessert"
    )
    recipes = [first_course, second_course, dessert]
    print_recipes(recipes)
    captured = capfd.readouterr()
    assert "Spaghetti Carbonara - 20 min - Difficulty: Medium" in captured.out
    assert "Florentine Steak - 30 min - Difficulty: High" in captured.out
    assert "Tiramisu - 30 min - Difficulty: Medium" in captured.out