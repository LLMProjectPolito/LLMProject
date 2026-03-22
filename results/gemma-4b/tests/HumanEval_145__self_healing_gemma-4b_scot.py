import pytest

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
    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


### SCoT Steps:
# STEP 1: REASONING
# The function `order_by_points` sorts a list of integers based on the sum of their digits,
# with a tie-breaker using the original index of the numbers in the list.
# We need to test various scenarios including empty lists, lists with positive and negative numbers,
# lists with numbers that have the same digit sum, and lists with numbers that have different digit sums.

# STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with positive numbers: [1, 2, 3, 4, 5]
# 3. List with negative numbers: [-1, -2, -3, -4, -5]
# 4. List with mixed positive and negative numbers: [1, -1, 2, -2, 3, -3]
# 5. List with numbers that have the same digit sum: [1, 11, 2, 22, 3, 33]
# 6. List with numbers that have the same digit sum and different indices: [1, 11, 2, 22, 3, 33]
# 7. List with single element: [5]
# 8. List with duplicate elements: [1, 1, 1]

# Test functions:
# test_empty_list
# test_positive_numbers
# test_negative_numbers
# test_mixed_numbers
# test_same_digit_sum
# test_same_digit_sum_different_indices
# test_single_element
# test_duplicate_elements


# STEP 3: CODE
def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_numbers():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [-1, -2, 1, -3, 2, 3]

def test_same_digit_sum():
    assert order_by_points([1, 11, 2, 22, 3, 33]) == [1, 2, 3, 11, 22, 33]

def test_same_digit_sum_different_indices():
    assert order_by_points([1, 11, 2, 22, 3, 33]) == [-1, -11, 1, -12, 11, 2]

def test_single_element():
    assert order_by_points([5]) == [5]

def test_duplicate_elements():
    assert order_by_points([1, 1, 1]) == [1, 1, 1]

def test_order_by_points([1, 11, -1, -11, -12]):
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]