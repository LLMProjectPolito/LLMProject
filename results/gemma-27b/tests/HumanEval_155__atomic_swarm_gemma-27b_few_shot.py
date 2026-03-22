import pytest
import math

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-1234567890) == (5, 5)

def test_even_odd_count_negative():
    assert even_odd_count(-12345) == (2, 3)