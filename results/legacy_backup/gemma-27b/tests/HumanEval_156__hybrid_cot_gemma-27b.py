import pytest
from your_module import int_to_mini_roman  # Replace your_module

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
        (58, "lviii"),
        (89, "lxxxix"),
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
        (399, "cccxcix"),
        (400, "cd"),
        (401, "cdi"),
        (426, "cdxxvi"),
        (444, "cdxliv"),
        (499, "cdxcix"),
        (500, "d"),
        (501, "di"),
        (555, "dlv"),
        (600, "dc"),
        (700, "dcc"),
        (789, "dccLxxxix"),
        (800, "dccc"),
        (850, "dcccl"),
        (900, "cm"),
        (901, "cmi"),
        (944, "cmxliv"),
        (999, "cmxcix"),
        (1000, "m"),
    ],
)
def test_int_to_mini_roman_parametrized(number, expected):
    assert int_to_mini_roman(number) == expected

def test_basic_values():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

def test_subtraction_cases():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_combination_cases():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(42) == 'xlii'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(888) == 'dccclxxxviii'
    assert int_to_mini_roman(944) == 'cmxliv'

def test_repetition_cases():
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'

def test_invalid_input():
    with pytest.raises(Exception):
        int_to_mini_roman(0)
    with pytest.raises(Exception):
        int_to_mini_roman(-1)
    assert int_to_mini_roman(1001) == 'm'