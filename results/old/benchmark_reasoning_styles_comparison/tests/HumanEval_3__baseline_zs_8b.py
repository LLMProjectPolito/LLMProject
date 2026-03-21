import pytest

def test_below_zero_no_withdrawal():
    assert below_zero([1, 2, 3]) == False

def test_below_zero_with_withdrawal():
    assert below_zero([1, 2, -4, 5]) == True

def test_below_zero_only_deposits():
    assert below_zero([100, 200, 300]) == False

def test_below_zero_only_withdrawals():
    assert below_zero([-100, -200, -300]) == True

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_single_deposit():
    assert below_zero([100]) == False

def test_below_zero_single_withdrawal():
    assert below_zero([-100]) == True

def test_below_zero_multiple_withdrawals():
    assert below_zero([100, -200, 300, -400]) == True

def test_below_zero_large_numbers():
    assert below_zero([1000000, -2000000, 3000000, -4000000]) == True

def test_below_zero_zero_balance():
    assert below_zero([0, 0, 0]) == False