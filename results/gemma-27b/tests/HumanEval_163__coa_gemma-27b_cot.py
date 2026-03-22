import pytest
import math


# Focus: Order of Inputs
import pytest

def test_order_of_inputs_ascending():
    """Test when a is less than b."""
    from your_module import generate_integers  # Replace your_module
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_order_of_inputs_descending():
    """Test when a is greater than b."""
    from your_module import generate_integers  # Replace your_module
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_order_of_inputs_no_even_digits():
    """Test when there are no even digits between a and b."""
    from your_module import generate_integers  # Replace your_module
    assert generate_integers(10, 14) == []

# Focus: Even Number Generation
import pytest

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

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