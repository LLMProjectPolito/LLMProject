import pytest
import math

def test_even_odd_count_basic():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12345) == (2, 3)