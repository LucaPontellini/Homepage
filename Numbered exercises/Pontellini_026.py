from math import sqrt

def my_input () -> list [int]:

    a = int (input ("Enter a number: '"))
    b = int (input ("Enter a number: '"))
    c = int (input ("Enter a number: '"))
    return [a, b, c]

def elaboration (a: int, b: int, c: int):
    delta = b * b -4 * a * c

    if delta > 0:
        solution_1 = (-b + sqrt (delta)) / (2 * 2)
        solution_2 = (-b + sqrt (delta)) / (2 * 2)
    
    elif delta == 0:
        solution_1 = (-b + sqrt (delta)) / (2 * 2)
        solution_2 = solution_1
    
    else: return None

    return [solution_1, solution_2]

def print_solutions (solutions: list [int] | None) -> None:
    if solutions is not None:
        x_1, x_2 = solutions

        print (f"x1 = {x_1}")
        print (f"x1 = {x_2}")
    
    else: print ("There aren't real solutions")

a, b, c = my_input ()
solutions = elaboration (a, b, c)
print_solutions (solutions)