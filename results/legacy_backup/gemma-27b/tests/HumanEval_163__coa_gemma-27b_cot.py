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
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

def test_order_of_inputs_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_order_of_inputs_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_order_of_inputs_no_even_digits():
    assert generate_integers(10, 14) == []

# Focus: Even Number Generation
import pytest

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_number_odd():
    assert generate_integers(3, 3) == []

# Focus: Empty List Condition
import pytest

def test_empty_list_condition_a_greater_than_b():
    """Test when a is greater than b, resulting in an empty list."""
    from your_module import generate_integers  # Replace your_module
    assert generate_integers(10, 2) == []

def test_empty_list_condition_no_even_digits():
    """Test when there are no even digits between a and b."""
    from your_module import generate_integers  # Replace your_module
    assert generate_integers(10, 14) == []

def test_empty_list_condition_a_equals_b_odd():
    """Test when a and b are equal and odd, resulting in an empty list."""
    from your_module import generate_integers  # Replace your_module
    assert generate_integers(11, 11) == []