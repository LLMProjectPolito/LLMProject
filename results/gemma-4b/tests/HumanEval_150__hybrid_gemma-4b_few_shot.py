
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
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

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
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('aba') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_whitespace():
    assert is_palindrome('  ') == True
    assert is_palindrome(' a ') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaCeCaR') == True

def test_is_palindrome_numbers():
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([1, 1, 1]) == 1

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-3, -2, -1]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3]) == 2
    assert get_max([1, -2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 10) == 5
    assert x_or_y(13, 20, 1) == 20
    assert x_or_y(2, 100, 5) == 100

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(20, 1, 10) == 1
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(9, 100, 50) == 50

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 10
    assert x_or_y(2, 10, 20) == 20
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(2, 1, 1) == 1

def test_is_palindrome_extended():
    assert is_palindrome('A man, a plan, a canal: Panama!') == True
    assert is_palindrome('123454321') == True
    assert is_palindrome('hello world') == False

def test_get_max_all_negatives():
    assert get_max([-5, -2, -8]) == -2

def test_get_max_single_value():
    assert get_max([10]) == 10

def test_x_or_y_large_prime():
    assert x_or_y(1000000007, 1000000007, 1000000008) == 1000000007

def test_x_or_y_large_non_prime():
    assert x_or_y(1000000008, 1000000007, 1000000009) == 1000000007