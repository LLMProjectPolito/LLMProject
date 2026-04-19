
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

# The function generate_integers is assumed to be defined in the environment.

@pytest.mark.parametrize("a, b, expected", [
    # --- Standard Cases (Ascending & Descending) ---
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (1, 5, [2, 4]),
    (5, 1, [2, 4]),
    (1, 2, [2]),
    (2, 1, [2]),

    # --- Single Value Ranges ---
    (2, 2, [2]),   # Even digit
    (4, 4, [4]),   # Even digit
    (3, 3, []),    # Odd digit
    (5, 5, []),    # Odd digit
    (11, 11, []),  # Out of digit range

    # --- Digit Boundaries & Zero ---
    (0, 5, [0, 2, 4]),       # Including zero
    (0, 15, [0, 2, 4, 6, 8]), # Zero to above digit range
    (1, 9, [2, 4, 6, 8]),    # Full positive span
    (9, 1, [2, 4, 6, 8]),    # Full positive span reversed

    # --- Partial Overlaps (One bound >= 10) ---
    (5, 12, [6, 8]),
    (12, 5, [6, 8]),
    (2, 15, [2, 4, 6, 8]),
    (15, 2, [2, 4, 6, 8]),
    (8, 11, [8]),
    (11, 8, [8]),

    # --- Out-of-Bounds (No digits 0-9) ---
    (10, 14, []),
    (14, 10, []),
    (100, 200, []),
    (200, 100, []),
    (11, 13, []),
])
def test_generate_integers_parametrized(a, b, expected):
    """
    Comprehensive test covering standard ranges, boundary conditions, 
    digit constraints, and input order independence.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_return_type():
    """
    Ensure the function always returns a list, regardless of whether 
    the result is empty or populated.
    """
    assert isinstance(generate_integers(11, 13), list)
    assert isinstance(generate_integers(2, 4), list)

def test_generate_integers_ordering_and_symmetry():
    """
    Verify that the output is always ascending and that the 
    order of arguments (a, b) does not change the result.
    """
    a, b = 2, 8
    res_forward = generate_integers(a, b)
    res_backward = generate_integers(b, a)
    
    # Symmetry: f(a, b) == f(b, a)
    assert res_forward == res_backward
    # Ordering: Result must be sorted ascending
    assert res_forward == sorted(res_forward)