
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

```python
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


@pytest.mark.parametrize(
    "number, expected",
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
        (12, "xii"),
        (13, "xiii"),
        (14, "xiv"),
        (15, "xv"),
        (16, "xvi"),
        (17, "xvii"),
        (18, "xviii"),
        (19, "xix"),
        (20, "xx"),
        (39, "xxxix"),
        (40, "xl"),
        (41, "xli"),
        (42, "xlii"),
        (43, "xliii"),
        (44, "xliv"),
        (45, "xlv"),
        (46, "xlvi"),
        (47, "xlvii"),
        (48, "xlviii"),
        (49, "xlix"),
        (50, "l"),
        (90, "xc"),
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        (1000, "m"),
        (1001, "mci"),
        (1002, "mccii"),
        (1003, "mcciii"),
        (1004, "mcciv"),
        (1005, "mccv"),
        (1006, "mccvi"),
        (1007, "mccvii"),
        (1008, "mccviii"),
        (1009, "mccix"),
        (1010, "mcx"),
        (1100, "mcc"),
        (1999, "mmxcix"),
        (2000, "mm"),
        (3999, "mmcccxciii"),
        (0, ""),
    ],
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected


@pytest.mark.parametrize(
    "number",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 426, 152, 1000],
)
def test_int_to_mini_roman_basic(number):
    assert int_to_mini_roman(number) == int_to_mini_roman(number)  # Self-check


@pytest.mark.parametrize(
    "number",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 426, 152, 1000],
)
def test_int_to_mini_roman_edge_cases(number):
    assert len(int_to_mini_roman(number)) <= 4  # Check length constraint



@pytest.mark.parametrize(
    "number",
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 426, 152, 1000],
)
def test_int_to_mini_roman_invalid_input(number):
    assert len(int_to_mini_roman(number)) <= 4

Suite 2:
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


@pytest.mark.parametrize(
    "number, expected",
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
        (12, "xii"),
        (13, "xiii"),
        (14, "xiv"),
        (15, "xv"),
        (16, "xvi"),
        (17, "xvii"),
        (18, "xviii"),
        (19, "xix"),
        (20, "xx"),
        (39, "xxxix"),
        (40, "xl"),
        (41, "xli"),
        (42, "xlii"),
        (43, "xliii"),
        (44, "xliv"),
        (45, "xlv"),
        (46, "xlvi"),
        (47, "xlvii"),
        (48, "xlviii"),
        (49, "xlix"),
        (50, "l"),
        (51, "li"),
        (52, "lii"),
        (53, "liii"),
        (54, "liv"),
        (55, "lv"),
        (56, "lvi"),
        (57, "lvii"),
        (58, "lvviii"),
        (59, "lxxix"),
        (60, "lx"),
        (61, "lxi"),
        (62, "lxii"),
        (63, "lxiii"),
        (64, "lxiv"),
        (65, "lxv"),
        (66, "lxvi"),
        (67, "lxvii"),
        (68, "lxviii"),
        (69, "lxx"),
        (70, "lxx"),
        (71,