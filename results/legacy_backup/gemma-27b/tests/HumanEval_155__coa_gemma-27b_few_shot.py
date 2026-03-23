import pytest
import math


# Focus: Boundary Values
def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

# Focus: Negative Numbers
def test_negative_numbers():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-135) == (0, 3)

def test_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_large_negative():
    assert even_odd_count(-1234567890) == (5, 5)

# Focus: Digit Composition
def test_even_odd_count_positive():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-123456) == (3, 3)

def test_even_odd_count_mixed():
    assert even_odd_count(123) == (1, 2)