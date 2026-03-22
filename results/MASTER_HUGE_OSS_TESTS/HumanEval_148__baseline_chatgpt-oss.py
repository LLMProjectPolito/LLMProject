import pytest

# The function under test is expected to be defined in a module named `solution.py`.
# Adjust the import path if the implementation lives in a different file.
from solution import bf


# ----------------------------------------------------------------------
# Helper data for parametrized tests
# ----------------------------------------------------------------------
PLANET_ORDER = (
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
    "planet1, planet2, expected",
    [
        # basic forward direction
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Earth", "Mars", ("")),
        # reverse direction – function must still return planets ordered
        # from the Sun outward, regardless of argument order
        ("Neptune", "Jupiter", ("Saturn", "Uranus")),
        ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Mars", "Earth", ("Venus",)),
        # same planet – there are no planets in‑between
        ("Earth", "Earth", ()),
        # adjacent planets – only the planet that lies strictly between
        ("Earth", "Mercury", ("Venus",)),
        ("Mercury", "Venus", ()),
    ],
)
def test_between_planets_basic(planet1, planet2, expected):
    """Check that bf returns the correct tuple for valid planet names."""
    result = bf(planet1, planet2)

    # Normalise expected: an empty string in the parametrisation above means an empty tuple
    if expected == ("",):
        expected = ()
    assert isinstance(result, tuple), "Result must be a tuple"
    assert result == expected


@pytest.mark.parametrize(
    "planet1, planet2",
    [
        ("Pluto", "Mars"),          # first argument invalid
        ("Earth", "Pluto"),         # second argument invalid
        ("pluto", "Mars"),          # case‑sensitive invalid
        ("Earth", ""),              # empty string
        (None, "Mars"),             # non‑string argument
        ("Earth", 42),              # non‑string argument
    ],
)
def test_invalid_inputs_return_empty_tuple(planet1, planet2):
    """If either argument is not a recognised planet name, the function must return an empty tuple."""
    result = bf(planet1, planet2)
    assert result == (), f"Expected empty tuple for inputs ({planet1!r}, {planet2!r})"


def test_original_arguments_unchanged():
    """The function must not mutate its input arguments."""
    p1 = "Jupiter"
    p2 = "Neptune"
    p1_copy = p1[:]
    p2_copy = p2[:]

    _ = bf(p1, p2)

    assert p1 == p1_copy
    assert p2 == p2_copy


def test_all_planets_between_first_and_last():
    """When the first planet is the innermost and the second is the outermost,
    the function should return every intermediate planet in order."""
    result = bf("Mercury", "Neptune")
    # All planets except the two extremes
    expected = tuple(PLANET_ORDER[1:-1])
    assert result == expected


def test_case_sensitivity():
    """The specification does not mention case‑insensitivity, so the function
    should treat differently‑cased strings as invalid."""
    assert bf("mercury", "Neptune") == ()
    assert bf("Mercury", "neptune") == ()


def test_whitespace_handling():
    """Leading/trailing whitespace should make the name invalid (strict matching)."""
    assert bf(" Mercury", "Neptune") == ()
    assert bf("Mercury ", "Neptune") == ()
    assert bf("Mercury", " Neptune") == ()
    assert bf("Mercury", "Neptune ") == ()


def test_no_duplicate_planets_in_result():
    """Result must never contain duplicate planet names."""
    result = bf("Mercury", "Uranus")
    assert len(result) == len(set(result)), "Result contains duplicate entries"


def test_result_is_sorted_by_distance_from_sun():
    """Regardless of argument order, the returned tuple must be sorted from
    the Sun outward (i.e., follow the order defined in PLANET_ORDER)."""
    # Random order of arguments
    result = bf("Neptune", "Mercury")
    # Expected list of all intermediate planets in proper order
    expected = tuple(PLANET_ORDER[1:-1])
    assert result == expected