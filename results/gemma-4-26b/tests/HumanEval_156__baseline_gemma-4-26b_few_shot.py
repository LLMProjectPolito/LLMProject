
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

@pytest.mark.parametrize("number, expected", [
    # Boundary cases
    (1, "i"),
    (1000, "m"),
    
    # Single digits and basic units
    (2, "ii"),
    (3, "iii"),
    (4, "iv"),
    (5, "v"),
    (6, "vi"),
    (8, "viii"),
    (9, "ix"),
    
    # Tens
    (10, "x"),
    (14, "xiv"),
    (19, "xix"),
    (20, "xx"),
    (40, "xl"),
    (49, "xlix"),
    (50, "l"),
    (90, "xc"),
    
    # Hundreds
    (100, "c"),
    (152, "clii"),
    (400, "cd"),
    (426, "cdxxvi"),
    (500, "d"),
    (900, "cm"),
    
    # Complex combinations
    (399, "cccxcix"),
    (888, "dccclxxxviii"),
    (999, "cmxcix"),
])
def test_int_to_mini_roman_valid_inputs(number, expected):
    """Tests various valid integers within the range 1-1000."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_docstring_examples():
    """Explicitly verifies the examples provided in the docstring."""
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'