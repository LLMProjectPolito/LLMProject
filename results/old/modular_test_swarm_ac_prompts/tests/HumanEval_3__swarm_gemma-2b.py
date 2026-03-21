import pytest
import math

def test_below_zero_debit_equals_credits():
    """ Test if the balance falls below zero when debits equal credits """
    assert below_zero([-1, 1, -1, 1]) is True

def test_below_zero_edge_case():
    """Test edge case where account balance just touches zero"""
    # Input: List of operations where the balance briefly touches zero
    operations = [1, -1]
    
    # Expected result: Function should return True if balance falls below zero
    assert below_zero(operations)

def test_balance_below_zero_with_single_operation():
    """Test that a single negative operation results in a balance below zero."""
    assert below_zero([-10]) == True