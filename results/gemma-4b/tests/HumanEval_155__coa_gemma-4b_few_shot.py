import pytest
import math


# Focus: Boundary Values
def test_even_odd_count_even():
    assert even_odd_count(12) == (1, 1)

def test_even_odd_count_odd():
    assert even_odd_count(135) == (0, 3)

def test_even_odd_count_mixed():
    assert even_odd_count(12345) == (2, 3)

# Focus: Type Scenarios
def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

# Focus: Logic Branches
def test_even_odd_count_even():
    assert even_odd_count(12) == (1, 1)

def test_even_odd_count_odd():
    assert even_odd_count(135) == (0, 3)

def test_even_odd_count_mixed():
    assert even_odd_count(12345) == (2, 3)