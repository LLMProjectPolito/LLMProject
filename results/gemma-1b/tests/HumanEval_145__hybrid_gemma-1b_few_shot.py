import pytest

def order_by_points(nums):
    """ Sorts the given list of integers in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    def sum_digits(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """

    if not arr:
        return None

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def test_order_by_points_positive():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single():
    assert order_by_points([5]) == [5]

def test_order_by_points_duplicate_digits():
    assert order_by_points([11, 11, 11]) == [11, 11, 11]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, 1, -12]) == [-1, -11, 1, -12]

def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_get_max():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) == None