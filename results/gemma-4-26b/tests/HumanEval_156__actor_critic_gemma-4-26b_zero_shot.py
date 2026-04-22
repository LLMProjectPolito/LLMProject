
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

# The function int_to_mini_roman is assumed to be defined in the scope 
# or imported from the module being tested.

@pytest.mark.parametrize("number, expected", [
    # Docstring Examples
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),

    # Boundary Cases
    (1, 'i'),
    (1000, 'm'),

    # Single Digits & Subtractive Logic (Units)
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),

    # Tens & Subtractive Logic (Tens)
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),

    # Hundreds & Subtractive Logic (Hundreds)
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),

    # Complex Combinations
    (38, 'xxxviii'),
    (44, 'xliv'),
    (88, 'lxxxviii'),
    (99, 'xcix'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (949, 'cmxlix'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_valid_range(number, expected):
    """Tests a wide variety of valid integers within the 1-1000 range."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("invalid_input, expected_exception", [
    # Out of bounds (ValueError)
    (0, ValueError),
    (1001, ValueError),
    (-5, ValueError),
    
    # Invalid types (TypeError)
    (10.5, TypeError),
    ("10", TypeError),
    (None, TypeError),
])
def test_invalid_inputs(invalid_input, expected_exception):
    """
    Tests behavior for inputs outside the specified restriction (1 <= num <= 1000)
    or incorrect types, ensuring the correct exception type is raised.
    """
    with pytest.raises(expected_exception):
        int_to_mini_roman(invalid_input)