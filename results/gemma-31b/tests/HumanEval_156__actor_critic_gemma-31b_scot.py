
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

# The function int_to_mini_roman is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("number, expected", [
    # Boundary Cases
    (1, 'i'),
    (1000, 'm'),
    
    # Provided Examples
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Subtractive Cases
    (4, 'iv'),
    (9, 'ix'),
    (40, 'xl'),
    (90, 'xc'),
    (400, 'cd'),
    (900, 'cm'),
    
    # Additive/Simple Cases
    (5, 'v'),
    (10, 'x'),
    (50, 'l'),
    (100, 'c'),
    (500, 'd'),
    (3, 'iii'),
    (30, 'xxx'),
    (300, 'ccc'),
    
    # Complex Combinations
    (8, 'viii'),
    (80, 'lxxx'),
    (800, 'dccc'),
    (88, 'lxxxviii'),
    (888, 'dccclxxxviii'),
    (444, 'cdxliv'),
    (999, 'cmxcix'),
    (399, 'cccxcix'),
    (49, 'xlix'),
    (94, 'xciv'),
])
def test_int_to_mini_roman_valid_inputs(number, expected):
    """Test a wide range of valid inputs within the 1-1000 constraint."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number", [
    0, 
    -1, 
    -100, 
    1001, 
    2000
])
def test_int_to_mini_roman_out_of_range(number):
    """Ensure that numbers outside the 1-1000 range raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(number)

@pytest.mark.parametrize("invalid_input", [
    1.5, 
    "10", 
    "x", 
    None, 
    [], 
    {}
])
def test_int_to_mini_roman_invalid_types(invalid_input):
    """Ensure that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(invalid_input)