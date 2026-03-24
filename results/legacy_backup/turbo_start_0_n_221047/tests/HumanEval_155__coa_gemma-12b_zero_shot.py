import pytest
import math


# Focus: Boundary Values
def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd():
    assert even_odd_count(1) == (0, 1)

# Focus: Type Scenarios
def test_even_odd_count_positive_integer():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_negative_integer():
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_single_digit():
    assert even_odd_count(2) == (1, 0)

# Focus: Logic Branches
def test_even_odd_count_positive_number():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative_number():
    assert even_odd_count(-2468) == (4, 0)

def test_even_odd_count_mixed_number():
    assert even_odd_count(1357924680) == (4, 6)