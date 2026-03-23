import pytest

def test_special_factorial_positive():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 46656000

def test_special_factorial_edge_cases():
    assert special_factorial(0) == 1 #Handles edge case where n = 0.  Although not specified in prompt, good practice.
    assert special_factorial(1) == 1

def test_special_factorial_larger_number():
    assert special_factorial(7) == 6402373705728000