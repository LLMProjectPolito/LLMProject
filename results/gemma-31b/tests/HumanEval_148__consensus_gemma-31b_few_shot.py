
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
    # Standard order
    ("Mercury", "Earth"), ("Venus",),
    ("Venus", "Mars"), ("Earth",),
    ("Mars", "Saturn"), ("Jupiter",),
    ("Jupiter", "Uranus"), ("Saturn",),
    ("Saturn", "Neptune"), ("Uranus",),
    ("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"),
    ("Jupiter", "Neptune"), ("Saturn", "Uranus"),
    ("Venus", "Saturn"), ("Earth", "Mars", "Jupiter"),
    ("Mercury", "Neptune"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"),
    # Reverse order
    ("Earth", "Mercury"), ("Venus",),
    ("Neptune", "Jupiter"), ("Saturn", "Uranus"),
    ("Mars", "Mercury"), ("Venus", "Earth"),
    ("Neptune", "Mercury"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"),
    # Adjacent planets
    ("Mercury", "Venus"), (),
    ("Venus", "Mercury"), (),
    ("Venus", "Earth"), (),
    ("Earth", "Venus"), (),
    ("Earth", "Mars"), (),
    ("Mars", "Earth"), (),
    ("Mars", "Jupiter"), (),
    ("Jupiter", "Mars"), (),
    ("Jupiter", "Saturn"), (),
    ("Saturn", "Jupiter"), (),
    ("Saturn", "Uranus"), (),
    ("Uranus", "Saturn"), (),
    ("Uranus", "Neptune"), (),
    ("Neptune", "Uranus"), (),
    # Same planet
    ("Earth", "Earth"), (),
    ("Mars", "Mars"), (),
    ("Jupiter", "Jupiter"), (),
])
def test_bf_valid_planets(p1, p2, expected):
    """Test the function with valid planet names in various orders and distances."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),
    ("Earth", "Pluto"),
    ("Mars", "Sun"),
    ("Moon", "Neptune"),
    ("Jupiter", "Unknown"),
    ("Earth", "Mars-like"),
    ("", "Mercury"),
    ("Venus", ""),
    ("", ""),
    (None, "Earth"),
    ("Earth", None),
    ("Earth", 123),
    ("EARTH", "Mars"), # Case sensitivity
    ("mercury", "Venus"), # Case sensitivity
    ("mercury", "earth"), # Case sensitivity
])
def test_bf_invalid_planets(p1, p2):
    """Test the function returns an empty tuple when one or both inputs are invalid."""
    assert bf(p1, p2) == ()

def test_bf_return_type():
    """Ensure the return type is always a tuple."""
    assert isinstance(bf("Jupiter", "Neptune"), tuple)
    assert isinstance(bf("Earth", "Mercury"), tuple)
    assert isinstance(bf("Invalid", "Invalid"), tuple)