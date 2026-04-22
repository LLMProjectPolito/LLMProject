
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

# Assuming the function is imported from your module
# from your_module import int_to_mini_roman

@pytest.mark.parametrize("num, expected", [
    # --- Boundary Cases ---
    pytest.param(1, "i", id="boundary_min"),
    pytest.param(1000, "m", id="boundary_max"),

    # --- Single Digits (Units) ---
    pytest.param(2, "ii", id="units_2"),
    pytest.param(3, "iii", id="units_3"),
    pytest.param(4, "iv", id="units_4_subtractive"),
    pytest.param(5, "v", id="units_5"),
    pytest.param(6, "vi", id="units_6"),
    pytest.param(7, "vii", id="units_7"),
    pytest.param(8, "viii", id="units_8"),
    pytest.param(9, "ix", id="units_9_subtractive"),

    # --- Tens Place ---
    pytest.param(10, "x", id="tens_10"),
    pytest.param(20, "xx", id="tens_20"),
    pytest.param(30, "xxx", id="tens_30"),
    pytest.param(40, "xl", id="tens_40_subtractive"),
    pytest.param(50, "l", id="tens_50"),
    pytest.param(60, "lx", id="tens_60"),
    pytest.param(70, "lxx", id="tens_70"),
    pytest.param(80, "lxxx", id="tens_80"),
    pytest.param(90, "xc", id="tens_90_subtractive"),

    # --- Hundreds Place ---
    pytest.param(100, "c", id="hundreds_100"),
    pytest.param(200, "cc", id="hundreds_200"),
    pytest.param(300, "ccc", id="hundreds_300"),
    pytest.param(400, "cd", id="hundreds_400_subtractive"),
    pytest.param(500, "d", id="hundreds_500"),
    pytest.param(600, "dc", id="hundreds_600"),
    pytest.param(700, "dcc", id="hundreds_700"),
    pytest.param(800, "dccc", id="hundreds_800"),
    pytest.param(900, "cm", id="hundreds_900_subtractive"),

    # --- Complex Combinations & Docstring Examples ---
    pytest.param(19, "xix", id="example_19"),
    pytest.param(38, "xxxviii", id="complex_38"),
    pytest.param(88, "lxxxviii", id="complex_88"),
    pytest.param(152, "clii", id="example_152"),
    pytest.param(388, "ccclxxxviii", id="complex_388"),
    pytest.param(426, "cdxxvi", id="example_426"),
    pytest.param(444, "cdxliv", id="complex_444_multi_subtractive"),
    pytest.param(777, "dccxxvii", id="complex_777"),
    pytest.param(999, "cmxcix", id="complex_999_near_max"),
])
def test_int_to_mini_roman_conversions(num, expected):
    """Tests a comprehensive range of valid integer-to-roman conversions."""
    assert int_to_mini_roman(num) == expected


def test_int_to_mini_roman_properties():
    """
    Property-based tests to ensure structural requirements:
    1. Output is always a string.
    2. Output is always lowercase.
    """
    test_values = [1, 10, 44, 99, 500, 1000]
    for val in test_values:
        result = int_to_mini_roman(val)
        
        # Check type
        assert isinstance(result, str), f"Value {val} should return a string"
        
        # Check case sensitivity
        assert result == result.lower(), f"Value {val} returned non-lowercase string: {result}"