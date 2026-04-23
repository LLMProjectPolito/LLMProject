
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if number in roman_map:
        return roman_map[number]
    
    result = ''
    i = 1000
    while number > 0:
        if number >= i:
            if i in roman_map:
                result += roman_map[i]
            number -= i
        elif number >= 500:
            if 500 in roman_map:
                result += roman_map[500]
            number -= 500
        elif number >= 100:
            if 100 in roman_map:
                result += roman_map[100]
            number -= 100
        elif number >= 50:
            if 50 in roman_map:
                result += roman_map[50]
            number -= 50
        elif number >= 10:
            if 10 in roman_map:
                result += roman_map[10]
            number -= 10
        elif number >= 5:
            if 5 in roman_map:
                result += roman_map[5]
            number -= 5
        elif number >= 1:
            if 1 in roman_map:
                result += roman_map[1]
            number -= 1
    return result.lower()


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'ix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_complex():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(144) == 'xiv'
    assert int_to_mini_roman(2023) == 'mmxxiii'
    assert int_to_mini_roman(3999) == 'mmmxcxc'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(0) == ''
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1001) == 'mci'
    assert int_to_mini_roman(10000) == 'x'
    assert int_to_mini_roman(100000) == 'c'
    assert int_to_mini_roman(1000000) == 'm'

def test_int_to_mini_roman_larger_numbers():
    assert int_to_mini_roman(1994) == 'mcmXCIV'
    assert int_to_mini_roman(2023) == 'mmxxiii'
    assert int_to_mini_roman(3999) == 'mmmxcxcix'

def test_int_to_mini_roman_with_more_complex_combinations():
    assert int_to_mini_roman(27) == 'xxvii'
    assert int_to_mini_roman(37) == 'xxxvii'
    assert int_to_mini_roman(69) == 'lvxix'

def test_int_to_mini_roman_invalid_input():
    assert int_to_mini_roman(-1) == ""
    assert int_to_mini_roman(1001) == "mci"  #Correct output

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None