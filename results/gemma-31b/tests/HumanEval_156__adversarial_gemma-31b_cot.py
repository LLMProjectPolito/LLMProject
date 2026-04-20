
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
    # Lower boundary
    (1, 'i'),
    # Upper boundary
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
    (19, 'xix'),
    (40, 'xl'),
    (49, 'xlix'),
    (50, 'l'),
    (59, 'lix'),
    (90, 'xc'),
    (99, 'xcix'),
    # Hundreds
    (100, 'c'),
    (152, 'clii'),
    (400, 'cd'),
    (426, 'cdxxvi'),
    (444, 'cdxliv'),
    (500, 'd'),
    (900, 'cm'),
    (944, 'cmxliv'),
    (999, 'cmxcix'),
    # Complex combinations
    (388, 'ccclxxxviii'),
    (888, 'dccclxxxviii'),
    (777, 'dlxxvii'),
    (666, 'dcmlxvi'), # Wait, 666 is dclxvi
])
def test_int_to_mini_roman_values(number, expected):
    """Test a wide range of valid inputs within the constraint 1 <= num <= 1000."""
    # Correcting the 666 case in the parametrization logic internally
    if number == 666:
        expected = 'dclxvi'
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is strictly lowercase."""
    result = int_to_mini_roman(19)
    assert result == result.lower()
    assert result != result.upper()

def test_int_to_mini_roman_type():
    """Ensure the output is a string."""
    assert isinstance(int_to_mini_roman(1), str)

@pytest.mark.parametrize("number", [
    1, 10, 100, 1000, 4, 9, 40, 90, 400, 900
])
def test_int_to_mini_roman_idempotency(number):
    """Ensure consistent results for key Roman numeral milestones."""
    first_call = int_to_mini_roman(number)
    second_call = int_to_mini_roman(number)
    assert first_call == second_call

# Note: The problem specifies 1 <= num <= 1000. 
# Testing outside this range is typically for 'Stress Testing' or 'Negative Testing'.
# Depending on implementation, these might raise errors or return unexpected results.