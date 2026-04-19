
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
    # Provided Examples & Full Range
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Forward Order
    ("Mercury", "Earth", ("Venus",)),
    ("Venus", "Jupiter", ("Earth", "Mars")),
    ("Mars", "Neptune", ("Jupiter", "Saturn", "Uranus")),
    ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
    
    # Reverse Order (Should return sorted by distance from sun)
    ("Earth", "Mercury", ("Venus",)),
    ("Jupiter", "Venus", ("Earth", "Mars")),
    ("Neptune", "Mars", ("Jupiter", "Saturn", "Uranus")),
    ("Saturn", "Venus", ("Earth", "Mars", "Jupiter")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    
    # Small Gaps
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Saturn", ("Jupiter",)),
    ("Saturn", "Neptune", ("Uranus",)),
    ("Jupiter", "Earth", ("Mars",)),
    
    # Adjacent Planets
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Earth", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    
    # Same Planet
    ("Earth", "Earth", ()),
    ("Jupiter", "Jupiter", ()),
    ("Neptune", "Neptune", ()),
])
def test_bf_logic(p1, p2, expected):
    """Test the core logic including forward, reverse, adjacent, and same-planet cases."""
    assert bf(p1, p2) == expected

def test_bf_invalid_planet_names():
    """Test cases where planet names are invalid, misspelled, or case-incorrect."""
    # One invalid
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Pluto") == ()
    # Both invalid
    assert bf("Sun", "Moon") == ()
    assert bf("Xenon", "Ytterbium") == ()
    # Case sensitivity
    assert bf("mercury", "Earth") == () 
    assert bf("EARTH", "Mars") == ()
    assert bf("Mercury", "mars") == ()
    # Empty strings or whitespace
    assert bf("", "Mars") == ()
    assert bf("Mars", " ") == ()

def test_bf_type_safety():
    """Test cases with non-string inputs to ensure robustness."""
    assert bf(None, "Earth") == ()
    assert bf("Mars", 123) == ()
    assert bf(1, 2) == ()
    assert bf(["Mercury"], "Venus") == ()

def test_bf_return_type_consistency():
    """Ensure the function always returns a tuple regardless of the input."""
    assert isinstance(bf("Jupiter", "Neptune"), tuple)
    assert isinstance(bf("Earth", "Mercury"), tuple)
    assert isinstance(bf("Invalid", "Invalid"), tuple)
    assert isinstance(bf(None, None), tuple)