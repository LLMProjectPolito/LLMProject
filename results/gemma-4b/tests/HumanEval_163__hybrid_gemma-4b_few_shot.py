
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
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

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
    result = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                result.append(int(digit))
                break
    return sorted(list(set(result)))


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('No lemon, no melon') == True

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
    assert get_max([1, 1, 1]) == 1
    assert get_max([1, 2, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 2) == []
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(4, 2) == [2, 4]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 28) == [2, 4, 6, 8]
    assert generate_integers(28, 20) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []
    assert generate_integers(11, 13) == []

def test_generate_integers_large_range():
    assert generate_integers(100, 108) == [10, 12, 14, 16, 18]
    assert generate_integers(108, 100) == [10, 12, 14, 16, 18]

def test_generate_integers_with_duplicates():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_one_char():
    assert is_palindrome('a') == True

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_all_same():
    assert get_max([5, 5, 5]) == 5