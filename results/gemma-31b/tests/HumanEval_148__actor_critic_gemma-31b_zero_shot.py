
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
    '''
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    start = min(idx1, idx2)
    end = max(idx1, idx2)
    
    # Slice from start + 1 to end (exclusive of the boundary planets)
    return planets[start + 1 : end]

@pytest.mark.parametrize("p1, p2, expected", [
    # Provided Examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Edge Case: Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Uranus", "Neptune", ()),
    
    # Edge Case: Same planet
    ("Earth", "Earth", ()),
    
    # Edge Case: Extreme ends of the solar system
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Edge Case: Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Mars", "Sun", ()),
    ("Moon", "Star", ()),
    ("", "Earth", ()),
    (None, "Earth", ()),
    
    # Edge Case: Case sensitivity (assuming strict matching)
    ("mercury", "Earth", ()),
    ("EARTH", "Mars", ()),
])
def test_bf(p1, p2, expected):
    assert bf(p1, p2) == expected

def test_bf_return_type():
    """Ensure the function always returns a tuple."""
    assert isinstance(bf("Jupiter", "Neptune"), tuple)
    assert isinstance(bf("Invalid", "Earth"), tuple)
    assert isinstance(bf("Earth", "Earth"), tuple)