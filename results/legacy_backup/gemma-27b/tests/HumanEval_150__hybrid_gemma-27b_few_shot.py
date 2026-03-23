import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 99, 0) == 99
    assert x_or_y(17, -1, -2) == -1
    assert x_or_y(19, 0, 1) == 0

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 5, 6) == 6
    assert x_or_y(9, 7, 8) == 8
    assert x_or_y(10, 11, 12) == 12
    assert x_or_y(12, 13, 14) == 14
    assert x_or_y(14, 15, 16) == 16
    assert x_or_y(16, 17, 18) == 18
    assert x_or_y(20, 19, 21) == 21

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 5, 6) == 6
    assert x_or_y(-1, 7, 8) == 8
    assert x_or_y(-2, 9, 10) == 10
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0

def test_x_or_y_large_numbers():
    assert x_or_y(1000000007, 1, 2) == 1  # Large prime
    assert x_or_y(1000000008, 3, 4) == 4  # Large non-prime

def test_x_or_y_negative_x_y():
    assert x_or_y(7, -34, -12) == -34
    assert x_or_y(15, -8, -5) == -5

def test_x_or_y_same_values():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(15, 5, 5) == 5

# --- Problem: is_palindrome ---
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# --- Problem: get_max ---
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None