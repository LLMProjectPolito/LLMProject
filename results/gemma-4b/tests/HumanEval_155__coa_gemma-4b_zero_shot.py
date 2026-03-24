
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math


# Focus: Boundary Values
import pytest

def test_even_odd_count_negative_even():
    assert even_odd_count(-2) == (1, 1)

def test_even_odd_count_negative_odd():
    assert even_odd_count(-1) == (0, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

# Focus: Type Scenarios
import pytest

def test_even_odd_count_even_dominant():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_odd_dominant():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_equal():
    assert even_odd_count(1234) == (2, 2)

# Focus: Logic Branches
import pytest

def test_even_odd_count_even_dominant():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_odd_dominant():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed():
    assert even_odd_count(12345) == (2, 3)