import pytest
import math

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -73, 14, -15]) == 1