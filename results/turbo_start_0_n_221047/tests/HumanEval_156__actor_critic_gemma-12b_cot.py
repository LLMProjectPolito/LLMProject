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
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")

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
        assert int_to_mini_roman(999) == "cmxcix"
        assert int_to_mini_roman(1000) == "m"
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(6) == "vi"
        assert int_to_mini_roman(7) == "vii"
        assert int_to_mini_roman(8) == "viii"
        assert int_to_mini_roman(41) == "xli"
        assert int_to_mini_roman(43) == "xliii"
        assert int_to_mini_roman(47) == "xlvii"
        assert int_to_mini_roman(48) == "xlviii"
        assert int_to_mini_roman(49) == "xlix"
        assert int_to_mini_roman(51) == "li"
        assert int_to_mini_roman(52) == "lii"
        assert int_to_mini_roman(53) == "liii"
        assert int_to_mini_roman(54) == "liv"
        assert int_to_mini_roman(55) == "lv"
        assert int_to_mini_roman(56) == "lvi"
        assert int_to_mini_roman(57) == "lvii"
        assert int_to_mini_roman(58) == "lviii"
        assert int_to_mini_roman(59) == "lix"
        assert int_to_mini_roman(91) == "xci"
        assert int_to_mini_roman(92) == "xcii"
        assert int_to_mini_roman(93) == "xciii"
        assert int_to_mini_roman(94) == "xciv"
        assert int_to_mini_roman(95) == "xcv"
        assert int_to_mini_roman(96) == "xcvi"
        assert int_to_mini_roman(97) == "xcvii"
        assert int_to_mini_roman(98) == "xcviii"
        assert int_to_mini_roman(99) == "xcix"

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(-1)
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)