
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

@pytest.mark.parametrize("planet1, planet2, expected", [
    # Provided examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Reverse order of planets
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    
    # Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Same planet
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Invalid", "Invalid", ()),
    ("Earth", "Invalid", ()),
    ("Invalid", "Earth", ()),
    
    # Case sensitivity check (assuming strict matching based on prompt)
    ("earth", "mercury", ()),
    ("EARTH", "MERCURY", ()),
    
    # Full range
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
])
def test_bf(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected