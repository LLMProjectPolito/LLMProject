
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

import pytest

# The function order_by_points is provided by the environment.
# We are writing the test suite to detect bugs in its implementation.

@pytest.mark.parametrize("input_list, expected", [
    # Basic cases
    ([], []),
    ([42], [42]),
    
    # The specific example from the docstring
    # Logic: -1 (sum -1), -11 (sum 0), 1 (sum 1), -12 (sum 1), 11 (sum 2)
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    
    # Stability tests (Positive)
    # 10 (sum 1), 1 (sum 1), 100 (sum 1) -> should maintain order
    ([10, 1, 100], [10, 1, 100]),
    ([1, 10, 100], [1, 10, 100]),
    
    # Stability tests (Negative)
    # -10 (sum -1+0=-1), -1 (sum -1) -> should maintain order
    ([-10, -1], [-10, -1]),
    ([-1, -10], [-1, -10]),
    
    # Mixed stability
    # 1 (sum 1), -12 (sum -1+2=1) -> should maintain order
    ([1, -12], [1, -12]),
    ([-12, 1], [-12, 1]),
    
    # General sorting order
    # 20 (sum 2), 10 (sum 1), 0 (sum 0) -> [0, 10, 20]
    ([20, 10, 0], [0, 10, 20]),
    
    # Negative number sorting
    # -1 (sum -1), -11 (sum 0), -2 (sum -2) -> [-2, -1, -11]
    ([-1, -11, -2], [-2, -1, -11]),
    
    # Large numbers
    # 99 (sum 18), -99 (sum -9+9=0), 100 (sum 1) -> [-99, 100, 99]
    ([99, -99, 100], [-99, 100, 99]),
    
    # Zeros and mixed
    # 0 (sum 0), -11 (sum 0), 11 (sum 2) -> [0, -11, 11]
    ([0, -11, 11], [0, -11, 11]),
])
def test_order_by_points(input_list, expected):
    """
    Tests the order_by_points function against various scenarios including
    the specific digit-sum logic for negative numbers and stability requirements.
    """
    assert order_by_points(input_list) == expected

def test_order_by_points_idempotency():
    """
    Verify that sorting an already sorted list doesn't change it.
    """
    nums = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == nums

def test_order_by_points_large_input():
    """
    Verify the function handles a larger list of integers.
    """
    # All these have sum 1: 1, 10, 100, 1000, -12, -120, -1200
    # -12: -1+2=1; -120: -1+2+0=1; -1200: -1+2+0+0=1
    nums = [1, 10, 100, 1000, -12, -120, -1200]
    # Since all have sum 1, the original order must be preserved.
    assert order_by_points(nums) == nums