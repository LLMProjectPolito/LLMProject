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
def test_even_odd_count_positive():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_mixed():
    assert even_odd_count(1234) == (2, 2)

# Focus: Logic Branches
def test_even_odd_count_positive():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_mixed():
    assert even_odd_count(1234) == (2, 2)