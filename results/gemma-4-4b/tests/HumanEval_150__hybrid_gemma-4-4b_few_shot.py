
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

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
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    if is_prime(n):
        return x
    else:
        return y

### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()  # Ignore case
    return s == s[::-1]

### Tests (Pytest):
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == False # Spaces matter

def test_palindrome_single_char():
    assert is_palindrome('a') == True
### Problem:
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

### Tests (Pytest):
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_single_element():
    assert get_max([5]) == 5
### Problem:
def sum_list(numbers: list[int]) -> int:
    """Calculates the sum of all numbers in a list."""
    total = 0
    for number in numbers:
        total += number
    return total

### Tests (Pytest):
def test_sum_empty():
    assert sum_list([]) == 0

def test_sum_positive():
    assert sum_list([1, 2, 3]) == 6

def test_sum_negative():
    assert sum_list([-1, -2, -3]) == -6

def test_sum_mixed():
    assert sum_list([-1, 2, -3, 4]) == 2

def test_sum_single():
    assert sum_list([5]) == 5