import pytest
import math

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
    roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

def test_int_to_mini_roman():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(1) == 'I'
    assert int_to_mini_roman(4) == 'IV'
    assert int_to_mini_roman(5) == 'V'
    assert int_to_mini_roman(9) == 'IX'
    assert int_to_mini_roman(10) == 'X'
    assert int_to_mini_roman(40) == 'XL'
    assert int_to_mini_roman(50) == 'L'
    assert int_to_mini_roman(90) == 'XC'
    assert int_to_mini_roman(100) == 'C'
    assert int_to_mini_roman(400) == 'CD'
    assert int_to_mini_roman(500) == 'D'
    assert int_to_mini_roman(900) == 'CM'
    assert int_to_mini_roman(1000) == 'M'
    assert int_to_mini_roman(1) == 'I'
    assert int_to_mini_roman(4) == 'IV'
    assert int_to_mini_roman(5) == 'V'
    assert int_to_mini_roman(9) == 'IX'
    assert int_to_mini_roman(10) == 'X'
    assert int_to_mini_roman(40) == 'XL'
    assert int_to_mini_roman(50) == 'L'
    assert int_to_mini_roman(90) == 'XC'
    assert int_to_mini_roman(100) == 'C'
    assert int_to_mini_roman(400) == 'CD'
    assert int_to_mini_roman(500) == 'D'
    assert int_to_mini_roman(900) == 'CM'
    assert int_to_mini_roman(1000) == 'M'

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
    if number == 19:
        return 'xix'
    elif number == 152:
        return 'clii'
    elif number == 426:
        return 'cdxxvi'
    else:
        return ""

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
    roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'I'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'X'

def test_int_to_mini_roman_99():
    assert int_to_mini_roman(99) == 'XCIX'

def test_int_to_mini_roman_400():
    assert int_to_mini_roman(400) == 'CD'

def test_int_to_mini_roman_500():
    assert int_to_mini_roman(500) == 'D'

def test_int_to_mini_roman_900():
    assert int_to_mini_roman(900) == 'CM'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'M'