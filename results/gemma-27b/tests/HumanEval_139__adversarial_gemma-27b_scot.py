import pytest

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n == 0:
        return 1
    else:
        return factorial(n) * special_factorial(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_special_factorial_base_case_1():
    assert special_factorial(1) == 1

def test_special_factorial_base_case_2():
    assert special_factorial(2) == 2

def test_special_factorial_positive_case_3():
    assert special_factorial(3) == 12

def test_special_factorial_positive_case_4():
    assert special_factorial(4) == 288

def test_special_factorial_positive_case_5():
    assert special_factorial(5) == 34560

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_negative():
    with pytest.raises(RecursionError):
        special_factorial(-1)

def test_special_factorial_float():
    with pytest.raises(TypeError):
        special_factorial(2.5)

def test_special_factorial_string():
    with pytest.raises(TypeError):
        special_factorial("2")

def test_special_factorial_large():
    assert special_factorial(6) == 4608000