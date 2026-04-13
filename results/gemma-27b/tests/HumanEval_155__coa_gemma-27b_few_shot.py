
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

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_negative_single_digit():
    assert even_odd_count(-2) == (1, 0)

def test_even_odd_count_positive_single_digit():
    assert even_odd_count(5) == (0, 1)

def test_even_odd_count_max_int():
    assert even_odd_count(2147483647) == (5, 4)

def test_even_odd_count_min_int():
    assert even_odd_count(-2147483648) == (1, 9)

# Focus: Negative Numbers
import pytest

def test_negative_number_even_odd():
    assert even_odd_count(-12) == (1, 1)

def test_negative_number_all_odd():
    assert even_odd_count(-135) == (0, 3)

def test_negative_number_all_even():
    assert even_odd_count(-246) == (3, 0)

# Focus: Digit Composition
import pytest

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(246) == (3, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(135) == (0, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)