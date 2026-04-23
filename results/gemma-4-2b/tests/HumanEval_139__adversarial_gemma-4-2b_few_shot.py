
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
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

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n <= 0:
        return 1  # Handle non-positive input gracefully
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result


# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('   ') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('b') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True
    assert is_palindrome('level') == True

def test_palindrome_with_spaces():
    assert is_palindrome('rotor') == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed_numbers():
    assert get_max([-1, 2, -3, 4]) == 4

# --- Tests for special_factorial ---
def test_special_factorial_basic():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 1440
    assert special_factorial(6) == 2880
    assert special_factorial(7) == 5040
    assert special_factorial(8) == 40320
    assert special_factorial(9) == 362880
    assert special_factorial(10) == 3628800

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_negative():
    assert special_factorial(-1) == 1
    assert special_factorial(-5) == 1