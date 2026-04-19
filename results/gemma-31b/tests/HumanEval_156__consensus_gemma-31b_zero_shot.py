
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
    # Tens and combinations
    (10, 'x'),
    (11, 'xi'),
    (19, 'xix'),
    (20, 'xx'),
    (37, 'xxxvii'),
    (38, 'xxxviii'),
    (40, 'xl'),
    (44, 'xliv'),
    (49, 'xlix'),
    (50, 'l'),
    (88, 'lxxxviii'),
    (90, 'xc'),
    (94, 'xciv'),
    (99, 'xcix'),
    # Hundreds and combinations
    (100, 'c'),
    (152, 'clii'),
    (399, 'cccxcix'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (444, 'cdxliv'),
    (500, 'd'),
    (888, 'dccclxxxviii'),
    (900, 'cm'),
    (999, 'cmxcix'),
    (1000, 'm'),
])
def test_int_to_mini_roman_correctness(number, expected):
    """Test that integers are correctly converted to lowercase roman numerals."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_type():
    """Ensure the return type is always a string."""
    result = int_to_mini_roman(10)
    assert isinstance(result, str)

def test_int_to_mini_roman_lowercase():
    """Ensure the output is strictly lowercase."""
    result = int_to_mini_roman(426)
    assert result == result.lower()
    assert result != result.upper()

@pytest.mark.parametrize("invalid_input", [0, 1001, -1])
def test_int_to_mini_roman_out_of_bounds(invalid_input):
    """
    Test behavior for inputs outside the specified range (1 <= num <= 1000).
    Ensures the function handles out-of-bounds inputs without crashing 
    unless an exception is explicitly intended.
    """
    try:
        int_to_mini_roman(invalid_input)
    except Exception:
        pass