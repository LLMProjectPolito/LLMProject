
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
    # Basic single digits
    (1, 'i'),
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),
    
    # Basic tens
    (10, 'x'),
    (20, 'xx'),
    (30, 'xxx'),
    (40, 'xl'),
    (50, 'l'),
    (60, 'lx'),
    (70, 'lxx'),
    (80, 'lxxx'),
    (90, 'xc'),
    
    # Basic hundreds
    (100, 'c'),
    (200, 'cc'),
    (300, 'ccc'),
    (400, 'cd'),
    (500, 'd'),
    (600, 'dc'),
    (700, 'dcc'),
    (800, 'dccc'),
    (900, 'cm'),
    
    # Boundary cases
    (1000, 'm'),
    
    # Examples provided in the docstring
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Complex combinations and subtractive notation
    (44, 'xliv'),
    (99, 'xcix'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
    (38, 'xxxviii'),
    (749, 'dxlix'),
    (944, 'cmxliv'),
])
def test_int_to_mini_roman_valid(number, expected):
    """Test that integers within the range 1-1000 are correctly converted to lowercase roman numerals."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("invalid_number", [0, -1, -100, 1001, 2000])
def test_int_to_mini_roman_out_of_bounds(invalid_number):
    """Test that integers outside the range 1-1000 raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(invalid_number)

@pytest.mark.parametrize("invalid_type", ["10", 10.5, None, [], {}])
def test_int_to_mini_roman_invalid_type(invalid_type):
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(invalid_type)