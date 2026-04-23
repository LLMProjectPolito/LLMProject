
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
    s = s.lower()
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
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('Racecar') == True # Test case sensitivity
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with spaces and punctuation
    assert is_palindrome('madam') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('level') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome(' ') == True # Test with space
    assert is_palindrome('a') == True # Test with single character

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([5]) == 5
    assert get_max([10, 5, 20, 1]) == 20

def test_get_max_empty():
    assert get_max([]) == None

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(13, 8, 5) == 8
    assert x_or_y(2, 10, 5) == 10
    assert x_or_y(17, 1, 2) == 1
    assert x_or_y(3, 100, 5) == 100

def test_x_or_y_not_prime():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(6, 8, 5) == 5
    assert x_or_y(9, 100, 5) == 5
    assert x_or_y(10, 1, 2) == 2
    assert x_or_y(12, 100, 5) == 5

def test_x_or_y_edge_cases():
    assert x_or_y(1, 34, 12) == 34 # 1 is not prime
    assert x_or_y(2, 34, 12) == 34 # 2 is prime
    assert x_or_y(0, 34, 12) == 12 # 0 is not prime
    assert x_or_y(1, 34, 12) == 12 # 1 is not prime