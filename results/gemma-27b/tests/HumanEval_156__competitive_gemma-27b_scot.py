
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

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_5():
    assert int_to_mini_roman(5) == 'v'

def test_int_to_mini_roman_9():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_40():
    assert int_to_mini_roman(40) == 'xl'

def test_int_to_mini_roman_50():
    assert int_to_mini_roman(50) == 'l'

def test_int_to_mini_roman_90():
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_100():
    assert int_to_mini_roman(100) == 'c'

def test_int_to_mini_roman_400():
    assert int_to_mini_roman(400) == 'cd'

def test_int_to_mini_roman_500():
    assert int_to_mini_roman(500) == 'd'

def test_int_to_mini_roman_900():
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(3) == 'iii'

def test_int_to_mini_roman_6():
    assert int_to_mini_roman(6) == 'vi'

def test_int_to_mini_roman_7():
    assert int_to_mini_roman(7) == 'vii'

def test_int_to_mini_roman_8():
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_11():
    assert int_to_mini_roman(11) == 'xi'

def test_int_to_mini_roman_14():
    assert int_to_mini_roman(14) == 'xiv'

def test_int_to_mini_roman_16():
    assert int_to_mini_roman(16) == 'xvi'

def test_int_to_mini_roman_18():
    assert int_to_mini_roman(18) == 'xviii'

def test_int_to_mini_roman_20():
    assert int_to_mini_roman(20) == 'xx'

def test_int_to_mini_roman_39():
    assert int_to_mini_roman(39) == 'xxxix'

def test_int_to_mini_roman_44():
    assert int_to_mini_roman(44) == 'xliv'

def test_int_to_mini_roman_49():
    assert int_to_mini_roman(49) == 'xlix'

def test_int_to_mini_roman_89():
    assert int_to_mini_roman(89) == 'lxxxix'

def test_int_to_mini_roman_94():
    assert int_to_mini_roman(94) == 'xciv'

def test_int_to_mini_roman_99():
    assert int_to_mini_roman(99) == 'xcix'

def test_int_to_mini_roman_388():
    assert int_to_mini_roman(388) == 'cccLXXXVIII'

def test_int_to_mini_roman_765():
    assert int_to_mini_roman(765) == 'DCCLXV'