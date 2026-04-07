
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(5, 5) == []
    assert generate_integers(8, 8) == [8]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(5, 5) == []
    assert generate_integers(7, 7) == []
    assert generate_integers(9, 9) == []

def test_generate_integers_mixed_range():
    assert generate_integers(1, 3) == [2]
    assert generate_integers(4, 6) == [4, 6]
    assert generate_integers(7, 9) == [8]
    assert generate_integers(0, 1) == [0]
    assert generate_integers(0, 2) == [0, 2]

def test_generate_integers_larger_range():
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(5, 15) == [6, 8]
    assert generate_integers(11, 20) == []

def test_generate_integers_edge_cases():
    assert generate_integers(0, 0) == [0]
    assert generate_integers(1, 0) == [0]
    assert generate_integers(0, 1) == [0]
    assert generate_integers(9, 1) == [2, 4, 6, 8]

def test_generate_integers_negative_inputs():
    # The problem statement specifies positive integers, but let's test
    # how the function handles negative inputs.
    assert generate_integers(-2, -1) == []
    assert generate_integers(-1, 2) == [2]
    assert generate_integers(2, -1) == [2]
    assert generate_integers(-2, -8) == [2, 4, 6, 8]
    assert generate_integers(-8, -2) == [2, 4, 6, 8]
    assert generate_integers(-10, -14) == []

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]
    assert generate_integers(5, 5) == []

def test_generate_integers_larger_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_edge_cases_2():
    assert generate_integers(0, 1) == [0]
    assert generate_integers(1, 0) == [0]
    assert generate_integers(0, 0) == [0]

### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

### Tests (Pytest):
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False # Case sensitive

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