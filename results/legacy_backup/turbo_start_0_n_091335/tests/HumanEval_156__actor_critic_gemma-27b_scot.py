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
    result = ""

    for value, numeral in sorted(roman_map.items(), key=lambda item: item[0], reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result

def test_input_validation():
    with pytest.raises(TypeError, match="Input must be an integer."):
        int_to_mini_roman("abc")
    with pytest.raises(TypeError, match="Input must be an integer."):
        int_to_mini_roman(3.14)
    with pytest.raises(ValueError, match="Number must be between 1 and 1000."):
        int_to_mini_roman(0)
    with pytest.raises(ValueError, match="Number must be between 1 and 1000."):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError, match="Number must be between 1 and 1000."):
        int_to_mini_roman(3999)

def test_subtractive_notation():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_combinations():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(888) == 'dccclxxxviii'
    assert int_to_mini_roman(1000) == 'm'