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

def test_single_digit():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"

def test_small_numbers():
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(19) == "xix"

def test_repeated_numerals():
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(30) == "xxx"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(70) == "lxx"
    assert int_to_mini_roman(80) == "lxxx"

def test_mixed_numerals():
    assert int_to_mini_roman(15) == "xv"
    assert int_to_mini_roman(25) == "xxv"
    assert int_to_mini_roman(35) == "xxxv"
    assert int_to_mini_roman(45) == "xlv"
    assert int_to_mini_roman(55) == "lv"
    assert int_to_mini_roman(65) == "lxxv"
    assert int_to_mini_roman(75) == "lxxxv"
    assert int_to_mini_roman(85) == "lxxxv"
    assert int_to_mini_roman(95) == "xcv"

def test_larger_numbers():
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(149) == "cxlix"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(249) == "ccxliix"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(449) == "cdxlix"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(549) == "dxlix"
    assert int_to_mini_roman(600) == "dc"
    assert int_to_mini_roman(700) == "dcc"
    assert int_to_mini_roman(800) == "dccc"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(1000) == "m"

def test_edge_cases():
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(99) == "xix"
    assert int_to_mini_roman(49) == "xlix"
    assert int_to_mini_roman(59) == "lvix"
    assert int_to_mini_roman(89) == "lxxxix"