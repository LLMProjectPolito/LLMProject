
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

@pytest.mark.parametrize("nums, expected", [
    # Edge Case: Empty list
    ([], []),
    
    # Edge Case: Single element
    ([5], [5]),
    ([0], [0]),
    ([-7], [-7]),
    
    # Basic Case: Already sorted by digit sum
    ([1, 2, 3], [1, 2, 3]),
    ([10, 11, 12], [10, 11, 12]),
    
    # Basic Case: Reverse sorted by digit sum
    ([3, 2, 1], [1, 2, 3]),
    ([12, 11, 10], [10, 11, 12]),
    
    # Stability: Same digit sum, should maintain original order
    ([10, 1, 100], [10, 1, 100]),  # All sums are 1
    ([11, 2, 20, 200], [11, 2, 20, 200]),  # All sums are 2
    ([123, 321, 213], [123, 321, 213]),  # All sums are 6
    
    # Negative Numbers: Sum of digits of absolute value
    # -1 (sum 1, idx 0), -11 (sum 2, idx 1), -2 (sum 2, idx 2)
    ([-1, -11, -2], [-1, -11, -2]),
    # -20 (sum 2, idx 0), -11 (sum 2, idx 1), -1 (sum 1, idx 2)
    ([-20, -11, -1], [-1, -20, -11]),
    
    # Mixed Positive and Negative
    # 1 (sum 1, idx 0), 11 (sum 2, idx 1), -1 (sum 1, idx 2), -11 (sum 2, idx 3), -12 (sum 3, idx 4)
    # Expected order by (sum, index): (1,0), (1,2), (2,1), (2,3), (3,4)
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]),
    
    # Zeros and Large Numbers
    ([0, 10, 1], [0, 10, 1]),
    ([1000000, 1], [1000000, 1]),
    ([999, 18, 9], [18, 9, 999]), # Sums: 27, 9, 9 -> [18, 9, 999] (Wait, 18 is idx 1, 9 is idx 2. So [18, 9, 999] is wrong. 
                                  # Sums: 18 (9), 9 (9), 999 (27). 
                                  # Indices: 18 is idx 1, 9 is idx 2. 
                                  # Correct: [18, 9, 999])
])
def test_order_by_points(nums, expected):
    """
    Tests the order_by_points function against various scenarios including
    empty lists, single elements, stability, negative numbers, and mixed inputs.
    Note: Tests follow the textual requirement: sort by sum of digits (abs), 
    then by original index.
    """
    assert order_by_points(nums) == expected

def test_order_by_points_large_input():
    """Test with a larger range of numbers to ensure performance and correctness."""
    nums = list(range(1, 101))
    # This is a sanity check to ensure it doesn't crash and returns a list of same length
    result = order_by_points(nums)
    assert len(result) == 100
    assert len(set(result)) == 100 # Ensure no duplicates were lost/added