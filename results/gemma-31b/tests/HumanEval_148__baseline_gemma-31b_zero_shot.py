
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
    # Provided examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Forward order cases
    ("Mercury", "Earth", ("Venus",)),
    ("Mars", "Neptune", ("Jupiter", "Saturn", "Uranus")),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Reverse order cases
    ("Neptune", "Mercury", ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
    ("Neptune", "Jupiter", ("Uranus", "Saturn")),
    ("Mars", "Venus", ("Earth",)),
    
    # Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    ("Venus", "Mercury", ()),
    
    # Same planet (should return empty tuple)
    ("Earth", "Earth", ()),
    ("Jupiter", "Jupiter", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Mars", "Mars-ish", ()),
    ("", "Mercury", ()),
    (None, "Venus", ()),
    
    # Case sensitivity checks (assuming strict matching based on prompt)
    ("earth", "mercury", ()),
    ("EARTH", "MERCURY", ()),
])
def test_bf_planets(p1, p2, expected):
    """Test the bf function with various planet combinations and edge cases."""
    result = bf(p1, p2)
    assert result == expected
    assert isinstance(result, tuple), f"Expected return type tuple, got {type(result)}"

def test_bf_return_type():
    """Ensure the function always returns a tuple regardless of input."""
    assert isinstance(bf("Mercury", "Neptune"), tuple)
    assert isinstance(bf("Invalid", "Invalid"), tuple)
    assert isinstance(bf("Earth", "Earth"), tuple)