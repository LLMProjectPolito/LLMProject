import pytest

@pytest.mark.parametrize("operations, expected", [
    ([1, 2, 3], False),
    ([1, 2, -4, 5], True),
    ([-1, 2, 3], True),
    ([1, -2, 3], False),
    ([0, 0, 0], False),
    ([], False),
    ([-1, -2, -3], True),
    ([1, 1, -2], True),
])
def test_below_zero(operations, expected):
    assert below_zero(operations) == expected

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_single_deposit():
    assert below_zero([1]) == False

def test_below_zero_single_withdrawal():
    assert below_zero([-1]) == True

def test_below_zero_multiple_deposits():
    assert below_zero([1, 2, 3]) == False

def test_below_zero_multiple_withdrawals():
    assert below_zero([-1, -2, -3]) == True

def test_below_zero_mixed_operations():
    assert below_zero([1, -2, 3]) == True