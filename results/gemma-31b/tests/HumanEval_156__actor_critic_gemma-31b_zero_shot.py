
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
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if not (1 <= number <= 1000):
        raise ValueError("Input must be between 1 and 1000 inclusive.")

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
    # Examples provided in the prompt
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
    
    # Boundary cases
    (1, 'i'),
    (1000, 'm'),
    
    # Single digit cases
    (2, 'ii'),
    (3, 'iii'),
    (4, 'iv'),
    (5, 'v'),
    (6, 'vi'),
    (7, 'vii'),
    (8, 'viii'),
    (9, 'ix'),
    
    # Tens cases
    (10, 'x'),
    (40, 'xl'),
    (50, 'l'),
    (90, 'xc'),
    
    # Hundreds cases
    (100, 'c'),
    (400, 'cd'),
    (500, 'd'),
    (900, 'cm'),
    
    # Complex combinations
    (39, 'xxxix'),
    (44, 'xliv'),
    (88, 'lxxxviii'),
    (99, 'xcix'),
    (399, 'cccxcix'),
    (888, 'dccclxxxviii'),
    (999, 'cmxcix'),
])
def test_int_to_mini_roman_valid(number, expected):
    """Test valid inputs within the range 1 <= num <= 1000."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("out_of_bounds_input", [
    0, 
    -1, 
    1001,
    2000
])
def test_int_to_mini_roman_out_of_bounds(out_of_bounds_input):
    """Test that inputs outside the range 1-1000 raise a ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(out_of_bounds_input)

@pytest.mark.parametrize("invalid_type", [
    "10", 
    10.5, 
    None, 
    [], 
    {}
])
def test_int_to_mini_roman_invalid_types(invalid_type):
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(invalid_type)