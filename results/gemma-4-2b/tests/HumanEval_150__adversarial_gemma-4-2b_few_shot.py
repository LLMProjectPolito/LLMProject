
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
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

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y


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

def test_palindrome_spaces():
    assert is_palindrome('   ') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True

def test_palindrome_with_punctuation():
    assert is_palindrome('.,?!') == True

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

# --- Tests for x_or_y ---
def test_x_or_y_prime_n():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 34, 12) == 34
    assert x_or_y(13, 34, 12) == 34
    assert x_or_y(17, 34, 12) == 34
    assert x_or_y(19, 34, 12) == 34

def test_x_or_y_not_prime_n():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(16, 8, 5) == 5
    assert x_or_y(18, 8, 5) == 5
    assert x_or_y(20, 8, 5) == 5
    assert x_or_y(21, 8, 5) == 5

def test_x_or_y_n_is_1():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_n_is_2():
    assert x_or_y(2, 34, 12) == 12

def test_x_or_y_n_is_3():
    assert x_or_y(3, 34, 12) == 34