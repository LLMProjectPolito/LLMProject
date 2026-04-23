
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
from your_module import int_to_mini_roman  # Replace your_module

def test_basic_numbers():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"

def test_combined_numerals():
    assert int_to_mini_roman(6) == "vi"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(141) == "cxl"

def test_subtractive_cases():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"

def test_boundary_conditions():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_invalid_input_less_than_one():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_invalid_input_greater_than_one_thousand():
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)