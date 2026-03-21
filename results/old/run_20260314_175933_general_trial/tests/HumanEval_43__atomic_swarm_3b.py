import pytest
import math

def test_pairs_sum_to_zero():
    # Test a positive case where two distinct elements sum to zero
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

import pytest

def test_empty_list():
    """
    Test the function with an empty list.
    """
    assert not pairs_sum_to_zero([])

import pytest

def test_pairs_sum_to_zero_empty_list():
    """
    Test that an empty list raises a ValueError.
    """
    with pytest.raises(ValueError):
        pairs_sum_to_zero([])