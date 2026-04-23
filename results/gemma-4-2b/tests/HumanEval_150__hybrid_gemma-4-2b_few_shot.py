
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
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('race car') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == False
    assert is_palindrome('RaceCar') == False
    assert is_palindrome('12321') == True
    assert is_palindrome("madamimadam") == True
    assert is_palindrome(".,;:'\"?!") == True

def test_get_max():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) == None
    assert get_max([5]) == 5
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([1, 1, 1, 1]) == 1
    assert get_max([1000000, 2000000, 3000000]) == 3000000
    assert get_max([1, 2.5, 3]) == 3
    assert get_max([3, 2.5, 1]) == 3

def test_x_or_y():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(11, 8, 5) == 8
    assert x_or_y(13, 1, 10) == 1
    assert x_or_y(2, 10, 5) == 10
    assert x_or_y(29, 100, 50) == 100
    assert x_or_y(31, 50, 100) == 50
    assert x_or_y(41, 100, 50) == 100
    assert x_or_y(1, 10, 5) == 5
    assert x_or_y(2, 10, 5) == 10
    assert x_or_y(3, 10, 5) == 10
    assert x_or_y(4, 10, 5) == 5
    assert x_or_y(5, 10, 5) == 10
    assert x_or_y(6, 10, 5) == 5
    assert x_or_y(7, 10, 5) == 5
    assert x_or_y(8, 10, 5) == 5
    assert x_or_y(9, 10, 5) == 5
    assert x_or_y(10, 10, 5) == 5
    assert x_or_y(11, 10, 5) == 10
    assert x_or_y(12, 10, 5) == 5
    assert x_or_y(13, 10, 5) == 5
    assert x_or_y(14, 10, 5) == 5
    assert x_or_y(15, 10, 5) == 5
    assert x_or_y(16, 10, 5) == 5
    assert x_or_y(17, 10, 5) == 10
    assert x_or_y(18, 10, 5) == 5
    assert x_or_y(19, 10, 5) == 5
    assert x_or_y(20, 10, 5) == 5
    assert x_or_y(21, 10, 5) == 5
    assert x_or_y(22, 10, 5) == 5
    assert x_or_y(23, 10, 5) == 5
    assert x_or_y(24, 10, 5) == 5
    assert x_or_y(25, 10, 5) == 5
    assert x_or_y(26, 10, 5) == 5
    assert x_or_y(27, 10, 5) == 5
    assert x_or_y(28, 10, 5) == 5
    assert x_or_y(29, 10, 5) == 5
    assert x_or_y(30, 10, 5) == 5
    assert x_or_y(31, 10, 5) == 10
    assert x_or_y(32, 10, 5) == 5
    assert x_or_y(33, 10, 5) == 5
    assert x_or_y(34, 10, 5) == 5
    assert x_or_y(35, 10, 5) == 5
    assert x_or_y(36, 10, 5) == 5
    assert x_or_y(37, 10, 5) == 10
    assert x_or_y(38, 10, 5) == 5
    assert x_or_y(39, 10, 5) == 5
    assert x_or_y(40, 10, 5) == 5
    assert x_or_y(41, 10, 5) == 10
    assert x_or_y(42, 10, 5) == 5
    assert x_or_y(43, 10, 5) == 5
    assert x_or_y(44, 10, 5) == 5
    assert x_or_y(45, 10, 5) == 5
    assert x_or_y(46, 10, 5) == 5
    assert x_or_y(47, 10, 5) == 10
    assert x_or_y(48, 10, 5) == 5
    assert x_or_y(49, 10, 5) == 5
    assert x_or_y(50, 10, 5) == 5