
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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


# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('.,') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('b') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([10, 2, 5, 1]) == 10
    assert get_max([1, 5, 2, 8]) == 8

def test_max_empty():
    assert get_max([]) is None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-10, -2, -5]) == -2

def test_max_mixed_positive_negative():
    assert get_max([-1, 2, -3, 4]) == 4

# --- Tests for order_by_points ---
def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([1, 2, 3]) == [1, 2, 3]
    assert order_by_points([3, 2, 1]) == [1, 2, 3]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_same_sum():
    assert order_by_points([1, 11, 2, 21]) == [1, 2, 11, 21]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2]) == [1, -1, 2, -2]

def test_order_by_points_large_numbers():
    assert order_by_points([100, 10, 1]) == [1, 10, 100]

def test_order_by_points_with_zero():
    assert order_by_points([0, 1, 2, 0]) == [0, 0, 1, 2]