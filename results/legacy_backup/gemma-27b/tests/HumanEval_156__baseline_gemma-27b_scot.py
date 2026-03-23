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

def test_valid_input_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_valid_input_tens():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(60) == 'lx'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(80) == 'lxxx'
    assert int_to_mini_roman(90) == 'xc'

def test_valid_input_hundreds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(900) == 'cm'

def test_valid_input_thousands():
    assert int_to_mini_roman(1000) == 'm'

def test_valid_input_combinations():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(888) == 'dccclxxxviii'

def test_valid_input_subtractive_notation():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_invalid_input_zero():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_invalid_input_negative():
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)

def test_invalid_input_greater_than_1000():
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)