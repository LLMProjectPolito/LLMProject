
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
from your_module import bf  # Replace your_module

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_valid_range():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mars", "Saturn") == ("Jupiter",)
    assert bf("Venus", "Earth") == ("Mercury",)
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn", "Mars", "Earth", "Venus", "Mercury")
    assert bf("Uranus", "Mars") == ("Saturn", "Jupiter", "Earth", "Venus", "Mercury")
    assert bf("Saturn", "Venus") == ("Jupiter", "Earth", "Mars", "Mercury")
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("InvalidPlanet", "Earth") == ()
    assert bf("Earth", "InvalidPlanet") == ()
    assert bf("InvalidPlanet1", "InvalidPlanet2") == ()

def test_bf_case_sensitivity():
    assert bf("mercury", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("jUpItEr", "nEpTuNe") == ()

def test_bf_empty_input():
    assert bf("", "") == ()

def test_bf_one_invalid_planet():
    assert bf("Earth", "Pluto") == ()
    assert bf("Pluto", "Earth") == ()

def test_bf_planet_order():
    assert bf("Venus", "Jupiter") == ("Earth", "Mars", "Saturn")
    assert bf("Mars", "Venus") == ("Mercury", "Earth")

def test_bf_same_planet():
    assert bf("Mercury", "Mercury") == ()
    assert bf("Venus", "Venus") == ()
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()
    assert bf("Jupiter", "Jupiter") == ()
    assert bf("Saturn", "Saturn") == ()
    assert bf("Uranus", "Uranus") == ()
    assert bf("Neptune", "Neptune") == ()