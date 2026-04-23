
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

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000
    """
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]
    roman_num = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num

@pytest.mark.parametrize("input_val, expected", [
    # Boundary Cases
    (1, "i"),
    (1000, "m"),
    
    # Docstring/Provided Examples
    (19, "xix"),
    (152, "clii"),
    (426, "cdxxvi"),
    
    # Single Digit Cases
    (2, "ii"),
    (3, "iii"),
    (4, "iv"),
    (5, "v"),
    (6, "vi"),
    (7, "vii"),
    (8, "viii"),
    (9, "ix"),
    
    # Tens and Subtractive Notation (Tens)
    (10, "x"),
    (30, "xxx"),
    (40, "xl"),
    (50, "l"),
    (80, "lxxx"),
    (90, "xc"),
    
    # Hundreds and Subtractive Notation (Hundreds)
    (100, "c"),
    (300, "ccc"),
    (400, "cd"),
    (500, "d"),
    (800, "dccc"),
    (900, "cm"),
    
    # Complex Combinations
    (38, "xxxviii"),
    (44, "xliv"),
    (88, "lxxxviii"),
    (99, "xcix"),
    (399, "cccxcix"),
    (444, "cdxliv"),
    (499, "cdxcix"),
    (888, "dccclxxxviii"),
    (949, "cmxlix"),
    (999, "cmxcix"),
])
def test_int_to_mini_roman_correctness(input_val, expected):
    """
    Tests a comprehensive range of valid integers including boundaries, 
    single digits, subtractive notation, and complex combinations.
    """
    assert int_to_mini_roman(input_val) == expected

def test_output_format_integrity():
    """
    Ensures the output is always a lowercase string.
    """
    result = int_to_mini_roman(500)
    assert isinstance(result, str)
    assert result == result.lower()
    assert result == 'd'

@pytest.mark.parametrize("num, expected_char", [
    (1000, 'm'),
    (500, 'd'),
    (100, 'c'),
    (50, 'l'),
    (10, 'x'),
    (5, 'v'),
    (1, 'i'),
])
def test_roman_symbols_presence(num, expected_char):
    """
    Verify that specific numbers contain their expected base Roman characters.
    """
    result = int_to_mini_roman(num)
    assert expected_char in result

@pytest.mark.parametrize("invalid_input", [0, -5])
def test_out_of_bounds_low(invalid_input):
    """
    Verifies behavior for inputs below the minimum constraint (1).
    Based on current implementation, these return an empty string.
    """
    assert int_to_mini_roman(invalid_input) == ""

def test_out_of_bounds_high():
    """
    Verifies behavior for inputs above the maximum constraint (1000).
    Note: The current implementation processes numbers > 1000 by appending 'm'.
    """
    # 1001 should result in 'mi' based on current logic
    assert int_to_mini_roman(1001) == "mi"