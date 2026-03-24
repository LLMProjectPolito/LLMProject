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
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result.lower()


class TestIntToMiniRoman:
    def test_valid_input_range_1(self):
        assert int_to_mini_roman(1) == "i"

    def test_valid_input_range_10(self):
        assert int_to_mini_roman(10) == "x"

    def test_valid_input_range_50(self):
        assert int_to_mini_roman(50) == "l"

    def test_valid_input_range_100(self):
        assert int_to_mini_roman(100) == "c"

    def test_valid_input_range_426(self):
        assert int_to_mini_roman(426) == "cdxxvi"

    def test_valid_input_range_999(self):
        assert int_to_mini_roman(999) == "cmxciii"

    def test_valid_input_range_1000(self):
        assert int_to_mini_roman(1000) == "m"

    def test_valid_input_typical_cases(self):
        assert int_to_mini_roman(19) == "xix"
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(388) == "cccxxxviii"
        assert int_to_mini_roman(426) == "cdxxvi"

    def test_valid_input_edge_cases(self):
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(8) == "viii"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(11) == "xi"
        assert int_to_mini_roman(14) == "xiv"
        assert int_to_mini_roman(16) == "xvi"
        assert int_to_mini_roman(18) == "xviii"
        assert int_to_mini_roman(44) == "xliv"
        assert int_to_mini_roman(48) == "xlviii"
        assert int_to_mini_roman(49) == "xlix"
        assert int_to_mini_roman(94) == "xciv"
        assert int_to_mini_roman(98) == "xcviii"
        assert int_to_mini_roman(99) == "xciii"

    def test_invalid_input_below_range(self):
        with pytest.raises(TypeError):
            int_to_mini_roman(0)

    def test_invalid_input_above_range(self):
        with pytest.raises(TypeError):
            int_to_mini_roman(1001)

    def test_lowercase_output(self):
        assert int_to_mini_roman(10) == "x"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(90) == "xc"