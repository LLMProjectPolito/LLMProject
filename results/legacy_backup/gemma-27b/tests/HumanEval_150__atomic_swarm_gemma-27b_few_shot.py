import pytest
import math

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_negative():
    assert x_or_y(-1, 1, 2) == 2

def test_x_or_y_composite():
    assert x_or_y(15, 8, 5) == 5