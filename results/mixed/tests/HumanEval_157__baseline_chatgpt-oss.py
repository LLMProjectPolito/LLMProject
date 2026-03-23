import math
import pytest

# The function under test is assumed to be defined in the same module as the tests.
# Do NOT redefine it here – just use the existing implementation.

# ----------------------------------------------------------------------
# Helper fixtures / utilities
# ----------------------------------------------------------------------
def is_right_angle(a, b, c):
    """Utility that mirrors the expected logic of `right_angle_triangle`."""
    # Sort sides so that the largest is last (hypotenuse candidate)
    x, y, z = sorted([a, b, c])
    # A triangle must satisfy the triangle inequality; otherwise it's not a triangle.
    if x <= 0 or y <= 0 or z <= 0 or x + y <= z:
        return False
    # Check the Pythagorean theorem
    return math.isclose(x * x + y * y, z * z, rel_tol=1e-12, abs_tol=1e-12)


# ----------------------------------------------------------------------
# Parametrized tests for valid right‑angled triangles
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "sides",
    [
        (3, 4, 5),
        (5, 12, 13),
        (6, 8, 10),          # scaled 3‑4‑5
        (9, 12, 15),         # another scale
        (7, 24, 25),
        (8, 15, 17),
        (0.3, 0.4, 0.5),     # floating‑point version
        (3000000, 4000000, 5000000),  # very large integers
    ],
)
def test_right_angle_true(sides):
    """All permutations of known Pythagorean triples must return True."""
    a, b, c = sides
    # Test the original ordering
    assert right_angle_triangle(a, b, c) is True
    # Test all permutations – the function should be order‑agnostic
    for perm in [(a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]:
        assert right_angle_triangle(*perm) is True


# ----------------------------------------------------------------------
# Parametrized tests for non‑right‑angled triangles (including invalid ones)
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "sides, expected",
    [
        ((1, 2, 3), False),          # fails triangle inequality
        ((2, 3, 4), False),          # valid triangle but not right‑angled
        ((5, 5, 5), False),          # equilateral
        ((0, 0, 0), False),          # degenerate
        ((-3, 4, 5), False),         # negative side
        ((3, -4, 5), False),
        ((3, 4, -5), False),
        ((1, 1, math.sqrt(2)), False),  # almost right but not exact (float rounding)
    ],
)
def test_right_angle_false(sides, expected):
    """Triangles that are not right‑angled (or not triangles at all) must return False."""
    a, b, c = sides
    assert right_angle_triangle(a, b, c) is expected
    # also test a shuffled order to ensure order‑independence
    for perm in [(a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]:
        assert right_angle_triangle(*perm) is expected


# ----------------------------------------------------------------------
# Tests for type safety – non‑numeric inputs should raise TypeError
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "bad_input",
    [
        ("3", 4, 5),          # string instead of number
        (3, None, 5),         # None as a side
        (3, [4], 5),          # list as a side
        (3, {4: "four"}, 5),  # dict as a side
        (object(), 4, 5),     # arbitrary object
    ],
)
def test_invalid_types_raise(bad_input):
    """Passing non‑numeric arguments should raise a TypeError."""
    with pytest.raises(TypeError):
        right_angle_triangle(*bad_input)


# ----------------------------------------------------------------------
# Edge‑case test: extremely small floating‑point numbers
# ----------------------------------------------------------------------
def test_very_small_floats():
    """Floating point numbers close to zero should be handled correctly."""
    a, b, c = 1e-10, 1e-10, math.sqrt(2) * 1e-10
    # The sides satisfy the Pythagorean theorem to within floating‑point precision,
    # but they do NOT form a valid triangle because a + b == c (degenerate).
    assert right_angle_triangle(a, b, c) is False


# ----------------------------------------------------------------------
# Consistency test: the helper `is_right_angle` should agree with the implementation
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "sides",
    [
        (3, 4, 5),
        (5, 12, 13),
        (2, 2, 3),
        (0, 0, 0),
        (-1, 2, 2),
        (0.3, 0.4, 0.5),
        (1, 1, math.sqrt(2)),
    ],
)
def test_implementation_matches_helper(sides):
    """Cross‑check the function against a reference implementation."""
    a, b, c = sides
    expected = is_right_angle(a, b, c)
    assert right_angle_triangle(a, b, c) is expected