import pytest
import math

def test_intersperse_negative_delimeter():
    """ Test that interspersing with a negative delimeter still works"""
    result = intersperse([1, 2, 3], -4)
    expected = [1, -4, 2, -4, 3]
    assert result == expected

def test_intersperse_single_element_list():
    """ Test if intersperse function works as expected with a list containing only one element """
    assert intersperse([1], 4) == [1]
    assert intersperse([1], 0) == [1]
    assert intersperse([1], -4) == [1]

def test_intersperse_delimeter_zero():
    """ Test edge case where the delimiter is zero and negative values are present. """
    numbers = [-10, -5, 0, 5, 10]
    delimeter = 0
    result = intersperse(numbers, delimeter)
    expected_result = [-10, 0, -5, 0, 0, 0, 5, 0, 10]
    assert result == expected_result