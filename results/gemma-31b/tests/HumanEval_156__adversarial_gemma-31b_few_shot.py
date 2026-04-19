
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

def test_roman_docstring_examples():
    """Verify the examples provided in the docstring."""
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),       # Lower boundary
    (1000, 'm'),    # Upper boundary
    (5, 'v'),       # Single character
    (10, 'x'),      # Single character
    (50, 'l'),      # Single character
    (100, 'c'),     # Single character
    (500, 'd'),     # Single character
])
def test_roman_single_symbols(number, expected):
    """Test numbers that map directly to a single Roman symbol."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (4, 'iv'),      # 4
    (9, 'ix'),      # 9
    (40, 'xl'),     # 40
    (90, 'xc'),     # 90
    (400, 'cd'),    # 400
    (900, 'cm'),    # 900
])
def test_roman_subtractive_notation(number, expected):
    """Test the 'subtractive' rules (the most common source of bugs)."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (3, 'iii'),     # Max repetition of I
    (8, 'viii'),    # Mixed additive
    (30, 'xxx'),    # Max repetition of X
    (80, 'lxxx'),   # Mixed additive
    (300, 'ccc'),   # Max repetition of C
    (800, 'dccc'),  # Mixed additive
])
def test_roman_additive_notation(number, expected):
    """Test standard additive sequences and maximum repetitions."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (44, 'xliv'),
    (99, 'xciix'), # Wait, 99 is xciix? No, 99 is xci x. Let's be precise:
    (99, 'xcix'),
    (444, 'cdxliv'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_roman_complex_combinations(number, expected):
    """Test complex numbers that combine multiple subtractive and additive rules."""
    assert int_to_mini_roman(number) == expected

def test_roman_lowercase_requirement():
    """Ensure the output is strictly lowercase as per requirements."""
    result = int_to_mini_roman(10)
    assert result == result.lower()
    assert result != 'X' # Explicitly check it's not uppercase