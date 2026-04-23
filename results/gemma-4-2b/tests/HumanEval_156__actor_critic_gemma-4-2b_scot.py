
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
    roman_map = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")

    result = ''
    while number:
        if number >= 1000:
            number -= 1000
        elif number >= 900:
            number -= 900
        elif number >= 500:
            number -= 500
        elif number >= 400:
            number -= 400
        elif number >= 100:
            number -= 100
        elif number >= 90:
            number -= 90
        elif number >= 50:
            number -= 50
        elif number >= 40:
            number -= 40
        elif number >= 10:
            number -= 10
        elif number >= 9:
            number -= 9
        elif number >= 5:
            number -= 5
        elif number >= 4:
            number -= 4
        elif number >= 1:
            number -= 1
        result += roman_map[number]
    return result.lower()


class TestIntToMiniRoman:

    def test_basic_cases(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(14) == "xiv"
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(49) == "xlix"
        assert int_to_mini_roman(50) == "l"
        assert int_to_mini_roman(99) == "xciii"
        assert int_to_mini_roman(100) == "c"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(900) == "cm"
        assert int_to_mini_roman(1000) == "m"

    def test_edge_cases(self):
        assert int_to_mini_roman(1001) == pytest.raises(ValueError)
        assert int_to_mini_roman(0) == pytest.raises(ValueError)
        assert int_to_mini_roman(1000) == "m"

    def test_invalid_input(self):
        with pytest.raises(ValueError) as excinfo:
            int_to_mini_roman(1001)
        assert "Number must be between 1 and 1000" in str(excinfo.value)
        with pytest.raises(ValueError) as excinfo:
            int_to_mini_roman(0)
        assert "Number must be between 1 and 1000" in str(excinfo.value)