
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

# The function to be tested
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, 
    they are ordered based on their index in the original list (stable sort).
    """
    def get_digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    # Python's sort() and sorted() are stable, so we only need to provide the digit sum as the key.
    return sorted(nums, key=get_digit_sum)

### Tests (Pytest):

@pytest.mark.parametrize("input_list, expected", [
    # Basic cases
    ([], []),                                      # Empty list
    ([10], [10]),                                  # Single element
    ([1, 2, 3], [1, 2, 3]),                        # Already sorted by sum
    ([3, 2, 1], [1, 2, 3]),                        # Reverse sorted by sum
    
    # Stability tests (same sum, should maintain original relative order)
    ([10, 1, 100], [10, 1, 100]),                  # All sum to 1
    ([11, 2, 20], [11, 2, 20]),                    # All sum to 2
    ([10, 20, 1, 2], [10, 1, 20, 2]),              # Mixed sums: 1, 2, 1, 2 -> 10, 1, 20, 2
    
    # Negative numbers (sum of digits usually refers to absolute values)
    ([-1, -11, -111], [-1, -11, -111]),            # Sums: 1, 2, 3
    ([-111, -11, -1], [-1, -11, -111]),            # Sums: 3, 2, 1
    ([-10, -1], [-10, -1]),                        # Both sum to 1, maintain order
    
    # Mixed positive and negative
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # Sums: 1, 2, 1, 2, 3 -> Stable sort
    ([-12, 1, -11, 11], [1, -11, 11, -12]),        # Sums: 3, 1, 2, 2 -> 1, -11, 11, -12
    
    # Edge cases
    ([0, 0, 0], [0, 0, 0]),                        # Zeros
    ([0, 10, -10], [0, 10, -10]),                  # All sum to 1 or 0 (0:0, 10:1, -10:1)
    ([999, 1000], [1000, 999]),                    # Large sum vs small sum (27 vs 1)
    ([123456789, 9], [9, 123456789]),              # 45 vs 9
])
def test_order_by_points(input_list, expected):
    assert order_by_points(input_list) == expected

def test_order_by_points_original_unmodified():
    """Ensure the original list is not mutated."""
    original = [11, 1, 2]
    input_list = original[:]
    order_by_points(input_list)
    assert input_list == original

def test_order_by_points_large_input():
    """Test with a larger range of numbers."""
    input_list = list(range(100))
    result = order_by_points(input_list)
    
    # Verify that for any two adjacent elements, the sum of digits is non-decreasing
    def get_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    for i in range(len(result) - 1):
        assert get_sum(result[i]) <= get_sum(result[i+1])