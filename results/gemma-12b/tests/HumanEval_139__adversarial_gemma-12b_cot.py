import pytest
from your_module import special_factorial  # Replace your_module

def test_special_factorial_base_cases():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288

def test_special_factorial_large_n():
    assert special_factorial(10) == 479001600

def test_special_factorial_zero():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_type_error_float():
    with pytest.raises(TypeError):
        special_factorial(1.5)

def test_special_factorial_type_error_string():
    with pytest.raises(TypeError):
        special_factorial("abc")

def test_special_factorial_type_error_list():
    with pytest.raises(TypeError):
        special_factorial([1, 2, 3])