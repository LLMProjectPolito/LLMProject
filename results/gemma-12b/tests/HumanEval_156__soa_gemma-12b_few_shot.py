
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

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(6) == "vi"
    assert int_to_mini_roman(7) == "vii"
    assert int_to_mini_roman(8) == "viii"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"

def test_int_to_mini_roman_intermediate():
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(15) == "xv"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(44) == "xliv"
    assert int_to_mini_roman(49) == "xlix"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(51) == "li"
    assert int_to_mini_roman(54) == "liv"
    assert int_to_mini_roman(59) == "lvix"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(61) == "lxi"
    assert int_to_mini_roman(64) == "lxiv"
    assert int_to_mini_roman(69) == "lxix"
    assert int_to_mini_roman(70) == "lxx"
    assert int_to_mini_roman(71) == "lxxi"
    assert int_to_mini_roman(74) == "lxxiv"
    assert int_to_mini_roman(79) == "lxxix"
    assert int_to_mini_roman(80) == "lxxx"
    assert int_to_mini_roman(81) == "lxxxi"
    assert int_to_mini_roman(84) == "lxxxiv"
    assert int_to_mini_roman(89) == "lxxxix"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(91) == "xci"
    assert int_to_mini_roman(94) == "xciv"
    assert int_to_mini_roman(99) == "xciix"
    assert int_to_mini_roman(100) == "c"

def test_int_to_mini_roman_advanced():
    assert int_to_mini_roman(101) == "ci"
    assert int_to_mini_roman(149) == "cxlix"
    assert int_to_mini_roman(150) == "cl"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(199) == "cxcix"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(244) == "ccxliv"
    assert int_to_mini_roman(299) == "ccxcix"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(344) == "cccxliv"
    assert int_to_mini_roman(399) == "cccxcix"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(444) == "cdxliv"
    assert int_to_mini_roman(499) == "cdxcix"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(501) == "di"
    assert int_to_mini_roman(544) == "divxliv"
    assert int_to_mini_roman(599) == "divxcix"
    assert int_to_mini_roman(600) == "dc"
    assert int_to_mini_roman(644) == "dcxliv"
    assert int_to_mini_roman(699) == "dcxcix"
    assert int_to_mini_roman(700) == "dcc"
    assert int_to_mini_roman(744) == "dccxliv"
    assert int_to_mini_roman(799) == "dccxcix"
    assert int_to_mini_roman(800) == "dccc"
    assert int_to_mini_roman(844) == "dcccxliv"
    assert int_to_mini_roman(899) == "dccxcix"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(944) == "cmxliv"
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(TypeError):
        int_to_mini_roman("abc")
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)