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
    assert even_odd_count(2147483647) == (5, 5)

def test_even_odd_count_min_int():
    assert even_odd_count(-2147483648) == (5, 5)

# Focus: Negative Numbers
import pytest

def test_negative_number_with_even_and_odd():
    assert even_odd_count(-12) == (1, 1)

def test_negative_number_all_odd():
    assert even_odd_count(-135) == (0, 3)

def test_negative_number_all_even():
    assert even_odd_count(-246) == (3, 0)

# Focus: Digit Composition
import pytest

def test_even_odd_count_positive():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-123456) == (3, 3)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)