
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

# Assuming the function is in a file named solution.py
# from solution import int_to_mini_roman

@pytest.mark.parametrize("input_val, expected", [
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
])
def test_provided_examples(input_val, expected):
    """Verify the examples provided in the docstring."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (1, 'i'),          # Minimum boundary
    (1000, 'm'),       # Maximum boundary
    (5, 'v'),          # Single digit mid-point
    (10, 'x'),         # Power of 10
    (50, 'l'),         # Mid-point
    (100, 'c'),        # Power of 10
    (500, 'd'),        # Mid-point
])
def test_boundaries_and_single_symbols(input_val, expected):
    """Test the absolute limits of the allowed range and single-character symbols."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (4, 'iv'),         # Subtractive 1
    (9, 'ix'),         # Subtractive 1
    (40, 'xl'),        # Subtractive 10
    (90, 'xc'),        # Subtractive 10
    (400, 'cd'),       # Subtractive 100
    (900, 'cm'),       # Subtractive 100
])
def test_subtractive_notation(input_val, expected):
    """
    Test the 'subtractive' rules (e.g., IV instead of IIII). 
    This is the most common area for logic errors in Roman numeral converters.
    """
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (3, 'iii'),        # Max repetition of I
    (30, 'xxx'),       # Max repetition of X
    (300, 'ccc'),      # Max repetition of C
    (8, 'viii'),       # Combination of repetition and single symbol
    (88, 'lxxxviii'),  # Complex repetition
    (888, 'dccclxxxviii'), # Deeply nested repetition
])
def test_repetition_logic(input_val, expected):
    """Test cases where symbols are repeated multiple times."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (399, 'cccxcix'),
    (444, 'cdxliv'),
    (999, 'cmxcix'),
    (949, 'cmxlix'),
])
def test_complex_combinations(input_val, expected):
    """Test complex numbers that combine multiple subtractive and additive rules."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("invalid_input", [
    (0),        # Below range
    (-1),       # Negative
    (1001),     # Above range
    (1000.5),   # Float (not an integer)
    ("19"),     # String (wrong type)
    (None),     # NoneType
])
def test_invalid_inputs(invalid_input):
    """
    Blue Team Strategy: Test how the function handles inputs outside the contract.
    A robust function should raise ValueError for out-of-range numbers 
    and TypeError for incorrect types.
    """
    with pytest.raises((ValueError, TypeError)):
        int_to_mini_roman(invalid_input)

def test_case_sensitivity():
    """Ensure the output is strictly lowercase as per requirements."""
    result = int_to_mini_roman(10)
    assert result == result.lower(), f"Expected lowercase output, got '{result}'"