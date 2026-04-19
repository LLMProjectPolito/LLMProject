
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

# Assuming the function is in a file named solution.py
# from solution import int_to_mini_roman

def int_to_mini_roman(number):
    """
    Implementation provided for the sake of making the test suite runnable.
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

@pytest.mark.parametrize("number, expected", [
    # Provided Examples
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Boundary Values
    (1, 'i'),
    (1000, 'm'),
    
    # Single Digits
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
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    
    # Hundreds
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    
    # Complex Combinations
    (39, 'xxxix'),
    (44, 'xliv'),
    (88, 'lxxxviii'),
    (99, 'xcix'),
    (399, 'cccxcix'),
    (444, 'cdxliv'),
    (888, 'dlxxxviii'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_valid(number, expected):
    """Test valid inputs within the range 1 <= num <= 1000."""
    assert int_to_mini_roman(number) == expected

def test_int_to_mini_roman_lowercase():
    """Ensure the output is always lowercase."""
    result = int_to_mini_roman(426)
    assert result == result.lower()

@pytest.mark.parametrize("invalid_input", [
    0, 
    1001, 
    -1, 
    -100
])
def test_int_to_mini_roman_out_of_bounds(invalid_input):
    """
    Test how the function handles inputs outside the specified range.
    Depending on requirements, this might raise an error or return an empty string.
    """
    # If the function is strictly for 1-1000, we check if it handles these gracefully
    # or if we expect a specific behavior. Here we just ensure it doesn't crash 
    # unless the spec requires an exception.
    try:
        result = int_to_mini_roman(invalid_input)
        # If it returns something for 0, it should be an empty string or handled
        if invalid_input <= 0:
            assert result == ""
    except Exception as e:
        pytest.fail(f"Function crashed on out-of-bounds input {invalid_input}: {e}")