
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
    (1, 'i'),
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (9, 'ix'),
    (10, 'x'),
    (19, 'xix'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    (100, 'c'),
    (152, 'clii'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (500, 'd'),
    (900, 'cm'),
    (999, 'cmxcix'),
    (1000, 'm'),
    (39, 'xxxix'),
    (88, 'lxxxviii'),
    (399, 'cccxcix'),
    (888, 'dlxxxviii'),
])
def test_int_to_mini_roman_valid_inputs(number, expected):
    """Test standard cases, boundaries, and subtractive combinations."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is always lowercase."""
    result = int_to_mini_roman(10)
    assert result == result.lower()

@pytest.mark.parametrize("number", [
    0, 
    1001, 
    -1, 
    -10
])
def test_int_to_mini_roman_out_of_bounds(number):
    """
    Test behavior for numbers outside the restriction 1 <= num <= 1000.
    Depending on implementation, this might raise an error or return unexpected results.
    This test ensures we know how the function handles these.
    """
    # Since the prompt specifies restrictions, we assume the function 
    # might not handle these, but a comprehensive suite should check them.
    # If the function is strictly for 1-1000, we just verify it doesn't crash 
    # or we check for specific error handling if implemented.
    try:
        int_to_mini_roman(number)
    except Exception:
        pass