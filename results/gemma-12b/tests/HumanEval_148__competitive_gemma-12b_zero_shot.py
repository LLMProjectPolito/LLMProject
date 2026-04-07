
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

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_neptune_neptune():
    assert bf("Neptune", "Neptune") == ()

def test_bf_venus_mars():
    assert bf("Venus", "Mars") == ("Earth",)

def test_bf_mars_jupiter():
    assert bf("Mars", "Jupiter") == ("Saturn",)

def test_bf_invalid_planet1():
    assert bf("Pluto", "Earth") == ()

def test_bf_invalid_planet2():
    assert bf("Earth", "Pluto") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Ceres") == ()

def test_bf_planet1_after_planet2():
    assert bf("Neptune", "Mercury") == ()

def test_bf_planet1_and_planet2_same():
    assert bf("Earth", "Earth") == ()

def test_bf_empty_tuple():
    assert bf("Uranus", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn")