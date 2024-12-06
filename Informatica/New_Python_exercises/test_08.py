from Pontellini_008 import Appetizer, FirstCourse, MainCourse, Dessert, calculate_bill, print_menu  # type: ignore

def test_appetizer():
    appetizer = Appetizer(
        "Bruschetta", 5.0, ["Bread", "Tomato", "Basil"], "Small"
    )
    assert appetizer.get_name() == "Bruschetta"
    assert appetizer.get_price() == 5.0
    assert appetizer.get_ingredients() == ["Bread", "Tomato", "Basil"]
    assert appetizer.get_portion() == "Small"

    appetizer.order()
    assert not appetizer.is_available()

    appetizer.make_available()
    assert appetizer.is_available()

def test_first_course():
    first_course = FirstCourse("Spaghetti Carbonara", 12.0, "Spaghetti", "Carbonara")
    assert first_course.get_name() == "Spaghetti Carbonara"
    assert first_course.get_price() == 12.0
    assert first_course.get_pasta_type() == "Spaghetti"
    assert first_course.get_sauce() == "Carbonara"

    first_course.order()
    assert not first_course.is_available()

    first_course.make_available()
    assert first_course.is_available()

def test_main_course():
    main_course = MainCourse("Florentine Steak", 25.0, "Beef", "Medium")
    assert main_course.get_name() == "Florentine Steak"
    assert main_course.get_price() == 25.0
    assert main_course.get_meat_type() == "Beef"
    assert main_course.get_cooking_level() == "Medium"

    main_course.order()
    assert not main_course.is_available()

    main_course.make_available()
    assert main_course.is_available()

def test_dessert():
    dessert = Dessert("Tiramisu", 6.0, "Tiramisu", 450)
    assert dessert.get_name() == "Tiramisu"
    assert dessert.get_price() == 6.0
    assert dessert.get_dessert_type() == "Tiramisu"
    assert dessert.get_calories() == 450

    dessert.order()
    assert not dessert.is_available()

    dessert.make_available()
    assert dessert.is_available()

def test_calculate_bill():
    appetizer = Appetizer(
        "Bruschetta", 5.0, ["Bread", "Tomato", "Basil"], "Small"
    )
    first_course = FirstCourse("Spaghetti Carbonara", 12.0, "Spaghetti", "Carbonara")
    main_course = MainCourse("Florentine Steak", 25.0, "Beef", "Medium")
    dessert = Dessert("Tiramisu", 6.0, "Tiramisu", 450)

    ordered_dishes = [appetizer, first_course, main_course, dessert]
    total_bill = calculate_bill(ordered_dishes)
    assert total_bill == 48.0

def test_print_menu(capfd):
    appetizer = Appetizer(
        "Bruschetta", 5.0, ["Bread", "Tomato", "Basil"], "Small"
    )
    first_course = FirstCourse("Spaghetti Carbonara", 12.0, "Spaghetti", "Carbonara")
    main_course = MainCourse("Florentine Steak", 25.0, "Beef", "Medium")
    dessert = Dessert("Tiramisu", 6.0, "Tiramisu", 450)

    dishes = [appetizer, first_course, main_course, dessert]
    print_menu(dishes)
    captured = capfd.readouterr()
    assert "Bruschetta - 5.0€ - Available" in captured.out
    assert "Spaghetti Carbonara - 12.0€ - Available" in captured.out
    assert "Florentine Steak - 25.0€ - Available" in captured.out
    assert "Tiramisu - 6.0€ - Available" in captured.out