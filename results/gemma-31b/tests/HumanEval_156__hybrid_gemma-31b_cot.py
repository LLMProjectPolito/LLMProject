
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
    # Boundary values
    (1, 'i'),
    (1000, 'm'),
    
    # Basic single digit values
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),
    
    # Tens boundaries and subtractive cases
    (10, 'x'),
    (11, 'xi'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    (99, 'xcix'),
    
    # Hundreds boundaries and subtractive cases
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    
    # Provided examples and complex combinations
    (19, 'xix'),
    (39, 'xxxix'),
    (44, 'xliv'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    (399, 'cccxcix'),
    (444, 'cdxliv'),
    (666, 'dclxvi'),
    (777, 'dcclxxvii'),
    (789, 'dcclxxxix'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_values(number, expected):
    """Test a comprehensive set of integers within the range [1, 1000], 
    including boundaries, subtractive rules, and complex combinations.
    """
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number", [1, 4, 9, 40, 90, 400, 666, 900, 1000])
def test_int_to_mini_roman_lowercase(number):
    """Ensure the output is always lowercase regardless of the input value."""
    result = int_to_mini_roman(number)
    assert result == result.lower()
    assert not any(char.isupper() for char in result)

@pytest.mark.parametrize("number", [1, 500, 1000])
def test_int_to_mini_roman_type(number):
    """Ensure the return type is always a string."""
    assert isinstance(int_to_mini_roman(number), str)

def test_int_to_mini_roman_non_empty():
    """Ensure that valid inputs within range do not produce empty strings."""
    assert len(int_to_mini_roman(1)) > 0
    assert len(int_to_mini_roman(1000)) > 0