
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
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    start = min(idx1, idx2)
    end = max(idx1, idx2)
    
    return planets[start + 1 : end]

import pytest

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard cases (Forward order)
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Standard cases (Reverse order)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Mars", "Venus", ("Earth",)),
    
    # Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Same planet (should return empty tuple)
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Jupiter", "Unknown", ()),
    ("", "Mercury", ()),
    ("Venus", "", ()),
    (None, "Mars", ()), 
])
def test_bf_planets(p1, p2, expected):
    assert bf(p1, p2) == expected

def test_bf_return_type():
    """Ensure the function always returns a tuple."""
    result = bf("Jupiter", "Neptune")
    assert isinstance(result, tuple)
    
    result_empty = bf("Invalid", "Invalid")
    assert isinstance(result_empty, tuple)

def test_bf_case_sensitivity():
    """
    Depending on implementation, 'earth' might be different from 'Earth'.
    The problem description uses Capitalized names. 
    Usually, these functions are case-sensitive unless specified.
    """
    # If the function is strictly following the provided list, lowercase should return ()
    assert bf("earth", "mercury") == ()