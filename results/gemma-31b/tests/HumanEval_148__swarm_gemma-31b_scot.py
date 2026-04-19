
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

def test_bf_invalid_planet_name():
    """Test that providing a planet name not in the solar system list returns an empty tuple."""
    assert bf("Mars", "Pluto") == ()

def test_bf_adjacent_planets():
    """Test that providing two adjacent planets returns an empty tuple."""
    assert bf("Mercury", "Venus") == ()

def test_bf_reverse_order_extremes():
    """Test the furthest and closest planets in reverse order.
    The result should be all planets between them, sorted by proximity to the Sun.
    """
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")