import pytest
import math


# Focus: Boundary Values
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
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

@pytest.mark.parametrize("number", [1, 1000])
def test_int_to_mini_roman_boundary_1_and_1000(number):
    """Test the function with the minimum and maximum allowed input values."""
    assert int_to_mini_roman(number) == ('i' if number == 1 else 'm')

@pytest.mark.parametrize("number", [4, 9, 40, 90, 400, 900])
def test_int_to_mini_roman_boundary_subtractive_cases(number):
    """Test the function with boundary values that use subtractive notation."""
    assert int_to_mini_roman(number) == ('iv' if number == 4 else ('ix' if number == 9 else ('xl' if number == 40 else ('xc' if number == 90 else ('cd' if number == 400 else 'cm')))))

# Focus: Equivalence Partitioning
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
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

@pytest.mark.parametrize("number, expected", [
    (1, "i"),
    (5, "v"),
    (10, "x"),
    (50, "l"),
    (100, "c"),
    (500, "d"),
    (1000, "m"),
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm"),
])
def test_equivalence_partitions_boundary_values():
    """Tests boundary values for equivalence partitions."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (19, "xix"),
    (44, "xliv"),
    (99, "xcix"),
    (149, "cxlix"),
    (499, "cdxcix"),
    (999, "cmxcix"),
])
def test_equivalence_partitions_representative_values():
    """Tests representative values within equivalence partitions."""
    assert int_to_mini_roman(number) == expected

# Focus: Logic Branches
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
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

@pytest.mark.parametrize("number, expected", [
    (1, "i"),
    (4, "iv"),
    (5, "v"),
    (9, "ix"),
    (10, "x"),
    (40, "xl"),
    (50, "l"),
    (90, "xc"),
    (100, "c"),
    (400, "cd"),
    (500, "d"),
    (900, "cm"),
    (1000, "m"),
])
def test_boundary_values(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (19, "xix"),
    (44, "xliv"),
    (99, "xcix"),
    (149, "cxlix"),
    (499, "cdxcix"),
    (944, "cmxliv"),
])
def test_combinations(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number", [
    152,
    426,
    789,
    399,
    888
])
def test_general_cases(number):
    result = int_to_mini_roman(number)
    assert isinstance(result, str)
    assert 1 <= number <= 1000