
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Input must be an integer between 1 and 1000")

    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    result = ""

    for value, symbol in sorted(roman_map.items(), key=lambda item: item[0], reverse=True):
        while number >= value:
            result += symbol
            number -= value

    return result.lower()


def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_boundaries():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_repeated_symbols():
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(300) == 'ccc'

def test_int_to_mini_roman_subtractive_notation():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_all_symbols():
    assert int_to_mini_roman(199) == 'cxcix'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(999) == 'cmxcix'

def test_int_to_mini_roman_value_error_out_of_range():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)

def test_int_to_mini_roman_value_error_invalid_type():
    with pytest.raises(ValueError):
        int_to_mini_roman("10")
    with pytest.raises(ValueError):
        int_to_mini_roman(10.0)