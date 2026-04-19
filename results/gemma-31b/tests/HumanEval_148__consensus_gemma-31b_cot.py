
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
    # Standard cases from docstring
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Reversed order (should still be sorted by proximity to sun)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Extremes
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Adjacent planets (no planets between them)
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    
    # Same planet
    ("Mars", "Mars", ()),
    ("Earth", "Earth", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Mars", "Jupiter-ish", ()),
    ("", "Mercury", ()),
    ("Venus", "", ()),
    
    # Case sensitivity
    ("earth", "mercury", ()),
    ("EARTH", "MERCURY", ()),
    ("Earth", "mercury", ()),
    
    # Non-string inputs
    (None, "Earth", ()),
    ("Earth", None, ()),
    (1, 2, ()),
])
def test_bf(p1, p2, expected):
    """
    Tests the bf function with various combinations of valid and invalid planet names,
    ensuring the result is always a tuple sorted by proximity to the sun.
    """
    assert bf(p1, p2) == expected

def test_bf_return_type():
    """
    Ensures that the function always returns a tuple.
    """
    # Single element case
    assert isinstance(bf("Earth", "Mercury"), tuple)
    # Empty case
    assert isinstance(bf("Mercury", "Venus"), tuple)
    # Multiple elements case
    assert isinstance(bf("Mercury", "Neptune"), tuple)