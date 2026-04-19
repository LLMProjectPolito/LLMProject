
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
    # Standard cases from examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Boundary cases: Extreme ends
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Boundary cases: Adjacent planets (should be empty)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Same planet
    ("Earth", "Earth", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Mars", "Sun", ()),
    ("Moon", "Jupiter", ()),
    ("Invalid", "Invalid", ()),
    
    # Case sensitivity and type checks (assuming strict string matching based on problem description)
    ("earth", "Mercury", ()), 
    ("EARTH", "Mercury", ()),
    (None, "Earth", ()),
    ("Earth", 123, ()),
])
def test_bf(p1, p2, expected):
    result = bf(p1, p2)
    assert result == expected
    assert isinstance(result, tuple)