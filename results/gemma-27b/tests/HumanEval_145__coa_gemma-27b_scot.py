import pytest
import math


# Focus: Digit Sum Calculation
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
    pass

def digit_sum(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_multiple_elements_different_sums():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_multiple_elements_same_sums():
    assert order_by_points([10, 1, 19, 100]) == [1, 10, 19, 100]

def test_negative_numbers():
    assert order_by_points([1, -11, -1, -11, -12]) == [-1, -11, -11, 1, -12]

def test_mixed_positive_negative():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_zero_and_positive():
    assert order_by_points([0, 1, 10, 100]) == [0, 1, 10, 100]

def test_zero_and_negative():
    assert order_by_points([0, -1, -10, -100]) == [0, -1, -10, -100]

# Focus: Empty/Null Input
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

def test_empty_list():
    """Test with an empty list."""
    assert order_by_points([]) == []

def test_null_input():
    """Test with None input."""
    with pytest.raises(TypeError):
        order_by_points(None)

# Focus: Tie-breaking with Original Index
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

def test_tie_breaking_original_index_1():
    """Test tie-breaking with original index when multiple numbers have the same digit sum."""
    nums = [10, 1, 19, 100]
    expected = [1, 10, 19, 100]
    assert order_by_points(nums) == expected

def test_tie_breaking_original_index_2():
    """Test tie-breaking with original index with negative numbers."""
    nums = [-10, -1, -19, -100]
    expected = [-1, -10, -19, -100]
    assert order_by_points(nums) == expected

def test_tie_breaking_original_index_3():
    """Test tie-breaking with original index with mixed positive and negative numbers."""
    nums = [10, -1, 19, -10]
    expected = [-1, 10, 19, -10]
    assert order_by_points(nums) == expected