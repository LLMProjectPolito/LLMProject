import pytest

def test_special_factorial_positive():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560

def test_special_factorial_edge():
    assert special_factorial(0) == 1 #Handles edge case where n = 0.  While not explicitly stated, it's good to handle.

def test_special_factorial_large():
    assert special_factorial(6) == 46656000