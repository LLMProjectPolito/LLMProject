
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function being tested
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    s = str(abs(num))
    evens = sum(1 for d in s if int(d) % 2 == 0)
    odds = len(s) - evens
    return (evens, odds)

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),               # basic_positive
    (-12, (1, 1)),               # basic_negative
    (4567, (2, 2)),              # basic_mixed
    (0, (1, 0)),                 # zero
    (2, (1, 0)),                 # single_digit_even
    (7, (0, 1)),                 # single_digit_odd
    (-5, (0, 1)),                # single_digit_negative
    (2468, (4, 0)),              # all_even
    (802, (3, 0)),               # all_even_with_zero
    (1357, (0, 4)),              # all_odd
    (91, (0, 2)),                # all_odd_small
    (1234567890, (5, 5)),        # large_number
    (10**50, (50, 1)),           # extreme_large_positive (1 followed by 50 zeros)
    (-(10**50), (50, 1)),        # extreme_large_negative (symmetry check)
    (True, (0, 1)),              # boolean_true_as_one (documents bool subclassing)
    (False, (1, 0)),             # boolean_false_as_zero (documents bool subclassing)
], ids=[
    "basic_positive", 
    "basic_negative", 
    "basic_mixed", 
    "zero", 
    "single_digit_even", 
    "single_digit_odd", 
    "single_digit_negative", 
    "all_even", 
    "all_even_with_zero", 
    "all_odd", 
    "all_odd_small", 
    "large_number", 
    "extreme_large_positive",
    "extreme_large_negative",
    "boolean_true",
    "boolean_false"
])
def test_even_odd_count_valid_inputs(num, expected):
    """Tests valid integer inputs including edge cases, extreme values, and booleans."""
    assert even_odd_count(num) == expected


@pytest.mark.parametrize("invalid_input", [
    None,
    "123",
    12.3,
    [1, 2],
    {"num": 1}
], ids=["none", "string", "float", "list", "dict"])
def test_even_odd_count_type_safety(invalid_input):
    """Tests that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        even_odd_count(invalid_input)