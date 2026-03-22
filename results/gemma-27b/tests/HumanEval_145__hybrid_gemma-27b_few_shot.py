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


def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_all_same_sum():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_order_by_points_duplicate_numbers():
    assert order_by_points([1, 1, 11, 11]) == [1, 1, 11, 11]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 6789, 12345]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_order_by_points_complex():
    assert order_by_points([21, 12, 3, 1, 2, 10, 11]) == [1, 2, 3, 10, 11, 12, 21]

def test_order_by_points_complex_case():
    assert order_by_points([21, 12, 3, 1, 100, 2, 11]) == [1, 2, 3, 11, 12, 21, 100]

def test_order_by_points_all_zeros():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_order_by_points_with_zero():
    assert order_by_points([10, 0, 1]) == [0, 1, 10]

def test_order_by_points_long_list():
    nums = list(range(100))
    expected = sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), nums.index(x)))
    assert order_by_points(nums) == expected

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None