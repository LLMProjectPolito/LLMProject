
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

import pytest

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result.lower()


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)



def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(999) == 'cxcciii'



def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_larger_numbers():
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(17) == 'xvii'
    assert int_to_mini_roman(18) == 'xviii'
    assert int_to_mini_roman(21) == 'xxi'
    assert int_to_mini_roman(25) == 'xxv'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(59) == 'lix'
    assert int_to_mini_roman(64) == 'lxvi'
    assert int_to_mini_roman(89) == 'lxxxix'
    assert int_to_mini_roman(94) == 'xxciv'
    assert int_to_mini_roman(99) == 'xixc'
    assert int_to_mini_roman(999) == 'cxcciii'

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_palindrome_with_numbers():
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single_element():
    assert get_max([5]) == 5