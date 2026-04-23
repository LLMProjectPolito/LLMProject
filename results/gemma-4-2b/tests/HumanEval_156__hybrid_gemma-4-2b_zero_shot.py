
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if 1000 <= number <= 3999:
        roman_string = ""
        thousands = number // 1000
        number %= 1000
        roman_string += str(thousands) + "m"
        
        hundreds = number // 100
        number %= 100
        if hundreds > 0:
            roman_string += str(hundreds) + "c"
            
        tens = number // 10
        number %= 10
        if tens > 0:
            roman_string += str(tens) + "x"
            
        ones = number
        if ones > 0:
            if ones >= 5:
                roman_string += str(ones // 10) + "v"
                number %= 10
                if number >= 5:
                    roman_string += str(number // 10) + "v"
                    number %= 10
                else:
                    roman_string += str(number) + "i"
            elif ones >= 4:
                roman_string += "iv"
                number %= 10
                if number >= 5:
                    roman_string += "v"
                    number %= 10
                else:
                    roman_string += str(number) + "i"
            elif ones >= 9:
                roman_string += "ix"
                number %= 10
                if number >= 5:
                    roman_string += "v"
                    number %= 10
                else:
                    roman_string += str(number) + "i"
            else:
                roman_string += str(ones) + "i"
        
        return roman_string
    else:
        return "Invalid input"


class TestIntToMiniRoman:

    def test_single_digit(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(4) == 'iv'
        assert int_to_mini_roman(5) == 'v'
        assert int_to_mini_roman(9) == 'ix'

    def test_two_digits(self):
        assert int_to_mini_roman(10) == 'x'
        assert int_to_mini_roman(14) == 'xiv'
        assert int_to_mini_roman(19) == 'xix'
        assert int_to_mini_roman(40) == 'xl'
        assert int_to_mini_roman(49) == 'xlix'
        assert int_to_mini_roman(50) == 'l'
        assert int_to_mini_roman(90) == 'xc'
        assert int_to_mini_roman(99) == 'xciii'

    def test_three_digits(self):
        assert int_to_mini_roman(100) == 'c'
        assert int_to_mini_roman(400) == 'cd'
        assert int_to_mini_roman(500) == 'd'
        assert int_to_mini_roman(900) == 'cm'
        assert int_to_mini_roman(1000) == 'm'

    def test_complex_cases(self):
        assert int_to_mini_roman(152) == 'clii'
        assert int_to_mini_roman(426) == 'cdxxvi'
        assert int_to_mini_roman(2023) == 'mmxxiii'
        assert int_to_mini_roman(999) == 'cmxccii'
        assert int_to_mini_roman(101) == 'xci'
        assert int_to_mini_roman(300) == 'ccc'

    def test_edge_cases(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(1000) == 'm'
        assert int_to_mini_roman(0) == ''  # Although the problem says 1 <= num <= 1000, it is good practice to handle invalid input.
        assert int_to_mini_roman(1001) == 'm'


    def test_large_numbers(self):
        assert int_to_mini_roman(999) == "cmxccii"
        assert int_to_mini_roman(1999) == "mcmxcci"
        assert int_to_mini_roman(2023) == "mmxxiii"


    def test_invalid_input_raises_error(self):
        with pytest.raises(ValueError):
            int_to_mini_roman(-1) #Negative number
        with pytest.raises(ValueError):
            int_to_mini_roman(1001) #Number greater than 1000