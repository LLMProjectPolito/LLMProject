
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    result = ''
    while number > 0:
        remainder = number % 10
        if remainder == 1:
            result += 'i'
            number //= 10
        elif remainder == 2:
            result += 'ii'
            number //= 10
        elif remainder == 3:
            result += 'iii'
            number //= 10
        elif remainder == 4:
            result += 'iv'
            number //= 10
        elif remainder == 5:
            result += 'v'
            number //= 10
        elif remainder == 6:
            result += 'vi'
            number //= 10
        elif remainder == 7:
            result += 'vii'
            number //= 10
        elif remainder == 8:
            result += 'viii'
            number //= 10
        elif remainder == 9:
            result += 'ix'
            number //= 10
        else:
            raise ValueError("Invalid remainder")

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
        (14, "xiv"),
        (16, "xvi"),
        (19, "xix"),
        (20, "xx"),
        (24, "xxiv"),
        (29, "xxix"),
        (30, "xxx"),
        (34, "xxxiv"),
        (40, "xl"),
        (44, "xliv"),
        (49, "xlix"),
        (50, "l"),
        (54, "liv"),
        (59, "lxix"),
        (60, "lxx"),
        (64, "lxiv"),
        (69, "lxix"),
        (70, "lxx"),
        (74, "lxxiv"),
        (79, "lxxix"),
        (80, "lviii"),
        (84, "lxxxiv"),
        (89, "lxxxix"),
        (90, "x"),
        (94, "xliiv"),
        (99, "xciii"),
        (100, "c"),
        (104, "civ"),
        (109, "ciix"),
        (110, "cii"),
        (144, "civil"),
        (149, "xivix"),
        (150, "xli"),
        (152, "clii"),
        (153, "cliii"),
        (160, "lx"),
        (164, "lxiv"),
        (169, "xciix"),
        (170, "xcii"),
        (174, "lxiv"),
        (179, "xciix"),
        (180, "xviii"),
        (184, "xliiiv"),
        (189, "xciix"),
        (190, "xci"),
        (192, "xcii"),
        (199, "xciixxix"),
        (200, "cc"),
        (204, "cciv"),
        (209, "ccix"),
        (210, "ccx"),
        (214, "ccxiv"),
        (219, "ccxix"),
        (220, "ccxx"),
        (224, "ccxxiv"),
        (229, "ccxxix"),
        (230, "ccxxx"),
        (234, "ccxxxiv"),
        (239, "ccxxxix"),
        (240, "ccc"),
        (244, "ccciv"),
        (249, "cccix"),
        (250, "cccx"),
        (254, "cccxiv"),
        (259, "cccxix"),
        (260, "cccxx"),
        (264, "cccxxiv"),
        (269, "cccxxix"),
        (270, "cccxxx"),
        (274, "cccxxiv"),
        (279, "cccxxix"),
        (280, "cccxxx"),
        (284, "cccxxxiv"),
        (289, "cccxxxix"),
        (290, "cccxl"),
        (294, "cccxliv"),
        (299, "cccxciix"),
        (300, "ccc"),
        (304, "ccciv"),
        (309, "cccix"),
        (310, "ccxc"),
        (314, "cccxiv"),
        (319, "cccxix"),
        (320, "cccxx"),
        (324, "cccxxiv"),
        (329, "cccxxix"),
        (330, "cccxxx"),
        (334, "cccxxxiv"),
        (339, "cccxxxix"),
        (340, "cccc"),
        (344, "cccciv"),
        (349, "ccccix"),
        (350, "ccccx"),
        (354, "ccccxiv"),
        (359, "ccccxix"),
        (360, "ccccxx"),
        (364, "ccccxxiv"),
        (369, "ccccxxix"),
        (370, "ccccxxx"),
        (374, "ccccxxxiv"),
        (379, "ccccxxix"),
        (380, "ccccxxx"),
        (384, "ccccxxxiv"),
        (389, "ccccxxxix"),
        (390, "ccccxl"),
        (394, "ccccxliv"),
        (399, "ccccxciix"),
        (400, "cccc"),
        (404, "cccciv"),
        (409, "ccccix"),
        (410, "ccccxc"),
        (414, "ccccxiv"),
        (419, "ccccxix"),
        (420, "ccccxx"),
        (424, "ccccxxiv"),
        (429, "ccccxxix"),
        (430, "ccccxxx"),
        (434, "ccccxxxiv"),
        (439, "ccccxxxix"),
        (440, "ccccxl"),
        (444, "ccccxliv"),
        (449, "ccccxciix"),
        (450, "ccccxl"),
        (454, "ccccxliv"),
        (459, "ccccxlix"),
        (460, "ccccxlx"),
        (464, "ccccxlxiv"),
        (469, "ccccxlix"),
        (470, "ccccxli"),
        (474, "ccccxliv