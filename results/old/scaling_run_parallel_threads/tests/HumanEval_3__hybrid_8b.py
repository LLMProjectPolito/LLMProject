import pytest

@pytest.mark.parametrize("operations, expected", [
    ([1, 2, 3], False),
    ([1, 2, -4, 5], True),
    ([-1], True),
    ([0], False),
    ([1, -1], False),
    ([-2, 1], True),
    ([], False),
    ([-1, 2, 3], True),
    ([1, -2, 3], False),
    ([0, 0, 0], False),
    ([-1, -2, -3], True),
    ([10, 5, -15], True),
    ([100], False),
    ([100, 200, 300], False),
    ([-100, -200, -300], True),
    ([100, -50, 200, -150], True),
    ([1, 2, 3, -4, 5, -6], True)
])
def test_below_zero(operations, expected):
    assert below_zero(operations) == expected

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_single_deposit():
    assert below_zero([100]) == False

def test_below_zero_single_withdrawal():
    assert below_zero([-100]) == True

def test_below_zero_single_operation():
    assert below_zero([1]) == False
    assert below_zero([-1]) == True

def test_below_zero_multiple_deposits():
    assert below_zero([100, 200, 300]) == False

def test_below_zero_multiple_withdrawals():
    assert below_zero([-100, -200, -300]) == True

def test_below_zero_multiple_operations():
    assert below_zero([1, 2, 3, -4, 5, -6]) == True

def test_below_zero_mixed_operations():
    assert below_zero([100, -50, 200, -150]) == True