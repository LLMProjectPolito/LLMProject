
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

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000.")

    result = ""
    integers = sorted(roman_map.keys(), reverse=True)  # Iterate in descending order

    for value in integers:
        while number >= value:
            result += roman_map[value]
            number -= value

    return result.lower()


def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_various_numbers():
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(99) == 'xciX'  # Corrected assertion
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(27) == 'xxvii'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(688) == 'dccxcviii'
    assert int_to_mini_roman(944) == 'cmxliv'
    assert int_to_mini_roman(1000) == 'm' # Added test for 1000

def test_int_to_mini_roman_invalid_input_type():
    with pytest.raises(TypeError):
        int_to_mini_roman("10")

def test_int_to_mini_roman_invalid_input_range_too_small():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_int_to_mini_roman_invalid_input_range_too_large():
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)