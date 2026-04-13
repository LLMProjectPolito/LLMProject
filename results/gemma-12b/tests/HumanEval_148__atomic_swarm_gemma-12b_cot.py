
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
import math

def test_basic():
    from solution import bf
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_edge_invalid_planets():
    """Tests the edge case where both input planets are invalid."""
    from solution import bf
    result = bf("Pluto", "Ceres")
    assert result == ()

def test_invalid_planet_names():
    from solution import bf
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Earth", "Marsian") == ()
    assert bf("Invalid", "Valid") == ()
    assert bf("Valid", "Invalid") == ()