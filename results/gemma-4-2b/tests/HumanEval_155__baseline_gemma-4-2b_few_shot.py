
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Added test case

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-3, -2, -1]) == -1

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(246) == (3, 0)
    assert even_odd_count(135) == (0, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-123) == (2, 1)
    assert even_odd_count(-1234) == (2, 2)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)