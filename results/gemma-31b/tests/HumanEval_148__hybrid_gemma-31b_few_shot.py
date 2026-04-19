
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
    # Standard Forward Ranges (p1 closer to sun than p2)
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
    ("Mars", "Neptune", ("Jupiter", "Saturn", "Uranus")),
    
    # Standard Reverse Ranges (p2 closer to sun than p1)
    ("Earth", "Mercury", ("Venus",)),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mars", "Venus", ("Earth",)),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Saturn", "Venus", ("Earth", "Mars", "Jupiter")),
    ("Neptune", "Mars", ("Jupiter", "Saturn", "Uranus")),
])
def test_bf_valid_ranges(p1, p2, expected):
    """Tests that valid planet pairs return the correct planets between them, sorted by proximity to the sun."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    # Adjacent Planets
    ("Mercury", "Venus"),
    ("Venus", "Earth"),
    ("Earth", "Mars"),
    ("Mars", "Jupiter"),
    ("Jupiter", "Saturn"),
    ("Saturn", "Uranus"),
    ("Uranus", "Neptune"),
    # Same Planet
    ("Earth", "Earth"),
    ("Jupiter", "Jupiter"),
    ("Mars", "Mars"),
])
def test_bf_empty_results(p1, p2):
    """Tests that adjacent planets or the same planet return an empty tuple."""
    assert bf(p1, p2) == ()

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),      # Outdated planet
    ("Mars", "Sun"),         # Star, not planet
    ("Xenon", "Ypsilon"),    # Fake names
    ("mercury", "Earth"),    # Case sensitivity
    ("Mars", "mars"),        # Case sensitivity
    ("", "Venus"),           # Empty string
    (None, "Mars"),          # None type
    ("Jupiter", 123),        # Integer type
])
def test_bf_invalid_inputs(p1, p2):
    """Tests that invalid planet names, incorrect casing, or wrong types return an empty tuple."""
    assert bf(p1, p2) == ()

def test_bf_return_type():
    """Ensures the function consistently returns a tuple regardless of the input."""
    assert isinstance(bf("Mercury", "Earth"), tuple)
    assert isinstance(bf("Mars", "Mars"), tuple)
    assert isinstance(bf("Invalid", "Invalid"), tuple)