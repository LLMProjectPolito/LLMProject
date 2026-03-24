
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

import pytest

def test_special_factorial_positive():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 12441600

def test_special_factorial_edge_case():
    assert special_factorial(0) == 1 #Handles the edge case where n is 0.  While the prompt specifies n > 0, it's good practice to handle this gracefully.

def test_special_factorial_large_number():
    assert special_factorial(7) == 1270080000