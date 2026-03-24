
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
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(41) == 'xli'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(45) == 'xlv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(51) == 'li'
    assert int_to_mini_roman(54) == 'liv'
    assert int_to_mini_roman(55) == 'lv'
    assert int_to_mini_roman(59) == 'lix'
    assert int_to_mini_roman(60) == 'lx'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(91) == 'xci'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(95) == 'xcv'
    assert int_to_mini_roman(99) == 'xcix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(150) == 'cl'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(199) == 'cxcix'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(950) == 'cml'
    assert int_to_mini_roman(1000) == 'm'

    # Edge cases
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

    # Test cases around 4, 9, 40, 90, 400, 900
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'