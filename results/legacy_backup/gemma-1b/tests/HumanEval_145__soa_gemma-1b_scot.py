import pytest

def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in original list.
    """
    if not nums:
        return []

    def sum_digits(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s

    nums_with_index = list(enumerate(nums))
    nums_with_index.sort(key=lambda x: (sum_digits(x[1]), x[0]))
    return [num for _, num in nums_with_index]