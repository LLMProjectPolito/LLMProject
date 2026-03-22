import pytest
import math


# Focus: Order of Inputs
import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_order_of_inputs_ascending():
    """Test when a < b"""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_order_of_inputs_descending():
    """Test when a > b"""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_order_of_inputs_no_evens():
    """Test when there are no even numbers between a and b"""
    assert generate_integers(10, 14) == []

# Focus: Even Number Generation
import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_evens():
    assert generate_integers(10, 14) == []

# Focus: Empty List Condition
import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_empty_list_condition_no_even_numbers():
    """Test case where there are no even numbers between a and b."""
    assert generate_integers(1, 3) == [2]

def test_empty_list_condition_a_greater_than_b():
    """Test case where a is greater than b, resulting in an empty list."""
    assert generate_integers(10, 8) == [8, 10]

def test_empty_list_condition_range_with_no_evens():
    """Test case where the range contains no even numbers."""
    assert generate_integers(11, 13) == []