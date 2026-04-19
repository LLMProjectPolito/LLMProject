
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
    # Examples provided in docstring
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Boundary values
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
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    
    # Hundreds
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    
    # Complex combinations
    (39, 'xxxix'),
    (44, 'xliv'),
    (88, 'lxxxviii'),
    (99, 'xcix'),
    (399, 'cccxcix'),
    (444, 'cdxliv'),
    (888, 'dlxxxviii'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_valid_inputs(number, expected):
    """Test that valid integers within the range 1-1000 are converted correctly to lowercase roman numerals."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is always lowercase."""
    result = int_to_mini_roman(1000)
    assert result == result.lower()
    assert result == 'm'