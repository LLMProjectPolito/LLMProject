
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
    # Standard cases (Forward order)
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    
    # Standard cases (Reverse order)
    ("Earth", "Mercury", ("Venus",)),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Mars", "Venus", ("Earth",)),
    
    # Adjacent planets (Empty result)
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    
    # Same planet (Empty result)
    ("Earth", "Earth", ()),
    ("Jupiter", "Jupiter", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Jupiter", "Mars-ish", ()),
    
    # Case sensitivity and type checks
    ("earth", "Mars", ()),
    ("EARTH", "MARS", ()),
    (None, "Earth", ()),
    ("Earth", 123, ()),
    ("", ""),
])
def test_bf(p1, p2, expected):
    assert bf(p1, p2) == expected

def test_bf_return_type():
    """Ensure the function always returns a tuple."""
    result = bf("Jupiter", "Neptune")
    assert isinstance(result, tuple)
    
    result_empty = bf("Invalid", "Invalid")
    assert isinstance(result_empty, tuple)