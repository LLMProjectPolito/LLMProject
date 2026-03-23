import pytest

# The function `bf` is assumed to be imported from the module under test.
# If the function resides in a specific module, replace the import accordingly, e.g.:
# from mymodule import bf


@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        # Basic forward ranges
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Earth", "Mars", ("Mars",)),  # only Mars is between Earth and Mars (exclusive)
        ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
        # Reverse order – function should handle both directions
        ("Neptune", "Jupiter", ("Saturn", "Uranus")),
        ("Uranus", "Mercury", ("Saturn", "Jupiter", "Mars", "Earth", "Venus")),
        # Adjacent planets – result should be empty
        ("Mercury", "Venus", ()),
        ("Mars", "Jupiter", ()),
        # Same planet – no planets in between
        ("Earth", "Earth", ()),
        # Invalid planet names – any invalid name yields empty tuple
        ("Pluto", "Mars", ()),
        ("Earth", "Pluto", ()),
        ("Pluto", "Krypton", ()),
        # Empty strings and None – also invalid
        ("", "Mars", ()),
        (None, "Earth", ()),
        ("Venus", "", ()),
        ("Saturn", None, ()),
        # Wrong capitalisation – should be considered invalid
        ("earth", "Mercury", ()),
        ("MERCURY", "Neptune", ()),
    ],
)
def test_bf_basic_and_edge_cases(planet1, planet2, expected):
    """Test bf with a variety of valid, reversed, adjacent, and invalid inputs."""
    result = bf(planet1, planet2)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert result == expected, f"Expected {expected} for ({planet1}, {planet2}), got {result}"


def test_bf_exhaustive_between_all_planets():
    """Exhaustively verify that the function returns the correct planets for every ordered pair."""
    planets = [
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune"
    ]

    # Build a lookup of index positions for quick reference
    index = {p: i for i, p in enumerate(planets)}

    for i, p1 in enumerate(planets):
        for j, p2 in enumerate(planets):
            # Expected planets are those whose indices lie strictly between i and j
            low, high = sorted((i, j))
            expected = tuple(planets[k] for k in range(low + 1, high))
            result = bf(p1, p2)
            assert result == expected, (
                f"For ({p1}, {p2}) expected {expected} but got {result}"
            )