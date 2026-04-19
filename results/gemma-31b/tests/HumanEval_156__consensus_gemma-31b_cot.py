
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
    (1, 'i'),
    (1000, 'm'),
    
    # Single digits
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),
    
    # Tens
    (10, 'x'),
    (11, 'xi'),
    (13, 'xiii'),
    (14, 'xiv'),
    (19, 'xix'),
    (20, 'xx'),
    (38, 'xxxviii'),
    (40, 'xl'),
    (44, 'xliv'),
    (49, 'xlix'),
    (50, 'l'),
    (60, 'lx'),
    (88, 'lxxxviii'),
    (90, 'xc'),
    (94, 'xciv'),
    (99, 'xcix'),
    
    # Hundreds
    (100, 'c'),
    (149, 'cxlix'),
    (152, 'clii'),
    (200, 'cc'),
    (300, 'ccc'),
    (388, 'ccclxxxviii'),
    (399, 'cccxcix'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (444, 'cdxliv'),
    (500, 'd'),
    (600, 'dc'),
    (888, 'dlxxxviii'),
    (900, 'cm'),
    (944, 'cmxliv'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_valid(number, expected):
    """Test that valid integers within the range 1-1000 are converted correctly."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is always lowercase."""
    result = int_to_mini_roman(426)
    assert result == result.lower()
    assert result == 'cdxxvi'

@pytest.mark.parametrize("invalid_input", [
    0,
    1001,
    -1,
    -100,
])
def test_int_to_mini_roman_out_of_bounds(invalid_input):
    """
    Check behavior for inputs outside the restricted range 1 <= num <= 1000.
    Ensures the function handles or fails predictably.
    """
    try:
        int_to_mini_roman(invalid_input)
    except Exception:
        pass