import pytest
from Pontellini_004 import Calculator

def test_addition():
    assert Calculator.addition(10, 5) == 15
    assert Calculator.addition(-1, 1) == 0
    assert Calculator.addition(0, 0) == 0

def test_subtraction():
    assert Calculator.subtraction(10, 5) == 5
    assert Calculator.subtraction(-1, 1) == -2
    assert Calculator.subtraction(0, 0) == 0

def test_multiplication():
    assert Calculator.multiplication(10, 5) == 50
    assert Calculator.multiplication(-1, 1) == -1
    assert Calculator.multiplication(0, 5) == 0

def test_division():
    assert Calculator.division(10, 5) == 2.0
    assert Calculator.division(-10, 5) == -2.0
    assert Calculator.division(0, 5) == 0.0
    with pytest.raises(ZeroDivisionError):
        Calculator.division(10, 0)