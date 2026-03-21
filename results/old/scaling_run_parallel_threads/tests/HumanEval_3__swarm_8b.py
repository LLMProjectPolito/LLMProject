import pytest
import math

def test_below_zero_zero_balance():
    """Test if the function handles an edge case where operations result in zero balance."""
    operations = [0, -0, 0, 0]
    assert below_zero(operations) == False

def test_all_withdrawals():
    """Edge case: all operations are withdrawals"""
    assert below_zero([-5, -10, -15])  # Expected output: True

def test_initial_balance_below_zero():
    """
    Test case for an edge condition where the initial balance is below zero.
    This case should return True immediately.
    """
    operations = [-1]
    assert below_zero(operations)