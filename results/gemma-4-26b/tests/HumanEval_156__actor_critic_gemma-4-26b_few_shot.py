
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

def test_provided_examples():
    """Tests the examples provided in the docstring."""
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),
])
def test_single_digits(number, expected):
    """Tests all single-digit Roman numerals (includes additive pattern 8)."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (80, 'lxxx'),  # Added to cover maximal additive pattern
    (90, 'xc'),
])
def test_tens(number, expected):
    """Tests key tens values including subtractive and maximal additive notation."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (800, 'dccc'), # Added to cover maximal additive pattern
    (900, 'cm'),
])
def test_hundreds(number, expected):
    """Tests key hundreds values including subtractive and maximal additive notation."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (38, 'xxxviii'),
    (44, 'xliv'),
    (99, 'xcix'),
    (444, 'cdxliv'),
    (999, 'cmxcix'),
])
def test_complex_numbers(number, expected):
    """Tests complex combinations of digits."""
    assert int_to_mini_roman(number) == expected

def test_boundaries():
    """Tests the boundary conditions of the allowed range [1, 1000]."""
    # Removed '1' as it is redundant with test_single_digits
    assert int_to_mini_roman(1000) == 'm'

@pytest.mark.parametrize("number", [0, -1, 1001, 5000])
def test_invalid_range(number):
    """Verifies that numbers outside the range [1, 1000] raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(number)

@pytest.mark.parametrize("number", [1.5, "10", None, [10]])
def test_invalid_types(number):
    """Verifies that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(number)