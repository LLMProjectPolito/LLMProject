import pytest

# Import the functions under test.
# Adjust the import path if the functions live in a different module.
from solution import is_palindrome, get_max, bf


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic palindrome
        ("hello", False),               # non‑palindrome
        ("", True),                     # empty string (trivially palindrome)
        ("a", True),                    # single character
        ("Able was I ere I saw ElbA", False),  # case‑sensitive, spaces included
        ("Madam", False),               # case‑sensitive
        ("madam", True),                # lower‑case palindrome
        ("😊🚀🚀😊", True),               # Unicode characters
        ("😊🚀😊", False),               # Unicode non‑palindrome
        ("  ", True),                   # two spaces – palindrome
        (" a ", True),                  # spaces around a single char
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a range of inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_mutability():
    """Ensure the function does not modify the original string."""
    original = "radar"
    copy = original[:]
    assert is_palindrome(original) is True
    # The original string should stay unchanged.
    assert original == copy


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # all positive
        ([-1, -5, -2], -1),                 # all negative
        ([0, -1, 5, 3], 5),                 # mixed values
        ([42], 42),                         # single element
        (list(range(-1000, 1001)), 1000),   # large range
    ],
)
def test_get_max_valid(arr, expected):
    """Check that get_max returns the correct maximum for non‑empty lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should yield None."""
    assert get_max([]) is None


def test_get_max_immutable_input():
    """The original list must remain unchanged after the call."""
    original = [3, 1, 4, 1, 5]
    copy = original[:]
    _ = get_max(original)
    assert original == copy


# ----------------------------------------------------------------------
# Tests for `bf`
# ----------------------------------------------------------------------
PLANETS = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Neptune", "Jupiter", ("Saturn", "Uranus")),  # order of args shouldn't matter
        ("Earth", "Mercury", ("Venus",)),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Mars", "Mars", ()),                         # same planet → empty tuple
        ("Saturn", "Saturn", ()),                     # same planet → empty tuple
    ],
)
def test_bf_valid_ranges(p1, p2, expected):
    """Validate correct intermediate planets for various planet pairs."""
    result = bf(p1, p2)
    assert isinstance(result, tuple)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_p1,invalid_p2",
    [
        ("Pluto", "Neptune"),   # first invalid
        ("Earth", "Pluto"),     # second invalid
        ("pluto", "neptune"),   # wrong case
        ("", "Mars"),           # empty string
        (None, "Venus"),        # None as first argument
        ("Mars", None),         # None as second argument
        (123, "Venus"),         # non‑string type
        ("Mars", 456),          # non‑string type
    ],
)
def test_bf_invalid_planet_names(invalid_p1, invalid_p2):
    """Any invalid planet name should cause an empty tuple result."""
    assert bf(invalid_p1, invalid_p2) == ()


def test_bf_original_arguments_unchanged():
    """The function must not mutate its input arguments."""
    p1 = "Earth"
    p2 = "Uranus"
    p1_copy = p1
    p2_copy = p2
    _ = bf(p1, p2)
    assert p1 == p1_copy
    assert p2 == p2_copy


def test_bf_all_possible_pairs():
    """
    Exhaustively check that for every ordered pair of distinct planets,
    the function returns exactly the planets that lie strictly between them.
    """
    for i, planet_a in enumerate(PLANETS):
        for j, planet_b in enumerate(PLANETS):
            if i == j:
                expected = ()
            else:
                low, high = sorted((i, j))
                expected = tuple(PLANETS[low + 1 : high])
            assert bf(planet_a, planet_b) == expected