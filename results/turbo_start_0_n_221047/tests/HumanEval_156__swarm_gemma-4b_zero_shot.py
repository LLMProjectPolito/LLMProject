import pytest
import math

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
    
def test_edge_case_one():
    assert int_to_mini_roman(1) == 'i'

def test_edge_case_five():
    assert int_to_mini_roman(5) == 'v'

def test_edge_case_ten():
    assert int_to_mini_roman(10) == 'x'

def test_simple_case_19():
    assert int_to_mini_roman(19) == 'xix'

def test_simple_case_152():
    assert int_to_mini_roman(152) == 'clii'

def test_simple_case_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_larger_number_444():
    assert int_to_mini_roman(444) == 'cdxliv'

def test_another_larger_number_999():
    assert int_to_mini_roman(999) == 'cmlxix'