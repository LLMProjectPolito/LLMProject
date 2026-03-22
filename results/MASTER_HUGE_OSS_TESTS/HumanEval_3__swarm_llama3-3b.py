import pytest
import math
from typing import List

def test_below_zero_edge_cases():
    """Test cases to check if withdrawal operations bring balance below zero"""
    # Single withdrawal operation
    operations = [-1]
    assert below_zero(operations)

    # Negative operation early in the sequence
    operations = [-10, 1, 2, 3]
    assert below_zero(operations)

    # First operation is a negative withdrawal
    operations = [-1, 2, 3]
    assert below_zero(operations)

def test_below_zero_no_negative_balance():
    """Test case to check if no withdrawal operations bring balance below zero"""
    operations = [1, 2, 3]
    assert not below_zero(operations)

def test_below_zero_empty_operations():
    """Test case to check if empty operations list brings balance below zero"""
    operations = []
    assert not below_zero(operations)