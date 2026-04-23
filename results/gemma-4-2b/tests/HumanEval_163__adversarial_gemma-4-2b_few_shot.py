
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits


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
    assert is_palindrome('.,?!') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('1') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([10, 5, 20, 1]) == 20
    assert get_max([1, 2, 3, 4, 5]) == 5

def test_max_empty():
    assert get_max([]) is None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative_and_positive():
    assert get_max([-1, -2, 0, 1, 2]) == 2

def test_max_all_same():
    assert get_max([5, 5, 5, 5]) == 5

# --- Tests for generate_integers ---
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_single_element():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(2, 1) == []

def test_generate_integers_start_greater_than_end():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_start_equal_to_end():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_large_range():
    assert generate_integers(100, 200) == [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]