from numpy.ma.core import divide, multiply, subtract

from test_calculator1 import add

def test_add_two_number():
    result = add(10, 5)
    assert result == 15

def test_sub_two_number():
    result = subtract(10, 5)
    assert result == 5

def test_mul_two_number():
    result = multiply(10, 5)
    assert result == 50

def test_div_two_number():
    result = divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    result = divide (10, 0)
    assert result == 'cannot divide by zero'