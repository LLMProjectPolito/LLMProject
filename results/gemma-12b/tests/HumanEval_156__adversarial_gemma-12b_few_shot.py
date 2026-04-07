
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
from your_module import int_to_mini_roman  # Replace your_module

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

def test_int_to_mini_roman_teen():
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(12) == "xii"
    assert int_to_mini_roman(13) == "xiii"
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(15) == "xv"
    assert int_to_mini_roman(16) == "xvi"
    assert int_to_mini_roman(17) == "xvii"
    assert int_to_mini_roman(18) == "xviii"
    assert int_to_mini_roman(19) == "xix"

def test_int_to_mini_roman_twenties():
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(21) == "xxi"
    assert int_to_mini_roman(29) == "xix"

def test_int_to_mini_roman_forties():
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(49) == "xlix"

def test_int_to_mini_roman_fifties():
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(51) == "li"
    assert int_to_mini_roman(59) == "lix"

def test_int_to_mini_roman_sixties():
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(61) == "lxi"
    assert int_to_mini_roman(69) == "lxix"

def test_int_to_mini_roman_seventies():
    assert int_to_mini_roman(70) == "lx"
    assert int_to_mini_roman(71) == "lxi"
    assert int_to_mini_roman(79) == "lxix"

def test_int_to_mini_roman_eighties():
    assert int_to_mini_roman(80) == "lxxx"
    assert int_to_mini_roman(81) == "lxxxi"
    assert int_to_mini_roman(89) == "lxxxix"

def test_int_to_mini_roman_nineties():
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(91) == "xci"
    assert int_to_mini_roman(99) == "xciix"

def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(101) == "ci"
    assert int_to_mini_roman(149) == "cxlix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(199) == "cxcix"

def test_int_to_mini_roman_larger_numbers():
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(575) == "dlxxv"
    assert int_to_mini_roman(944) == "cmlxxxiv"
    assert int_to_mini_roman(999) == "cmlxxxix"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1000) == "m" # Technically outside the range, but good to test
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(399) == "cccxcix"

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)  # Should raise an error
    with pytest.raises(ValueError):
        int_to_mini_roman(1001) # Should raise an error
    with pytest.raises(TypeError):
        int_to_mini_roman("abc") # Should raise an error
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5) # Should raise an error