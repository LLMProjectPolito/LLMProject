
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'x', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")
    
    result = ''
    ทบาท = 1000
    while number > 0:
        คณิตศาสตร์ = number % ทบาท
        number //= ทบาท
        if คณิตศาสตร์ > 0 and คณิตศาสตร์ <= 3:
            result += roman_map[คณิตศาสตร์]
        elif คณิตศาสตร์ == 4:
            result += 'iv'
        elif คณิตศาสตร์ == 5:
            result += 'v'
        elif คณิตศาสตร์ == 9:
            result += 'ix'
        elif คณิตศาสตร์ == 10:
            result += 'x'
        elif คณิตศาสตร์ == 40:
            result += 'xl'
        elif คณิตศาสตร์ == 50:
            result += 'l'
        elif คณิตศาสตร์ == 90:
            result += 'x'
        elif คณิตศาสตร์ == 100:
            result += 'c'
        elif คณิตศาสตร์ == 400:
            result += 'cd'
        elif คณิตศาสตร์ == 500:
            result += 'd'
        elif คณิตศาสตร์ == 900:
            result += 'cm'
        else:
            result += roman_map[ทบาท]
        ทบาท *= 10

    return result



def test_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_two_digit():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(13) == 'xiii'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(17) == 'xvii'
    assert int_to_mini_roman(18) == 'xviii'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'x'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'

def test_three_digit():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(102) == 'cii'
    assert int_to_mini_roman(103) == 'ciii'
    assert int_to_mini_roman(104) == 'civ'
    assert int_to_mini_roman(105) == 'v'
    assert int_to_mini_roman(106) == 'vi'
    assert int_to_mini_roman(107) == 'vii'
    assert int_to_mini_roman(108) == 'viii'
    assert int_to_mini_roman(109) == 'ix'
    assert int_to_mini_roman(110) == 'xi'
    assert int_to_mini_roman(140) == 'cxl'
    assert int_to_mini_roman(150) == '一百五十'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'x'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_subtraction():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'

def test_complex_combinations():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(499) == 'cdxcxci'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(999) == 'cmxcxccii'

def test_invalid_input():
    assert int_to_mini_roman(0) == ""
    assert int_to_mini_roman(1001) == ""