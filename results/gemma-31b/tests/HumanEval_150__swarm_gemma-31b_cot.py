
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

@pytest.mark.parametrize("x, if_prime, if_not_prime, expected", [
    (1, "prime", "not prime", "not prime"),  # 1 is not prime, should return if_not_prime
    (1, 100, 200, 200),                      # 1 is not prime, should return if_not_prime
    (2, "prime", "not_prime", "prime"),      # 2 is the smallest prime, should return if_prime
])
def test_x_or_y(x, if_prime, if_not_prime, expected):
    assert x_or_y(x, if_prime, if_not_prime) == expected