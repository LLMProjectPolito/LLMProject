
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
    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000 inclusive.")

    result = ""
    for value, numeral in sorted(roman_map.items(), key=lambda item: item[0], reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result

def test_basic_values():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

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
    assert int_to_mini_roman(888) == 'dccclxxxviii'
    assert int_to_mini_roman(68) == 'lxviii'

def test_small_numbers():
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'

def test_out_of_range():
    @pytest.mark.parametrize("number", [0, -1, 1001, 2000])
    def test_value(number):
        with pytest.raises(ValueError):
            int_to_mini_roman(number)

def test_large_number():
    with pytest.raises(ValueError):
        int_to_mini_roman(4000)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)
    with pytest.raises(TypeError):
        int_to_mini_roman("10")