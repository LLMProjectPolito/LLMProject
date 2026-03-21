import pytest
import math
from typing import List
from itertools import accumulate

def test_below_zero_single_withdrawal():
    """Test that below zero returns True when the operation is a single withdrawal."""
    assert below_zero([-100])  # A single withdrawal operation should return True

def test_below_zero_edge_case_zero_balance():
    """
    Test when all operations result in a balance of zero.
    """
    assert below_zero([0]) == False
    assert below_zero([0, 0]) == False

def test_below_zero_single_negative_operation():
    """Test case for a single negative operation."""
    operations = [1, -10, 1, 1, 1, 1, -4]
    expected_result = True
    result = below_zero(operations)
    assert result == expected_result