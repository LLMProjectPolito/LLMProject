import pytest

# ----------------------------------------------------------------------
# Adjust the import below to match the location of `specialFilter`.
# For example, if the implementation lives in `solution.py`:
#     from solution import specialFilter
# If the tests are placed in the same file as the implementation,
# you can simply use:
#     from __main__ import specialFilter
# ----------------------------------------------------------------------
from solution import specialFilter


@pytest.mark.parametrize(
    "input_list, expected",
    [
        # Provided examples
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),

        # Empty list → 0
        ([], 0),

        # No element satisfies the condition
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -22], 0),

        # All elements satisfy the condition
        ([11, 13, 15, 31, 55, 101, 1111], 7),

        # Boundary values
        ([10, 11, 12, 13, 20, 21, 22, 23], 3),  # 11,13,21 are counted

        # Numbers with even first or last digit
        ([22, 24, 26, 28, 30, 32, 34, 36, 38, 40], 0),

        # Mixed positive and negative numbers
        ([-101, -99, 101, 99, 110, 111], 2),  # 101 and 111 are counted

        # Large numbers
        ([123456789, 987654321, 1357913579, 2468024680], 2),  # first two count
    ],
)
def test_special_filter_various_cases(input_list, expected):
    """
    Verify that `specialFilter` returns the correct count for a wide range
    of inputs, including edge‑cases and typical scenarios.
    """
    assert specialFilter(input_list) == expected


def test_return_type_is_int():
    """The function should always return an integer, even for empty input."""
    result = specialFilter([11, 22, 33])
    assert isinstance(result, int)


def test_invalid_input_type():
    """
    The specification expects a list/iterable of numbers.
    Passing a non‑iterable should raise a TypeError.
    """
    with pytest.raises(TypeError):
        specialFilter(123)          # not iterable
    with pytest.raises(TypeError):
        specialFilter(None)         # not iterable
    with pytest.raises(TypeError):
        specialFilter("12345")      # string is iterable but not a list of numbers


def test_non_integer_numbers_are_ignored():
    """
    If the iterable contains non‑int numeric types (e.g., floats),
    they should be treated according to Python's comparison rules.
    Here we expect the function to raise a ValueError because the
    digit‑extraction logic works only with integers.
    """
    with pytest.raises(ValueError):
        specialFilter([12.5, 13.0, 14.2])