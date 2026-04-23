
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
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

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))  # Handle negative numbers
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)



# Pytest Suite
def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with spaces and punctuation
    assert is_palindrome('Racecar') == True # Test with uppercase letters
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('level') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('reviver') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('civic') == True
    assert is_palindrome('wow') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('aba') == True
    assert is_palindrome('abcba') == True
    assert is_palindrome('abcda') == False
    assert is_palindrome('123321') == True
    assert is_palindrome('1234321') == True
    assert is_palindrome('123454321') == True
    assert is_palindrome('12345678900987654321') == True


def test_get_max():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) == None
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([-1, -5, -2]) == -1
    assert get_max([0, 0, 0]) == 0
    assert get_max([1]) == 1
    assert get_max([-1]) == -1
    assert get_max([1, -1]) == 1
    assert get_max([1, 2, 3, 4, 5]) == 5
    assert get_max([5, 4, 3, 2, 1]) == 5
    assert get_max([1, 5, 2, 4, 3]) == 5
    assert get_max([-1, 0, 1]) == 1
    assert get_max([-1, -2, -3]) == -1
    assert get_max([10, 5, 20, 15]) == 20
    assert get_max([100, 50, 200, 150]) == 200


def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(1357) == (0, 3)
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(20) == (2, 0)
    assert even_odd_count(11) == (0, 2)
    assert even_odd_count(22) == (2, 0)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(21) == (1, 1)
    assert even_odd_count(102) == (2, 1)
    assert even_odd_count(201) == (1, 2)
    assert even_odd_count(-102) == (2, 1)
    assert even_odd_count(-201) == (1, 2)
    assert even_odd_count(12345678901234567890) == (10, 10)
    assert even_odd_count(-12345678901234567890) == (10, 10)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(21) == (1, 1)
    assert even_odd_count(10) == (1, 1)
    assert even_odd_count(20) == (2, 0)
    assert even_odd_count(11) == (0, 2)
    assert even_odd_count(22) == (2, 0)
    assert even_odd_count(13) == (0, 2)
    assert even_odd_count(31) == (0, 2)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(321) == (1, 2)
    assert even_odd_count(100) == (2, 0)
    assert even_odd_count(101) == (1, 1)
    assert even_odd_count(110) == (2, 1)
    assert even_odd_count(111) == (0, 3)
    assert even_odd_count(112) == (2, 1)
    assert even_odd_count(113) == (0, 2)
    assert even_odd_count(114) == (2, 1)
    assert even_odd_count(115) == (0, 2)
    assert even_odd_count(116) == (2, 1)
    assert even_odd_count(117) == (0, 2)
    assert even_odd_count(118) == (2, 1)
    assert even_odd_count(119) == (0, 2)
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(12345678901234567890) == (10, 10)
    assert even_odd_count(123456789012345678901234567890) == (15, 15)