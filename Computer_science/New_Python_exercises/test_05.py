from Pontellini_005 import Employee, Manager, Developer

def test_employee():
    employee = Employee("Mario", 30000)
    assert employee.get_name() == "Mario"
    assert employee.get_salary() == 30000

    employee.set_name("Luigi")
    employee.set_salary(35000)
    assert employee.get_name() == "Luigi"
    assert employee.get_salary() == 35000

def test_manager():
    manager = Manager("Alice", 50000, 3)
    assert manager.get_name() == "Alice"
    assert manager.get_salary() == 50000
    assert manager.get_number_of_teams() == 3

    manager.set_name("Eve")
    manager.set_salary(55000)
    manager.set_number_of_teams(4)
    assert manager.get_name() == "Eve"
    assert manager.get_salary() == 55000
    assert manager.get_number_of_teams() == 4

def test_developer():
    developer = Developer("Bob", 40000, "Python")
    assert developer.get_name() == "Bob"
    assert developer.get_salary() == 40000
    assert developer.get_programming_language() == "Python"

    developer.set_name("Charlie")
    developer.set_salary(45000)
    developer.set_programming_language("Java")
    assert developer.get_name() == "Charlie"
    assert developer.get_salary() == 45000
    assert developer.get_programming_language() == "Java"