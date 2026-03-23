import pytest
import math

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_edge_negative_n():
    assert x_or_y(-5, 10, 20) == 20

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_non_prime():
    assert x_or_y(15, 8, 5) == 5