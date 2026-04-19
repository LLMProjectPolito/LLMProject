
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

def test_bf_basic_forward():
    """Test cases where planet1 is closer to the sun than planet2."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_basic_reverse():
    """Test cases where planet2 is closer to the sun than planet1."""
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_adjacent_planets():
    """Planets immediately next to each other should return an empty tuple."""
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Earth", "Mars") == ()

def test_bf_same_planet():
    """Providing the same planet twice should return an empty tuple."""
    assert bf("Mars", "Mars") == ()

def test_bf_invalid_names():
    """Test that invalid planet names return an empty tuple."""
    assert bf("Pluto", "Earth") == ()  # Pluto is not in the provided list
    assert bf("Earth", "Mars-ish") == ()
    assert bf("Sun", "Moon") == ()
    assert bf("", "") == ()

def test_bf_case_sensitivity():
    """Test that the function handles case sensitivity (assuming strict matching)."""
    assert bf("mercury", "Earth") == ()
    assert bf("EARTH", "Mars") == ()

def test_bf_invalid_types():
    """Test that non-string inputs return an empty tuple rather than crashing."""
    assert bf(None, "Earth") == ()
    assert bf("Earth", 123) == ()
    assert bf(["Mars"], "Jupiter") == ()
    assert bf(None, None) == ()