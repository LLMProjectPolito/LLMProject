
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
    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000 inclusive.")

    result = ""
    for value, numeral in sorted(roman_map.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result

def test_int_to_mini_roman_raises_type_error_for_string():
    with pytest.raises(TypeError):
        int_to_mini_roman("5")

def test_int_to_mini_roman_raises_type_error_for_float():
    with pytest.raises(TypeError):
        int_to_mini_roman(5.5)

def test_int_to_mini_roman_raises_value_error_for_zero():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_int_to_mini_roman_raises_value_error_for_1001():
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)

def test_int_to_mini_roman_for_3():
    assert int_to_mini_roman(3) == 'iii'

def test_int_to_mini_roman_for_7():
    assert int_to_mini_roman(7) == 'vii'

def test_int_to_mini_roman_for_8():
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_for_33():
    assert int_to_mini_roman(33) == 'xxxiii'

def test_int_to_mini_roman_for_38():
    assert int_to_mini_roman(38) == 'xxxviii'

def test_int_to_mini_roman_for_83():
    assert int_to_mini_roman(83) == 'lxxxiii'

def test_int_to_mini_roman_for_88():
    assert int_to_mini_roman(88) == 'lxxxviii'

def test_int_to_mini_roman_for_399():
    assert int_to_mini_roman(399) == 'cccxcix'

def test_int_to_mini_roman_for_401():
    assert int_to_mini_roman(401) == 'cdi'

def test_int_to_mini_roman_for_899():
    assert int_to_mini_roman(899) == 'dcccxcix'

def test_int_to_mini_roman_for_901():
    assert int_to_mini_roman(901) == 'cmi'

def test_int_to_mini_roman_for_999():
    assert int_to_mini_roman(999) == 'cmxcix'

def test_int_to_mini_roman_for_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_for_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_for_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_for_888():
    assert int_to_mini_roman(888) == 'dccclxxxviii'