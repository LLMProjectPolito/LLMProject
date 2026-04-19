
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

def order_by_points(nums):
    """
    Implementation provided for the sake of testing. 
    The goal is to sort by sum of digits (absolute value) and maintain stability.
    """
    def get_digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    # Python's sorted() is stable by default, satisfying the index requirement.
    return sorted(nums, key=get_digit_sum)

class TestOrderByPoints:
    """
    Blue Team QA Suite to detect bugs in order_by_points.
    Focuses on: stability, negative numbers, edge cases, and large inputs.
    """

    @pytest.mark.parametrize("input_list, expected", [
        # Basic functionality
        ([1, 11, 2], [1, 2, 11]),
        ([10, 2, 1], [10, 1, 2]),
        
        # Empty and single element cases
        ([], []),
        ([5], [5]),
        
        # Stability Test: Items with same sum should maintain original relative order
        # 10 (sum 1), 1 (sum 1), 100 (sum 1) -> should remain in this order
        ([10, 1, 100], [10, 1, 100]),
        # 11 (sum 2), 2 (sum 2), 20 (sum 2) -> should remain in this order
        ([11, 2, 20], [11, 2, 20]),
        
        # Negative numbers: Sum of digits usually refers to the absolute value
        # -1 (sum 1), -11 (sum 2), -12 (sum 3)
        ([-1, -11, -12], [-1, -11, -12]),
        # -12 (sum 3), -1 (sum 1) -> [-1, -12]
        ([-12, -1], [-1, -12]),
        
        # Mixed signs and stability
        # 1 (sum 1), 11 (sum 2), -1 (sum 1), -11 (sum 2), -12 (sum 3)
        # Sum 1: [1, -1], Sum 2: [11, -11], Sum 3: [-12]
        ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]),
        
        # Zeros
        ([0, 0, 0], [0, 0, 0]),
        ([0, 1, 0], [0, 0, 1]),
        
        # Large numbers
        ([999, 1000, 1], [1000, 1, 999]), # sums: 27, 1, 1 -> [1000, 1, 999]
    ])
    def test_order_by_points_scenarios(self, input_list, expected):
        assert order_by_points(input_list) == expected

    def test_original_list_unmodified(self):
        """Ensure the function does not mutate the original input list."""
        original = [11, 1, 2]
        input_copy = list(original)
        order_by_points(input_copy)
        assert input_copy == original, "The original list should not be mutated."

    def test_large_dataset_stability(self):
        """Stress test for stability with a larger set of identical sums."""
        # Create a list of 100 numbers that all have a digit sum of 1
        # [1, 10, 100, 1000, ...]
        nums = [10**i for i in range(100)]
        result = order_by_points(nums)
        assert result == nums, "Stability failed on large dataset with identical sums."

    def test_extreme_values(self):
        """Test with very large integers to ensure no overflow or string conversion errors."""
        large_num_1 = 10**100 # sum 1
        large_num_2 = 10**100 - 1 # sum 9 * 100 = 900
        assert order_by_points([large_num_2, large_num_1]) == [large_num_1, large_num_2]