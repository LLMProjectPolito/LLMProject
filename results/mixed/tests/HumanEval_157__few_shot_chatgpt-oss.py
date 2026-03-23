import pytest

# Import the functions under test.
# Adjust the module name (`solution`) if the functions live in a different file.
from solution import is_palindrome, get_max, right_angle_triangle


# ----------------------------------------------------------------------
# is_palindrome ---------------------------------------------------------
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic palindrome
        ("hello", False),         # simple non‑palindrome
        ("", True),               # empty string (edge case)
        ("A", True),              # single character
        ("RaceCar", False),       # case‑sensitive check
        ("12321", True),          # numeric characters
        ("12345", False),         # numeric non‑palindrome
        ("!@#@!", True),          # punctuation palindrome
        ("!@#$%", False),         # punctuation non‑palindrome
        ("Able was I ere I saw Elba".replace(" ", ""), False),  # spaces removed, still case‑sensitive
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and mixed inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_non_string():
    """The function expects a string; passing other types should raise a TypeError."""
    with pytest.raises(TypeError):
        is_palindrome(123)          # int
    with pytest.raises(TypeError):
        is_palindrome(None)         # NoneType
    with pytest.raises(TypeError):
        is_palindrome(["a", "b"])   # list


# ----------------------------------------------------------------------
# get_max ---------------------------------------------------------------
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # all positive
        ([-1, -5, -2], -1),                 # all negative
        ([0, -1, 5, 3], 5),                 # mixed values
        ([42], 42),                         # single element
        ([-100, 0, 100], 100),              # extremes
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Validate correct maximum for typical non‑empty lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_invalid_input():
    """Non‑list inputs should raise a TypeError."""
    with pytest.raises(TypeError):
        get_max(123)          # int
    with pytest.raises(TypeError):
        get_max("abc")        # str
    with pytest.raises(TypeError):
        get_max(None)         # NoneType


def test_get_max_non_numeric_elements():
    """If the list contains non‑numeric items, max() will raise a TypeError."""
    with pytest.raises(TypeError):
        get_max([1, "two", 3])


# ----------------------------------------------------------------------
# right_angle_triangle ---------------------------------------------------
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "sides,expected",
    [
        ((3, 4, 5), True),          # classic 3‑4‑5 triangle
        ((5, 12, 13), True),        # another Pythagorean triple
        ((6, 8, 10), True),         # scaled 3‑4‑5
        ((1, 1, (2**0.5)), True),   # isosceles right triangle (float)
        ((2, 3, 4), False),         # valid triangle but not right‑angled
        ((1, 2, 3), False),         # degenerate (fails triangle inequality)
        ((0, 0, 0), False),         # zero‑length sides
        ((-3, 4, 5), False),        # negative side length (invalid triangle)
        ((3, 4, 6), False),         # close but not right‑angled
        ((7, 24, 25), True),        # larger Pythagorean triple
    ],
)
def test_right_angle_triangle_various(sides, expected):
    """Check right‑angle detection for a variety of integer and float inputs."""
    a, b, c = sides
    assert right_angle_triangle(a, b, c) is expected


def test_right_angle_triangle_permutations():
    """The order of sides should not affect the result."""
    a, b, c = 3, 4, 5
    permutations = [
        (a, b, c),
        (a, c, b),
        (b, a, c),
        (b, c, a),
        (c, a, b),
        (c, b, a),
    ]
    for perm in permutations:
        assert right_angle_triangle(*perm) is True


def test_right_angle_triangle_invalid_types():
    """Non‑numeric inputs should raise a TypeError."""
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, None, 5)
    with pytest.raises(TypeError):
        right_angle_triangle([3], 4, 5)


def test_right_angle_triangle_floating_point_precision():
    """Floating point rounding errors should not cause false negatives."""
    # 0.1, 0.2, sqrt(0.1**2 + 0.2**2) ≈ 0.2236067977
    a, b = 0.1, 0.2
    c = (a**2 + b**2) ** 0.5
    assert right_angle_triangle(a, b, c) is True