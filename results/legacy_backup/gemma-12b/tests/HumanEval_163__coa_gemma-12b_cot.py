import pytest
import math


# Focus: Boundary Values
def test_boundary_same_even():
    assert generate_integers(2, 2) == [2]

def test_boundary_adjacent_even():
    assert generate_integers(2, 4) == [2, 4]

def test_boundary_odd_to_even():
    assert generate_integers(1, 2) == [2]

# Focus: Type Scenarios
def test_generate_integers_valid_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

# Focus: Logic Branches
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []