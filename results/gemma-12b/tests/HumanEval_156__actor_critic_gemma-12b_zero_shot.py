
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

MAX_VALUE = 1000  # Define the maximum allowed value


@pytest.mark.parametrize(
    "number, expected_roman",
    [
        (1, "i"),
        (2, "ii"),
        (3, "iii"),
        (4, "iv"),
        (5, "v"),
        (6, "vi"),
        (7, "vii"),
        (8, "viii"),
        (9, "ix"),
        (10, "x"),
        (11, "xi"),
        (19, "xix"),
        (20, "xx"),
        (39, "xxxix"),
        (40, "xl"),
        (41, "xli"),
        (49, "xlix"),
        (50, "l"),
        (51, "li"),
        (90, "xc"),
        (91, "xci"),
        (100, "c"),
        (101, "ci"),
        (149, "cxlix"),
        (150, "cl"),
        (152, "clii"),
        (199, "xciix"),
        (200, "cc"),
        (399, "cccxciix"),
        (400, "cd"),
        (426, "cdxxvi"),
        (444, "cdxliv"),
        (499, "cdxciix"),
        (500, "d"),
        (501, "di"),
        (900, "cm"),
        (901, "cmi"),
        (999, "cmxciix"),
        (1000, "m"),
    ],
)
def test_valid_input(number, expected_roman):
    """Tests valid integer inputs and their corresponding Roman numeral representations."""
    assert int_to_mini_roman(number) == expected_roman


def test_invalid_input():
    """Tests invalid input types and boundary conditions."""
    with pytest.raises(ValueError):
        int_to_mini_roman(0)  # Test zero
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)  # Test above maximum allowed value
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)  # Test negative number
    with pytest.raises(TypeError):
        int_to_mini_roman("abc")  # Test invalid type (string)
    with pytest.raises(TypeError):
        int_to_mini_roman(None)  # Test invalid type (None)


def test_max_value():
    """Tests the maximum allowed value (1000)."""
    assert int_to_mini_roman(MAX_VALUE) == "m"