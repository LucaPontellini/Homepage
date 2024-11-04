from Pontellini_010-1 import Fraction  # type: ignore

def test_addition():
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 4)
    f3 = f1 + f2
    assert str(f3) == "Fraction(5, 4)"

def test_subtraction():
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 4)
    f4 = f1 - f2
    assert str(f4) == "Fraction(1, 4)"

def test_multiplication():
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 4)
    f5 = f1 * f2
    assert str(f5) == "Fraction(6, 16)"

def test_representation():
    f1 = Fraction(3, 4)
    assert str(f1) == "Fraction(3, 4)"