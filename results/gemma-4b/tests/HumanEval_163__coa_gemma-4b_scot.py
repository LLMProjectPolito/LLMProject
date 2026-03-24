
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest
import math


# Focus: Boundary Values
import pytest

def test_generate_integers_empty():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_value():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_range_with_even_numbers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_range_with_odd_numbers():
    assert generate_integers(1, 3) == [1, 3]

def test_generate_integers_reverse_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

# Focus: Type Scenarios
import pytest

def test_generate_integers_empty():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_multiple_even():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

# Focus: Logic Branches
import pytest

def test_generate_integers_empty():
    assert generate_integers(10, 14) == []

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]