import pytest
import math

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_negative_range():
    assert generate_integers(-2, 2) == []

def test_generate_integers_invalid_input():
    assert generate_integers(-2, 8) == []