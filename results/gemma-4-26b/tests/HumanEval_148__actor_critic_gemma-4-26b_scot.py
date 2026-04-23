
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
from __main__ import bf

@pytest.mark.parametrize("p1, p2, expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
])
def test_docstring_examples(p1, p2, expected):
    """Verify the examples provided in the docstring."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    ("Jupiter", "Neptune"),
    ("Neptune", "Jupiter"),
    ("Earth", "Mercury"),
    ("Mercury", "Earth"),
    ("Mercury", "Uranus"),
    ("Uranus", "Mercury"),
])
def test_order_invariance(p1, p2):
    """Verify that the order of input planets does not affect the result."""
    assert bf(p1, p2) == bf(p2, p1)

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),      # Non-existent planet
    ("Earth", "MarsX"),      # Typo
    ("Sun", "Moon"),         # Not planets
    ("", ""),                # Empty strings
    (" ", "Venus"),          # Whitespace
    ("123", "Jupiter"),      # Numeric strings
    ("earth", "Mercury"),    # Case sensitivity (lowercase)
    ("JUPITER", "Neptune"),  # Case sensitivity (uppercase)
])
def test_invalid_string_names(p1, p2):
    """Verify that invalid planet name strings return an empty tuple."""
    assert bf(p1, p2) == ()

@pytest.mark.parametrize("p1, p2", [
    (None, "Earth"),
    (123, "Jupiter"),
    ("Mars", ["Venus"]),
])
def test_invalid_types(p1, p2):
    """Verify that passing non-string types raises a TypeError."""
    with pytest.raises(TypeError):
        bf(p1, p2)

def test_full_range():
    """Verify the result when the two input planets are the first and last in the sequence."""
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected

def test_same_planet():
    """Verify that if both planets are the same, an empty tuple is returned."""
    assert bf("Mars", "Mars") == ()
    assert bf("Neptune", "Neptune") == ()

@pytest.mark.parametrize("p1, p2", [
    ("Mercury", "Venus"),
    ("Venus", "Earth"),
    ("Earth", "Mars"),
    ("Mars", "Jupiter"),
    ("Jupiter", "Saturn"),
    ("Saturn", "Uranus"),
    ("Uranus", "Neptune"),
])
def test_adjacent_planets(p1, p2):
    """Verify that adjacent planets return an empty tuple."""
    assert bf(p1, p2) == ()