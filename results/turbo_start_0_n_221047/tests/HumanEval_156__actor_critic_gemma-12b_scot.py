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
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if not 1 <= number <= 1000:
        raise TypeError("Input must be between 1 and 1000.")

    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = len(integers) - 1
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result.lower()


class TestIntToMiniRoman:
    def test_typical_numbers(self):
        assert int_to_mini_roman(25) == "xxv"
        assert int_to_mini_roman(74) == "lxxiv"
        assert int_to_mini_roman(388) == "cccxxxviii"
        assert int_to_mini_roman(672) == "dclxxii"
        assert int_to_mini_roman(911) == "cmi"
        assert int_to_mini_roman(789) == "dlxxxix"
        assert int_to_mini_roman(888) == "dccclxxxviii"
        assert int_to_mini_roman(899) == "dcccxcix"
        assert int_to_mini_roman(944) == "cmxliv"
        assert int_to_mini_roman(999) == "cmxcix"

    def test_edge_cases(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(1000) == "m"

    def test_subtractive_cases(self):
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(90) == "xc"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(900) == "cm"

    def test_five_hundred(self):
        assert int_to_mini_roman(500) == "d"

    def test_complex_subtractive(self):
        assert int_to_mini_roman(444) == "cdxliv"
        assert int_to_mini_roman(888) == "dccclxxxviii"
        assert int_to_mini_roman(944) == "cmxliv"
        assert int_to_mini_roman(994) == "cmxciv"

    def test_invalid_input_type_string(self):
        with pytest.raises(TypeError):
            int_to_mini_roman("abc")