import pytest
import math


# Focus: Order of Inputs
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

# Focus: Even Number Generation
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_evens():
    assert generate_integers(10, 14) == []

# Focus: Empty List Condition
def test_generate_integers_empty_range():
    assert generate_integers(10, 14) == []

def test_generate_integers_empty_range_reversed():
    assert generate_integers(14, 10) == []