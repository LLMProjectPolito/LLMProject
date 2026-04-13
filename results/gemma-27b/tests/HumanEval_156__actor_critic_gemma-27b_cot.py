
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

def test_int_to_mini_roman_basic_tens_hundreds():
    """Tests basic, tens, and hundreds roman numeral conversions."""
    pytest.param(1, 'i', id='basic_1'),
    pytest.param(10, 'x', id='basic_10'),
    pytest.param(20, 'xx', id='tens_20'),
    pytest.param(50, 'l', id='tens_50'),
    pytest.param(100, 'c', id='hundreds_100'),
    pytest.param(500, 'd', id='hundreds_500'),
    pytest.param(900, 'cm', id='hundreds_900')

@pytest.mark.parametrize(
    "input_num, expected_roman",
    [
        (19, 'xix'),
        (44, 'xliv'),
        (99, 'xcix'),
        (149, 'cxlix'),
        (444, 'cdxliv'),
        (944, 'cmxliv'),
        (152, 'clii'),
        (426, 'cdxxvi'),
        (888, 'dccclxxxviii'),
    ]
)
def test_int_to_mini_roman_combined(input_num, expected_roman):
    """Tests combined roman numeral conversions."""
    assert int_to_mini_roman(input_num) == expected_roman

def test_int_to_mini_roman_edge_cases():
    """Tests edge cases for 1000."""
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_maximum_value():
    """Tests the maximum allowed value (3999)."""
    assert int_to_mini_roman(3999) == 'mmmcmxcix'

def test_int_to_mini_roman_over_maximum_value():
    """Tests a value just over the maximum allowed value (4000)."""
    with pytest.raises(ValueError):
        int_to_mini_roman(4000)

def test_int_to_mini_roman_negative_input():
    """Tests negative input."""
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)

@pytest.mark.parametrize(
    "invalid_input",
    [
        1.5,
        "1",
    ]
)
def test_int_to_mini_roman_invalid_input(invalid_input):
    """Tests invalid input types (float and string)."""
    with pytest.raises(TypeError):
        int_to_mini_roman(invalid_input)

def test_int_to_mini_roman_zero_input():
    """Tests zero input."""
    with pytest.raises(ValueError):
        int_to_mini_roman(0)