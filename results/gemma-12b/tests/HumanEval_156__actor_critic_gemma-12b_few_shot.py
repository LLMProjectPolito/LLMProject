
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
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000.")

    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    integers = list(roman_map)
    symbols = list(roman_map.values())

    result = ""

    for i in range(len(integers) - 1, -1, -1):
        while number >= integers[i]:
            result += symbols[i]
            number -= integers[i]

    return result.lower()


def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(500) == "d"

def test_int_to_mini_roman_subtractive():
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"

def test_int_to_mini_roman_mixed():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(888) == "dccclxxxviii"
    assert int_to_mini_roman(399) == "cccxcix"

def test_int_to_mini_roman_boundary():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_large():
    assert int_to_mini_roman(999) == "cmxcix"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(6) == "vi"
    assert int_to_mini_roman(7) == "vii"
    assert int_to_mini_roman(8) == "viii"
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(16) == "xvi"
    assert int_to_mini_roman(18) == "xviii"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(43) == "xl iii"
    assert int_to_mini_roman(44) == "xl iv"
    assert int_to_mini_roman(45) == "xl v"
    assert int_to_mini_roman(49) == "xl ix"
    assert int_to_mini_roman(51) == "li i"
    assert int_to_mini_roman(54) == "l iv"
    assert int_to_mini_roman(55) == "l v"
    assert int_to_mini_roman(59) == "l ix"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(69) == "lx ix"
    assert int_to_mini_roman(70) == "lxx"
    assert int_to_mini_roman(79) == "lxx ix"
    assert int_to_mini_roman(80) == "lxxx"
    assert int_to_mini_roman(89) == "lxxx ix"
    assert int_to_mini_roman(91) == "xci i"
    assert int_to_mini_roman(94) == "xc iv"
    assert int_to_mini_roman(95) == "xc v"
    assert int_to_mini_roman(99) == "xc ix"
    assert int_to_mini_roman(101) == "ci i"
    assert int_to_mini_roman(104) == "civ"
    assert int_to_mini_roman(105) == "c v"
    assert int_to_mini_roman(109) == "c ix"
    assert int_to_mini_roman(110) == "c x"
    assert int_to_mini_roman(119) == "c xix"
    assert int_to_mini_roman(140) == "c xl"
    assert int_to_mini_roman(149) == "c xl ix"
    assert int_to_mini_roman(150) == "cl"
    assert int_to_mini_roman(159) == "cl ix"
    assert int_to_mini_roman(190) == "cxc"
    assert int_to_mini_roman(199) == "cxc ix"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(299) == "ccxcix"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(399) == "cccxcix"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(401) == "cd i"
    assert int_to_mini_roman(444) == "cdxliv"
    assert int_to_mini_roman(499) == "cdxcix"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(501) == "di"
    assert int_to_mini_roman(549) == "d xl ix"
    assert int_to_mini_roman(599) == "dxcix"
    assert int_to_mini_roman(600) == "dc"
    assert int_to_mini_roman(699) == "dcxcix"
    assert int_to_mini_roman(700) == "dcc"
    assert int_to_mini_roman(799) == "dccxcix"
    assert int_to_mini_roman(800) == "dccc"
    assert int_to_mini_roman(899) == "dccxcix"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(901) == "cm i"
    assert int_to_mini_roman(949) == "cm xl ix"
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(TypeError):
        int_to_mini_roman("abc")
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)