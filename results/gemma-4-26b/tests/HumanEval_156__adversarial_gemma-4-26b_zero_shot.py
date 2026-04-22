
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

# Assuming the function is imported from the target module
# from solution import int_to_mini_roman

class TestIntToMiniRoman:
    """
    Blue Team QA Suite for int_to_mini_roman.
    Tests boundary conditions, Roman numeral subtraction logic, 
    case sensitivity, and input validation.
    """

    @pytest.mark.parametrize("number, expected", [
        # Boundary Values
        (1, "i"),
        (1000, "m"),
        
        # Single Digits & Subtraction Rules (1-10)
        (2, "ii"),
        (3, "iii"),
        (4, "iv"),
        (5, "v"),
        (6, "vi"),
        (8, "viii"),
        (9, "ix"),
        (10, "x"),
        
        # Tens (Subtractive notation)
        (40, "xl"),
        (50, "l"),
        (90, "xc"),
        
        # Hundreds (Subtractive notation)
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        
        # Complex Combinations (Provided Examples)
        (19, "xix"),
        (152, "clii"),
        (426, "cdxxvi"),
        
        # High Complexity Edge Cases
        (399, "cccxcix"),
        (444, "cdxliv"),
        (888, "dccclxxxviii"),
        (999, "cmxcix"),
    ])
    def test_valid_conversions(self, number, expected):
        """Verifies that correct Roman numeral strings are returned for valid inputs."""
        assert int_to_mini_roman(number) == expected

    def test_output_format(self):
        """Ensures the output is strictly lowercase as per the requirement."""
        result = int_to_mini_roman(1000)
        assert result == result.lower(), f"Expected lowercase output, but got '{result}'"
        assert result.isalpha(), "Output should only contain alphabetic characters"

    @pytest.mark.parametrize("out_of_bounds", [0, -1, -100, 1001, 5000])
    def test_range_constraints(self, out_of_bounds):
        """
        Verifies that the function enforces the restriction 1 <= num <= 1000.
        A robust implementation should raise a ValueError for out-of-bounds integers.
        """
        with pytest.raises(ValueError):
            int_to_mini_roman(out_of_bounds)

    @pytest.mark.parametrize("bad_input", [1.5, "10", None, [5], {"num": 10}])
    def test_type_safety(self, bad_input):
        """
        Verifies that the function handles non-integer inputs gracefully.
        A robust implementation should raise a TypeError.
        """
        with pytest.raises(TypeError):
            int_to_mini_roman(bad_input)

    def test_large_input_stability(self):
        """Checks if the function handles extremely large integers without crashing (should raise ValueError)."""
        with pytest.raises(ValueError):
            int_to_mini_roman(10**10)