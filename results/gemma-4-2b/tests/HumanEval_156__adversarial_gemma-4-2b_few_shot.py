
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
    thousands = number // 1000
    number %= 1000
    
    hundreds = number // 100
    number %= 100
    
    tens = number // 10
    number %= 10
    
    ones = number
    
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    for i in range(len(roman_values)):
        if hundreds >= roman_values[i]:
            result += roman_map[roman_values[i]]
            hundreds %= roman_values[i]
        elif hundreds < roman_values[i]:
            if hundreds > 0:
                result += 'm'
                hundreds = 0
    
    for i in range(len(roman_values)):
        if tens >= roman_values[i]:
            result += roman_map[roman_values[i]]
            tens %= roman_values[i]
        elif tens < roman_values[i]:
            if tens > 0:
                result += 'x'
                tens = 0
    
    for i in range(len(roman_values)):
        if ones >= roman_values[i]:
            result += roman_map[roman_values[i]]
            ones %= roman_values[i]
        elif ones < roman_values[i]:
            if ones > 0:
                result += 'i'
                ones = 0
    
    return result



@pytest.mark.parametrize("input_value, expected_output", [
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    (1, 'i'),
    (4, 'iv'),
    (5, 'v'),
    (9, 'ix'),
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xix'),
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    (1000, 'm'),
    (0, ''),
])
def test_int_to_mini_roman_all(input_value, expected_output):
    assert int_to_mini_roman(input_value) == expected_output

@pytest.mark.parametrize("input_value", [1, 2, 3])
def test_int_to_mini_roman_positive(input_value):
    assert int_to_mini_roman(input_value) == str(input_value)

@pytest.mark.parametrize("input_value", [1000])
def test_int_to_mini_roman_thousand(input_value):
    assert int_to_mini_roman(input_value) == 'm'

@pytest.mark.parametrize("input_value", [0])
def test_int_to_mini_roman_zero(input_value):
    assert int_to_mini_roman(input_value) == ''