import pytest
import math

def test_equal_even_range():
    assert generate_integers(4, 4) == [4]

def test_equal_even_bounds():
    assert generate_integers(4, 4) == [4]