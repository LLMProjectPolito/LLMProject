
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

import pytest

# The function is assumed to be in the same scope or imported
# from solution import bf

@pytest.mark.parametrize("p1, p2, expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
])
def test_bf_happy_path(p1, p2, expected):
    """Test standard valid inputs provided in the problem description."""
    assert bf(p1, p2) == expected


@pytest.mark.parametrize("p1, p2, expected", [
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
])
def test_bf_order_invariance(p1, p2, expected):
    """Test that the function returns the same result regardless of the order of planets."""
    assert bf(p1, p2) == expected
    assert bf(p2, p1) == expected


@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),      # Non-existent planet
    ("Mars", "X"),           # Typo/Invalid name
    ("", "Venus"),           # Empty string
    ("jupiter", "Neptune"),  # Case sensitivity check (assuming exact match required)
    ("Earth", " earth"),     # Leading space
    (None, "Mars"),          # Non-string input
    (123, "Venus"),          # Non-string input
])
def test_bf_invalid_inputs(p1, p2):
    """Test that invalid planet names or types return an empty tuple."""
    assert bf(p1, p2) == ()


@pytest.mark.parametrize("p1, p2, expected", [
    ("Earth", "Mars"),       # Adjacent planets (no planets between)
    ("Mars", "Earth"),       # Adjacent planets reverse
    ("Mercury", "Venus"),    # Adjacent planets
    ("Saturn", "Uranus"),    # Adjacent planets
    ("Earth", "Earth"),      # Same planet
    ("Mercury", "Mercury"),  # Same planet
])
def test_bf_boundary_conditions(p1, p2, expected):
    """Test adjacent planets and identical planet inputs."""
    assert bf(p1, p2) == expected


def test_bf_return_type():
    """Ensure the function strictly returns a tuple, not a list or other iterable."""
    result = bf("Jupiter", "Neptune")
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    
    empty_result = bf("Invalid", "Planet")
    assert isinstance(empty_result, tuple), f"Expected tuple for invalid input, got {type(empty_result)}"