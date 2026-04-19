
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
    """
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]
    roman_num = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num

class TestIntToMiniRoman:
    """
    Comprehensive test suite for int_to_mini_roman.
    Merges boundary analysis, subtractive logic, complex combinations, 
    and edge-case handling.
    """

    @pytest.mark.parametrize("number, expected", [
        (1, 'i'),
        (1000, 'm'),
    ])
    def test_boundaries(self, number, expected):
        """Test the minimum and maximum allowed input values."""
        assert int_to_mini_roman(number) == expected

    @pytest.mark.parametrize("number, expected", [
        (4, 'iv'),
        (9, 'ix'),
        (40, 'xl'),
        (90, 'xc'),
        (400, 'cd'),
        (900, 'cm'),
    ])
    def test_subtractive_notations(self, number, expected):
        """Test specific cases where Roman numerals use subtraction (4s and 9s)."""
        assert int_to_mini_roman(number) == expected

    @pytest.mark.parametrize("number, expected", [
        (5, 'v'),
        (10, 'x'),
        (50, 'l'),
        (100, 'c'),
        (500, 'd'),
    ])
    def test_single_character_values(self, number, expected):
        """Test the base Roman numeral characters."""
        assert int_to_mini_roman(number) == expected

    @pytest.mark.parametrize("number, expected", [
        (19, 'xix'),
        (152, 'clii'),
        (426, 'cdxxvi'),
    ])
    def test_provided_examples(self, number, expected):
        """Test the examples provided in the problem description."""
        assert int_to_mini_roman(number) == expected

    @pytest.mark.parametrize("number, expected", [
        (2, 'ii'),
        (3, 'iii'),
        (8, 'viii'),
        (20, 'xx'),
        (80, 'lxxx'),
        (300, 'ccc'),
        (800, 'dccc'),
        (38, 'xxxviii'),
        (88, 'lxxxviii'),
        (99, 'xcix'),
        (399, 'cccxcix'),
        (444, 'cdxliv'),
        (888, 'dccclxxxviii'),
        (999, 'cmxcix'),
    ])
    def test_complex_combinations(self, number, expected):
        """Test a variety of complex numbers to ensure logic holds across multiple digits."""
        assert int_to_mini_roman(number) == expected

    def test_output_is_lowercase(self):
        """Verify that the output is strictly lowercase."""
        result = int_to_mini_roman(426)
        assert result == result.lower()
        assert result.isupper() is False
        # Specific check against uppercase 'X' to ensure no capitalization
        assert 'X' not in int_to_mini_roman(10)

    @pytest.mark.parametrize("number", [1, 500, 1000])
    def test_type_consistency(self, number):
        """Ensure the function returns a string."""
        assert isinstance(int_to_mini_roman(number), str)

    @pytest.mark.parametrize("invalid_input, expected", [
        (0, ""),      # Algorithm results in empty string for 0
        (1001, "mi"),  # Algorithm handles > 1000 by appending 'm's
        (-5, ""),     # Negative numbers result in empty string
    ])
    def test_out_of_bounds(self, invalid_input, expected):
        """
        Test behavior outside the restricted range (1 <= num <= 1000).
        Ensures the function handles these gracefully based on current logic.
        """
        assert int_to_mini_roman(invalid_input) == expected