
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

@pytest.mark.parametrize("input_val, expected", [
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
])
def test_docstring_examples(input_val, expected):
    """Verify the examples provided in the function docstring."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (1, 'i'),
    (1000, 'm'),
])
def test_boundary_values(input_val, expected):
    """Verify the minimum and maximum constraints of the function."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (5, 'v'),
    (50, 'l'),
    (500, 'd'),
])
def test_base_units(input_val, expected):
    """Verify the fundamental single-unit Roman numeral mappings."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (4, 'iv'),
    (9, 'ix'),
    (40, 'xl'),
    (90, 'xc'),
    (400, 'cd'),
    (900, 'cm'),
])
def test_subtraction_logic(input_val, expected):
    """Verify that subtractive notation (e.g., IV, XC) is handled correctly."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (3, 'iii'),
    (30, 'xxx'),
    (300, 'ccc'),
    (333, 'cccxxxiii'),
])
def test_repetition_logic(input_val, expected):
    """Verify that repeating characters (up to 3 times) are handled correctly."""
    assert int_to_mini_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    (8, 'viii'),
    (44, 'xliv'),
    (88, 'lxxxviii'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_complex_numbers(input_val, expected):
    """Verify complex numbers that combine subtraction and repetition rules."""
    assert int_to_mini_roman(input_val) == expected

def test_output_is_lowercase():
    """Ensure the output is always lowercase for all valid inputs in the range."""
    for i in range(1, 1001):
        result = int_to_mini_roman(i)
        assert result == result.lower(), f"Output for {i} was not lowercase: {result}"

@pytest.mark.parametrize("input_val", [
    0,
    -1,
    -100,
    1001,
    5000,
])
def test_out_of_range_errors(input_val):
    """Verify that values outside the 1-1000 range raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(input_val)

@pytest.mark.parametrize("input_val", [
    1.5,
    "10",
    None,
    [10],
])
def test_type_errors(input_val):
    """Verify that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(input_val)