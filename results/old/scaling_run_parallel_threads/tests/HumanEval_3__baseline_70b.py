import pytest

def test_below_zero_no_negative_balance():
    assert below_zero([1, 2, 3]) == False

def test_below_zero_negative_balance():
    assert below_zero([1, 2, -4, 5]) == True

def test_below_zero_initial_negative_balance():
    assert below_zero([-1, 2, 3]) == True

def test_below_zero_multiple_negative_balances():
    assert below_zero([1, -2, 3, -4, 5]) == True

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_single_positive_operation():
    assert below_zero([1]) == False

def test_below_zero_single_negative_operation():
    assert below_zero([-1]) == True

def test_below_zero_multiple_positive_operations():
    assert below_zero([1, 2, 3, 4, 5]) == False

def test_below_zero_multiple_negative_operations():
    assert below_zero([-1, -2, -3, -4, -5]) == True