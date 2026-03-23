import pytest
import math

def test_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_algebra_negative_numbers():
    assert do_algebra(['-', '+'], [10, -5, 2]) == 7

def test_do_algebra_invalid_operator():
    with pytest.raises(TypeError):
        do_algebra(['+', 'a', '-'], [2, 3, 4])