import pytest
import math

def test_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_edge():
    assert generate_integers(10, 14) == []

def test_negative_input():
    assert generate_integers(-2, -8) == []