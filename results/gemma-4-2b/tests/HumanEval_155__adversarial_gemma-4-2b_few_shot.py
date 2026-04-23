
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
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



# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('b') == True

def test_palindrome_with_spaces():
    assert is_palindrome('  madam  ') == True

def test_palindrome_with_special_chars():
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_palindrome_negative_number():
    assert is_palindrome('-121') == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) is None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_duplicate():
    assert get_max([1, 1, 1]) == 1

# --- Tests for even_odd_count ---
def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-24) == (2, 0)
    assert even_odd_count(-135) == (0, 3)

def test_even_odd_count_mixed():
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)