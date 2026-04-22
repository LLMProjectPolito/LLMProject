
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

def test_bf_provided_examples():
    """Tests the examples provided in the problem description."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_order_independence():
    """Tests that the function returns the same result regardless of argument order."""
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert bf("Mercury", "Earth") == ("Venus",)
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_adjacent_planets():
    """Tests that planets next to each other return an empty tuple."""
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Saturn", "Uranus") == ()
    assert bf("Uranus", "Saturn") == ()

def test_bf_same_planet():
    """Tests that providing the same planet twice returns an empty tuple."""
    assert bf("Mars", "Mars") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_invalid_planet_names():
    """Tests that invalid planet names return an empty tuple."""
    assert bf("Pluto", "Earth") == ()
    assert bf("Mars", "Sun") == ()
    assert bf("Jupiter", "Xylophone") == ()
    assert bf("", "Mercury") == ()
    assert bf("Earth", "earth") == ()  # Testing case sensitivity

def test_bf_full_range():
    """Tests the range between the first and last planets."""
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected