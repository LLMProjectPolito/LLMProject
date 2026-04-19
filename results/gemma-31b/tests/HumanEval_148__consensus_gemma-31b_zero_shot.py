
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

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard Forward
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
    # Standard Backward
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mars", "Venus", ("Earth",)),
    # Adjacent Planets
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Earth", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Mars", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    # Same Planet
    ("Earth", "Earth", ()),
    ("Jupiter", "Jupiter", ()),
])
def test_bf_valid_ranges(p1, p2, expected):
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),
    ("Earth", "Pluto"),
    ("Mars", "Sun"),
    ("Moon", "Jupiter"),
    ("Earth", "InvalidPlanet"),
    ("", "Mercury"),
    (None, "Venus"),
    ("Mars", 123),
    ([], {}),
])
def test_bf_invalid_inputs(p1, p2):
    assert bf(p1, p2) == ()

def test_bf_case_sensitivity():
    """Test that the function is case-sensitive and treats incorrect casing as invalid."""
    assert bf("mercury", "earth") == ()
    assert bf("MERCURY", "EARTH") == ()
    assert bf("earth", "Mars") == ()
    assert bf("Earth", "mars") == ()
    assert bf("Venus", "VENUS") == ()