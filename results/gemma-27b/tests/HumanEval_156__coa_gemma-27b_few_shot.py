
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

def test_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_boundary_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_boundary_4():
    assert int_to_mini_roman(4) == 'iv'

def test_boundary_9():
    assert int_to_mini_roman(9) == 'ix'

def test_boundary_40():
    assert int_to_mini_roman(40) == 'xl'

def test_boundary_90():
    assert int_to_mini_roman(90) == 'xc'

def test_boundary_400():
    assert int_to_mini_roman(400) == 'cd'

def test_boundary_900():
    assert int_to_mini_roman(900) == 'cm'

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
def test_equivalence_partitions_boundary(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (3, "iii"),
    (6, "vi"),
    (7, "vii"),
    (8, "viii"),
    (11, "xi"),
    (12, "xii"),
    (13, "xiii"),
    (14, "xiv"),
    (15, "xv"),
    (16, "xvi"),
    (17, "xvii"),
    (18, "xviii"),
    (20, "xx"),
    (30, "xxx"),
    (40, "xl"),
    (50, "l"),
    (60, "lx"),
    (70, "lxx"),
    (80, "lxxx"),
    (90, "xc"),
    (100, "c"),
    (200, "cc"),
    (300, "ccc"),
    (400, "cd"),
    (500, "d"),
    (600, "dc"),
    (700, "dcc"),
    (800, "dccc"),
    (900, "cm"),
    (1000, "m")
])
def test_equivalence_partitions_typical(number, expected):
    assert int_to_mini_roman(number) == expected

# Focus: Logic Branches
import pytest

def test_int_to_mini_roman_single_digit():
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_multiple_digits():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(99) == 'xcix'

def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'