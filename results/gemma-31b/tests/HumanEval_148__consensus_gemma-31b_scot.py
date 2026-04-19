
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
    # Provided examples and standard ranges
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Saturn", ("Jupiter",)),
    ("Mercury", "Mars", ("Venus", "Earth")),
    ("Venus", "Jupiter", ("Earth", "Mars")),
    ("Saturn", "Earth", ("Mars", "Jupiter")),
    
    # Reverse order (should still be sorted by proximity to sun)
    ("Earth", "Mercury", ("Venus",)),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Saturn", "Venus", ("Earth", "Mars", "Jupiter")),
    ("Mars", "Mercury", ("Venus", "Earth")),
    ("Jupiter", "Venus", ("Earth", "Mars")),
    ("Earth", "Saturn", ("Mars", "Jupiter")),
    
    # Extreme boundaries
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
])
def test_bf_valid_ranges(p1, p2, expected):
    """Test various valid planet ranges, both forward and reverse."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    # Adjacent planets
    ("Mercury", "Venus"),
    ("Venus", "Mercury"),
    ("Venus", "Earth"),
    ("Earth", "Venus"),
    ("Earth", "Mars"),
    ("Mars", "Earth"),
    ("Mars", "Jupiter"),
    ("Jupiter", "Mars"),
    ("Jupiter", "Saturn"),
    ("Saturn", "Jupiter"),
    ("Saturn", "Uranus"),
    ("Uranus", "Saturn"),
    ("Uranus", "Neptune"),
    ("Neptune", "Uranus"),
    # Same planet
    ("Mercury", "Mercury"),
    ("Earth", "Earth"),
    ("Mars", "Mars"),
    ("Jupiter", "Jupiter"),
    ("Saturn", "Saturn"),
    ("Uranus", "Uranus"),
    ("Neptune", "Neptune"),
])
def test_bf_empty_results(p1, p2):
    """Test that adjacent or identical planets return an empty tuple."""
    assert bf(p1, p2) == ()

@pytest.mark.parametrize("p1, p2", [
    # Invalid planet names
    ("Pluto", "Earth"),
    ("Earth", "Pluto"),
    ("Sun", "Moon"),
    ("Jupiter", "InvalidPlanet"),
    ("InvalidPlanet", "Jupiter"),
    # Case sensitivity
    ("mercury", "Earth"),
    ("EARTH", "Mars"),
    ("jupiter", "neptune"),
    # Empty strings or None/Wrong types
    ("", "Venus"),
    ("Venus", ""),
    ("", ""),
    (None, "Earth"),
    ("Earth", None),
    (123, "Mars"),
    ("Mars", 456),
])
def test_bf_invalid_inputs(p1, p2):
    """Test that invalid inputs return an empty tuple."""
    assert bf(p1, p2) == ()