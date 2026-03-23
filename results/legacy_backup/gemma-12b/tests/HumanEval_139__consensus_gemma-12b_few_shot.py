import pytest

def test_special_factorial_positive():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 12441600

def test_special_factorial_edge_case():
    assert special_factorial(0) == 1 #Handles the edge case where n is 0.

def test_special_factorial_large_number():
    assert special_factorial(7) == 609408000000