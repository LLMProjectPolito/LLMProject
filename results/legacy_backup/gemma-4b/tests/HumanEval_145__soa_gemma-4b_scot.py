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

### STEP 1: REASONING
# The function `order_by_points` sorts a list of integers based on the sum of their digits,
# with a tie-breaker using the original index of the numbers in the list.
# The test suite needs to cover various scenarios including:
# 1. Empty list: Should return an empty list.
# 2. List with positive numbers: Should sort based on digit sum.
# 3. List with negative numbers: Should sort based on digit sum, considering the absolute value.
# 4. List with mixed positive and negative numbers: Should sort based on digit sum, considering the absolute value.
# 5. List with numbers having the same digit sum: Should sort based on original index.
# 6. List with duplicate numbers: Should maintain original order for duplicates.

### STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests the case when the input list is empty.
# - test_positive_numbers: Tests the case when the input list contains only positive numbers.
# - test_negative_numbers: Tests the case when the input list contains only negative numbers.
# - test_mixed_numbers: Tests the case when the input list contains both positive and negative numbers.
# - test_same_digit_sum: Tests the case when multiple numbers have the same digit sum.
# - test_duplicate_numbers: Tests the case when the input list contains duplicate numbers.

### STEP 3: CODE
def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22, 3]) == [1, 2, 3, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22, -3]) == [-1, -2, -3, -11, -22]

def test_mixed_numbers():
    assert order_by_points([1, -1, 11, -11, 2, -2]) == [-1, -2, 1, -11, 2, 11]

def test_same_digit_sum():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_duplicate_numbers():
    assert order_by_points([1, 11, 1, 11]) == [1, 1, 11, 11]