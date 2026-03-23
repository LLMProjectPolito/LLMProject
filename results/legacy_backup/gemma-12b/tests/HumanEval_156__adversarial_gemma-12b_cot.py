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
    def test_valid_input(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(5) == "v"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(10) == "x"
        assert int_to_mini_roman(19) == "xix"
        assert int_to_mini_roman(426) == "cdxxvi"
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(444) == "cdxliv"
        assert int_to_mini_roman(999) == "cmxciii"
        assert int_to_mini_roman(1000) == "m"

    def test_edge_cases(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(1000) == "m"
        assert int_to_mini_roman(399) == "cccxcix"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(900) == "cm"

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            int_to_mini_roman("abc")
        with pytest.raises(TypeError):
            int_to_mini_roman(1.5)
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)
        with pytest.raises(TypeError):
            int_to_mini_roman([1,2,3])