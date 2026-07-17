def add(a: object, b: object) -> object:
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

#pytest test cases
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


