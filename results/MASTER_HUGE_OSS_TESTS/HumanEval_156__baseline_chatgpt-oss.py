import pytest

# ----------------------------------------------------------------------
# NOTE:
# The function under test is expected to be defined in a module that is
# importable from the test file.  Adjust the import statement below to match
# the actual location (e.g. `from roman import int_to_mini_roman` or
# `from solution import int_to_mini_roman`).
# ----------------------------------------------------------------------
from solution import int_to_mini_roman  # <-- change if needed


# ----------------------------------------------------------------------
# Helper data – a collection of numbers and their expected lowercase Roman
# numerals.  The list covers:
#   * simple additive cases (1‑3, 5‑8, 10‑30, 50‑80, 100‑300, 500‑800)
#   * subtractive notation (4, 9, 40, 90, 400, 900)
#   * edge values (1 and 1000)
#   * a few random values to increase confidence
# ----------------------------------------------------------------------
ROMAN_PAIRS = [
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
    (19, "xix"),
    (20, "xx"),
    (30, "xxx"),
    (40, "xl"),
    (44, "xliv"),
    (49, "xlix"),
    (50, "l"),
    (58, "lviii"),
    (68, "lxviii"),
    (70, "lxx"),
    (80, "lxxx"),
    (90, "xc"),
    (94, "xciv"),
    (99, "xcix"),
    (100, "c"),
    (104, "civ"),
    (149, "cxlix"),
    (152, "clii"),
    (190, "cxc"),
    (199, "cxcix"),
    (200, "cc"),
    (276, "cclxxvi"),
    (300, "ccc"),
    (400, "cd"),
    (426, "cdxxvi"),
    (444, "cdxliv"),
    (500, "d"),
    (578, "dlxxviii"),
    (600, "dc"),
    (699, "dcxcix"),
    (700, "dcc"),
    (800, "dccc"),
    (900, "cm"),
    (944, "cmxliv"),
    (999, "cmxcix"),
    (1000, "m"),
]


@pytest.mark.parametrize("number,expected", ROMAN_PAIRS)
def test_known_values(number, expected):
    """
    Verify that a wide range of valid inputs produce the exact expected
    lowercase Roman numeral.
    """
    result = int_to_mini_roman(number)
    assert isinstance(result, str), "Result must be a string"
    assert result == expected, f"{number} should be '{expected}' but got '{result}'"


# ----------------------------------------------------------------------
# Boundary tests – the function is defined only for 1 ≤ n ≤ 1000.
# ----------------------------------------------------------------------
@pytest.mark.parametrize("invalid", [0, -1, -42, 1001, 1234, 10_000])
def test_out_of_range_raises(invalid):
    """
    Numbers outside the allowed interval must raise an exception.
    The exact exception type is not documented, so we accept any subclass of
    Exception.
    """
    with pytest.raises(Exception):
        int_to_mini_roman(invalid)


# ----------------------------------------------------------------------
# Type‑checking tests – the implementation should reject non‑integer inputs.
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "bad_input",
    [
        3.14,                     # float
        "X",                      # string
        b"iv",                    # bytes
        None,                     # NoneType
        [5],                      # list
        {"num": 10},              # dict
        (7,),                     # tuple
        True,                     # bool (subclass of int but semantically wrong)
    ],
)
def test_invalid_type_raises(bad_input):
    """
    Passing a value that is not an int should raise an exception.
    """
    with pytest.raises(Exception):
        int_to_mini_roman(bad_input)


# ----------------------------------------------------------------------
# Randomised sanity check – generate a few numbers, convert them, and then
# convert the result back to an integer using a simple reference implementation.
# This ensures the function is internally consistent even for values not
# explicitly listed in ROMAN_PAIRS.
# ----------------------------------------------------------------------
def _reference_roman_to_int(s: str) -> int:
    """
    Very small reference implementation (uppercase) used only for the
    sanity‑check test below.  It supports the same range (1‑1000) and the
    standard subtractive rules.
    """
    roman_map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = roman_map[ch]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total


import random


@pytest.mark.parametrize("seed", [0, 42, 12345])
def test_random_roundtrip(seed):
    """
    For a handful of random numbers in the valid range, ensure that converting
    to a mini‑roman string and back yields the original integer.
    """
    random.seed(seed)
    for _ in range(20):
        n = random.randint(1, 1000)
        roman = int_to_mini_roman(n)
        # The function must return a lowercase string; the reference works with uppercase.
        assert roman.islower()
        assert _reference_roman_to_int(roman) == n