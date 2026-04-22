
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_numbers = []
    start = min(a, b)
    end = max(a, b)

    for i in range(start, end + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('Racecar') == True  # Test case-insensitivity
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with spaces and punctuation
    assert is_palindrome('madam') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('level') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome(' ') == True # Test with space
    assert is_palindrome('') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2, 7]) == 9
    assert get_max([10, 5, 20, 1]) == 20

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative_numbers():
    assert get_max([-1, -5, -2]) == -1

def test_get_max_mixed_numbers():
    assert get_max([-1, 5, -2, 10]) == 10

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 6) == [4, 6]
    assert generate_integers(1, 10) == [2, 4, 6, 8, 10]
    assert generate_integers(10, 1) == [2, 4, 6, 8, 10]
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 1) == [2]
    assert generate_integers(0, 0) == [] #edge case
    assert generate_integers(0, 1) == [2] #edge case
    assert generate_integers(1, 0) == [2] #edge case