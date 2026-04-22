
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
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def sum_digits(n):
        n = abs(n)
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()  # Ignore case
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
        ([], []),
        ([12, 1, 21], [1, 12, 21]),
        ([-1, 0, 1], [-1, 0, 1]),
        ([100, 10, 1], [1, 10, 100]),
        ([1, 10, 100, 1000], [1, 10, 100, 1000]),
        ([-10, -1, 0, 1, 10], [-10, -1, 0, 1, 10]),
        ([11, 2, 1], [1, 11, 2]),
        ([2,11,1], [1, 2, 11]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted
        ([100, 10, 1], [1, 10, 100]),
        ([10,1], [1, 10]),
    ],
)
def test_order_by_points_basic(input_list, expected_output):
    assert order_by_points(input_list) == expected_output


def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -12, -100]) == [-1, -100, -11, -12]


def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [-1, 1, -10, 10]


def test_order_by_points_large_numbers():
    assert order_by_points([1000, 100, 10, 1]) == [1, 10, 100, 1000]

def test_order_by_points_duplicates():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_order_by_points_zeroes():
  assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_order_by_points_single_element():
  assert order_by_points([5]) == [5]



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == False # spaces matter

def test_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == False # punctuation matters

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_single_char_not_palindrome():
    assert is_palindrome('b') == True # single character is a palindrome

def test_palindrome_numbers():
    assert is_palindrome('121') == True

def test_palindrome_numbers_not_palindrome():
    assert is_palindrome('123') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single_element():
    assert get_max([5]) == 5