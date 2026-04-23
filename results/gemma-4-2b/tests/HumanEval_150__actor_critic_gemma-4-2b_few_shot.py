
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

```python
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


import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False
    assert is_palindrome(' ') == True
    assert is_palindrome('.,') == True
    assert is_palindrome('a') == True
    assert is_palindrome('') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_non_alphanumeric():
    assert is_palindrome('12321') == True
    assert is_palindrome('.,') == True
    assert is_palindrome(' ') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([1]) == 1
    assert get_max([1, 1]) == 1

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-3, -2, -1]) == -1
    assert get_max([-1]) == -1
    assert get_max([-1, -1]) == -1

def test_get_max_mixed():
    assert get_max([-1, 0, 1]) == 1
    assert get_max([0, -1, 1]) == 1
    assert get_max([1, 0, -1]) == 1

def test_x_or_y_prime_n():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 34, 12) == 34
    assert x_or_y(13, 34, 12) == 34
    assert x_or_y(17, 34, 12) == 34
    assert x_or_y(19, 34, 12) == 34
    assert x_or_y(23, 34, 12) == 34
    assert x_or_y(29, 34, 12) == 34
    assert x_or_y(31, 34, 12) == 34
    assert x_or_y(37, 34, 12) == 34
    assert x_or_y(41, 34, 12) == 34
    assert x_or_y(43, 34, 12) == 34
    assert x_or_y(47, 34, 12) == 34
    assert x_or_y(53, 34, 12) == 34
    assert x_or_y(59, 34, 12) == 34
    assert x_or_y(61, 34, 12) == 34
    assert x_or_y(67, 34, 12) == 34
    assert x_or_y(71, 34, 12) == 34
    assert x_or_y(73, 34, 12) == 34
    assert x_or_y(79, 34, 12) == 34
    assert x_or_y(83, 34, 12) == 34
    assert x_or_y(89, 34, 12) == 34
    assert x_or_y(97, 34, 12) == 34
    assert x_or_y(101, 34, 12) == 34
    assert x_or_y(103, 34, 12) == 34
    assert x_or_y(107, 34, 12) == 34
    assert x_or_y(109, 34, 12) == 34
    assert x_or_y(113, 34, 12) == 34
    assert x_or_y(127, 34, 12) == 34
    assert x_or_y(131, 34, 12) == 34
    assert x_or_y(137, 34, 12) == 34
    assert x_or_y(139, 34, 12) == 34
    assert x_or_y(149, 34, 12) == 34
    assert x_or_y(151, 34, 12) == 34
    assert x_or_y(157, 34, 12) == 34
    assert x_or_y(163, 34, 12) == 34
    assert x_or_y(167, 34, 12) == 34
    assert x_or_y(173, 34, 12) == 34
    assert x_or_y(179, 34, 12) == 34
    assert x_or_y(181, 34, 12) == 34
    assert x_or_y(191, 34, 12) == 34
    assert x_or_y(193, 34, 12) == 34
    assert x_or_y(197, 34, 12) == 34
    assert x_or_y(199, 34, 12) == 34
    assert x_or_y(211, 34, 12) == 34
    assert x_or_y(223, 34, 12) == 34
    assert x_or_y(227, 34, 12) == 34
    assert x_or_y(229, 34, 12) == 34
    assert x_or_y(233, 34, 12) == 34
    assert x_or_y(239, 34, 12) == 34
    assert x_or_y(241, 34, 12) == 34
    assert x_or_y(251, 34, 12) == 34
    assert x_or_y(257, 34, 12) == 34
    assert x