
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
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
    num = abs(num)
    even_count = 0
    odd_count = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaCeCaR') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Madam, I\'m Adam') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([1, 1, 1]) == 1

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-3, -2, -1]) == -1
    assert get_max([-1, -1, -1]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3]) == 2
    assert get_max([1, -2, 3]) == 3
    assert get_max([-1, 0, 1]) == 1

def test_get_max_empty():
    assert get_max([]) == None

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(246) == (3, 0)
    assert even_odd_count(1357) == (0, 4)
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-246) == (3, 0)
    assert even_odd_count(-1357) == (0, 4)
    assert even_odd_count(-2468) == (4, 0)

def test_even_odd_count_mixed():
    assert even_odd_count(1234) == (2, 2)
    assert even_odd_count(-1234) == (2, 2)
    assert even_odd_count(12a4) == (2, 2) #Handles non-digit characters
    assert even_odd_count(-12a4) == (2, 2)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_no_alphanumeric():
    assert is_palindrome('!@#$%^') == True

def test_palindrome_with_spaces():
    assert is_palindrome("race car") == True

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative_single_element():
    assert get_max([-5]) == -5

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(3) == (0, 1)