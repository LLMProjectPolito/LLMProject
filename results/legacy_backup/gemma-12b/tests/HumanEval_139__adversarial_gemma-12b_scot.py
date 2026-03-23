import pytest
from your_module import special_factorial  # Replace your_module

def test_base_case():
    assert special_factorial(1) == 1

def test_small_values():
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288

def test_larger_values():
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 3628800

def test_zero_input():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_float_input():
    with pytest.raises(TypeError):
        special_factorial(2.5)

def test_string_input():
    with pytest.raises(TypeError):
        special_factorial("abc")