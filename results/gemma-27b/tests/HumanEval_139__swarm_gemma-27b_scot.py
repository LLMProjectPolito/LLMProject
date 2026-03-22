import pytest

def test_special_factorial_n_equals_1():
    assert special_factorial(1) == 1

def test_special_factorial_edge_case():
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560

def test_special_factorial_invalid_input():
    with pytest.raises(ValueError):
        special_factorial(0)
    with pytest.raises(ValueError):
        special_factorial(-1)