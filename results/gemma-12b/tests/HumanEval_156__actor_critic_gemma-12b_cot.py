
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

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    i = len(roman_map) - 1
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result.lower()

class TestIntToMiniRoman:
    def test_valid_input(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(5) == "v"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(10) == "x"
        assert int_to_mini_roman(19) == "xix"
        assert int_to_mini_roman(426) == "cdxxvi"
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(444) == "cdxliv"
        assert int_to_mini_roman(1000) == "m"

    def test_edge_cases(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(2) == "ii"
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(5) == "v"
        assert int_to_mini_roman(10) == "x"
        assert int_to_mini_roman(50) == "l"
        assert int_to_mini_roman(100) == "c"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(399) == "cccxcix"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(900) == "cm"

    def test_number_with_subtractive_notation(self):
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(90) == "xc"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(900) == "cm"

    def test_multiple_subtractive_notations(self):
        assert int_to_mini_roman(44) == "xliv"
        assert int_to_mini_roman(99) == "xciX"
        assert int_to_mini_roman(444) == "cdxliv"

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            int_to_mini_roman("abc")
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)
        with pytest.raises(ValueError):
            int_to_mini_roman(-1)

    @pytest.mark.parametrize("number, expected", [
        (2, "ii"), (3, "iii"), (6, "vi"), (7, "vii"), (8, "viii"),
        (11, "xi"), (12, "xii"), (13, "xiii"), (14, "xiv"), (15, "xv"),
        (16, "xvi"), (17, "xvii"), (18, "xviii"), (20, "xx"), (30, "xxx"),
        (41, "xli"), (42, "xlxii"), (43, "xlxiii"), (45, "xlv"), (46, "xlvi"),
        (47, "xlvii"), (48, "xlviii"), (49, "xlix"), (51, "li"), (52, "lxxii"),
        (53, "lxxiii"), (54, "lxiv"), (55, "lv"), (56, "lvi"), (57, "lvii"),
        (58, "lviii"), (59, "lix"), (60, "lx"), (61, "lxi"), (62, "lxii"),
        (63, "lxiii"), (64, "lxiv"), (65, "lxv"), (66, "lxvi"), (67, "lxvii"),
        (68, "lxviii"), (69, "lxix"), (70, "lxx"), (71, "lxxxi"), (72, "lxxii"),
        (73, "lxxiii"), (74, "lxxiv"), (75, "lxxv"), (76, "lxxvi"), (77, "lxxvii"),
        (78, "lxxviii"), (79, "lxxix"), (80, "lxxx"), (81, "lxxxi"), (82, "lxxxii"),
        (83, "lxxxiii"), (84, "lxxxiv"), (85, "lxxxv"), (86, "lxxxvi"), (87, "lxxxvii"),
        (88, "lxxxviii"), (89, "lxxxix"), (91, "xci"), (92, "xciii"), (93, "xciv"),
        (94, "xcv"), (95, "xcvi"), (96, "xcvii"), (97, "xcviii"), (98, "xcix")
    ])
    def test_more_valid_numbers(self, number, expected):
        assert int_to_mini_roman(number) == expected