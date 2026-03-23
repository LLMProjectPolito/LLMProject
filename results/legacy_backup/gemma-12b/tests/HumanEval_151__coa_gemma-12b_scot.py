import pytest
import math


# Focus: Boundary Values
def test_double_the_difference_empty_list():
    """Test with an empty list - boundary condition."""
    assert double_the_difference([]) == 0

def test_double_the_difference_zero():
    """Test with a list containing only zero - boundary condition."""
    assert double_the_difference([0]) == 0

def test_double_the_difference_negative_zero():
    """Test with a list containing only negative zero - boundary condition."""
    assert double_the_difference([-0]) == 0

# Focus: Type Scenarios
def test_empty_list():
    assert double_the_difference([]) == 0

def test_list_with_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 1.5]) == 1

def test_list_with_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

# Focus: Logic Branches
def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_and_non_integer_values():
    assert double_the_difference([-1, -2, 0, 1.5]) == 1

def test_mixed_odd_even_positive_and_negative():
    assert double_the_difference([1, 3, 2, -1, 0, 5]) == 1 + 9 + 0 + 25