
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


### SCoT Steps:
# STEP 1: REASONING
# The function `int_to_mini_roman` converts an integer to its Roman numeral representation.
# The input is a positive integer between 1 and 1000.
# The output is a string representing the Roman numeral in lowercase.
# The function uses a dictionary `roman_map` to store the mapping between integer values and their Roman numeral representations.
# The algorithm iterates through the `roman_map` from largest to smallest values, subtracting the largest possible value from the input number and appending the corresponding Roman numeral to the result string.

# STEP 2: PLAN
# Test cases:
# 1. Test with numbers 1 to 9 (single digits).
# 2. Test with numbers 10 to 99 (tens and ones).
# 3. Test with numbers 100 to 999 (hundreds, tens, and ones).
# 4. Test with numbers 1 to 1000.
# 5. Test edge cases: 1, 1000.
# 6. Test numbers with combinations of Roman numerals (e.g., 4, 9, 40, 90, 400, 900).
# 7. Test with numbers that have a mix of Roman numeral values.
# 8. Test with invalid input (outside the range 1-1000) - although the problem states 1 <= num <= 1000, it's good practice to include this.

# STEP 3: CODE
import pytest

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
        (42, "xliii"),
        (43, "xliv"),
        (44, "xlv"),
        (45, "xlvi"),
        (46, "xlvii"),
        (47, "xlviii"),
        (48, "xlix"),
        (49, "l"),
        (50, "l"),
        (51, "li"),
        (52, "lii"),
        (53, "liii"),
        (54, "liv"),
        (55, "lv"),
        (56, "lvi"),
        (57, "lvii"),
        (58, "lvii"),
        (59, "lviii"),
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
        (71, "lxcodeproj"),
        (72, "lxxii"),
        (73, "lxxiii"),
        (74, "lxxiv"),
        (75, "lxxv"),
        (76, "lxxvi"),
        (77, "lxxvii"),
        (78, "lxxviii"),
        (79, "lxxix"),
        (80, "lxxx"),
        (81, "lxxxi"),
        (82, "lxxii"),
        (83, "lxxiii"),
        (84, "lxxiv"),
        (85, "lxxv"),
        (86, "lxxvi"),
        (87, "lxxvii"),
        (88, "lxxviii"),
        (89, "lxxix"),
        (90, "lxxx"),
        (91, "lix"),
        (92, "lixii"),
        (93, "lixiii"),
        (94, "lixiv"),
        (95, "lixv"),
        (96, "lixvi"),
        (97, "lixvii"),
        (98, "lixviii"),
        (99, "lixix"),
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        (1000, "m"),
        (1001, "m"), # Test beyond 1000
        (-1, "invalid"), # Test negative input
        (1001, "invalid") # Test input greater than 1000
    ]
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected