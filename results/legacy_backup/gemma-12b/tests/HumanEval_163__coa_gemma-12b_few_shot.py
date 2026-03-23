import pytest
import math


# Focus: Boundary Values
def test_generate_integers_boundary_a_equals_b_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_boundary_a_equals_b_odd():
    assert generate_integers(5, 5) == []

def test_generate_integers_boundary_a_one_less_than_even():
    assert generate_integers(1, 2) == [2]

# Focus: Logic Branches
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

# Focus: Type Scenarios
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []