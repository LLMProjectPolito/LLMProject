
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

```python
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
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True

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
    assert get_max([-1, -2, -3]) == -1

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative_and_positive():
    assert get_max([-1, 2, -3, 4]) == 4

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 34, 12) == 34
    assert x_or_y(13, 34, 12) == 34
    assert x_or_y(17, 34, 12) == 34
    assert x_or_y(19, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(20, 8, 5) == 5
    assert x_or_y(21, 8, 5) == 5
    assert x_or_y(25, 8, 5) == 5
    assert x_or_y(27, 8, 5) == 5

def test_x_or_y_edge_cases():
    assert x_or_y(1, 34, 12) == 34
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(4, 34, 12) == 34
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(6, 34, 12) == 34
    assert x_or_y(8, 34, 12) == 34
    assert x_or_y(9, 34, 12) == 34
    assert x_or_y(10, 34, 12) == 34
    assert x_or_y(12, 34, 12) == 34
    assert x_or_y(14, 34, 12) == 34
    assert x_or_y(16, 34, 12) == 34
    assert x_or_y(18, 34, 12) == 34
    assert x_or_y(20, 34, 12) == 34
    assert x_or_y(22, 34, 12) == 34
    assert x_or_y(24, 34, 12) == 34
    assert x_or_y(26, 34, 12) == 34
    assert x_or_y(28, 34, 12) == 34
    assert x_or_y(30, 34, 12) == 34
    assert x_or_y(32, 34, 12) == 34
    assert x_or_y(33, 34, 12) == 34
    assert x_or_y(35, 34, 12) == 34
    assert x_or_y(36, 34, 12) == 34
    assert x_or_y(38, 34, 12) == 34
    assert x_or_y(39, 34, 12) == 34
    assert x_or_y(40, 34, 12) == 34
    assert x_or_y(42, 34, 12) == 34
    assert x_or_y(44, 34, 12) == 34
    assert x_or_y(45, 34, 12) == 34
    assert x_or_y(46, 34, 12) == 34
    assert x_or_y(48, 34, 12) == 34
    assert x_or_y(49, 34, 12) == 34
    assert x_or_y(50, 34, 12) == 34
    assert x_or_y(51, 34, 12) == 34
    assert x_or_y(52, 34, 12) == 34
    assert x_or_y(54, 34, 12) == 34
    assert x_or_y(55, 34, 12) == 34
    assert x_or_y(56, 34, 12) == 34
    assert x_or_y(57, 34, 12) == 34
    assert x_or_y(58, 34, 12) == 34
    assert x_or_y(60, 34, 12) == 34
    assert x_or_y(62, 34, 12) == 34
    assert x_or_y(63, 34, 12) == 34
    assert x_or_y(64, 34, 12) == 34
    assert x_or_y(65, 34, 12) == 34
    assert x_or_y(66, 34, 12) == 34
    assert x_or_y(68, 34, 12) == 34
    assert x_or_y(69, 34, 12) == 34
    assert x_or_