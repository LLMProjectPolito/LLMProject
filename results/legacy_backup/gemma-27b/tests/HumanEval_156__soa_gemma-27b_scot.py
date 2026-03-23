import pytest

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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function converts an integer between 1 and 1000 to its mini-roman numeral representation (lowercase).
# We need to test:
# - Valid inputs within the range [1, 1000]
# - Edge cases: 1, 3, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000
# - Combinations of these values
# - Inputs close to the boundaries (e.g., 2, 999)
# - Invalid inputs (outside the range) - although the problem statement doesn't explicitly require this, it's good practice.

# STEP 2: PLAN - List test functions names and scenarios.
# - test_valid_input: Tests valid inputs within the range [1, 1000] with various combinations.
# - test_edge_cases: Tests the edge cases (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000).
# - test_boundary_values: Tests inputs close to the boundaries (e.g., 2, 999).
# - test_invalid_input: Tests inputs outside the range [1, 1000] (optional, but good practice).

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("input_num, expected_output", [
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
    (14, "xiv"),
    (15, "xv"),
    (16, "xvi"),
    (19, "xix"),
    (20, "xx"),
    (39, "xxxix"),
    (40, "xl"),
    (41, "xli"),
    (44, "xliv"),
    (45, "xlv"),
    (49, "xlix"),
    (50, "l"),
    (51, "li"),
    (55, "lv"),
    (59, "lix"),
    (60, "lx"),
    (64, "lxiv"),
    (70, "lxx"),
    (80, "lxxx"),
    (85, "lxxxv"),
    (90, "xc"),
    (91, "xci"),
    (94, "xciv"),
    (95, "xcv"),
    (99, "xcix"),
    (100, "c"),
    (101, "ci"),
    (149, "cxlix"),
    (150, "cl"),
    (152, "clii"),
    (199, "cxcix"),
    (200, "cc"),
    (300, "ccc"),
    (400, "cd"),
    (401, "cdi"),
    (444, "cdxliv"),
    (450, "cdl"),
    (500, "d"),
    (501, "di"),
    (555, "dlv"),
    (600, "dc"),
    (700, "dcc"),
    (800, "dccc"),
    (900, "cm"),
    (901, "cmi"),
    (949, "cmxlix"),
    (950, "cml"),
    (999, "cmxcix"),
    (1000, "m"),
])
def test_valid_input(input_num, expected_output):
    assert int_to_mini_roman(input_num) == expected_output

def test_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(1000) == "m"

def test_boundary_values():
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(998) == "cmxcviii"
    assert int_to_mini_roman(999) == "cmxcix"

@pytest.mark.parametrize("input_num", [0, 1001])
def test_invalid_input(input_num):
    with pytest.raises(TypeError):
        int_to_mini_roman(input_num)