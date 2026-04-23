
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
    assert bf("Neptune", "Uranus") == ()
    assert bf("Saturn", "Jupiter") == ("Uranus", "Neptune")
    assert bf("Earth", "Jupiter") == ("Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Mars") == ("Venus", "Earth")
    assert bf("Venus", "Venus") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Invalid", "Earth") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()
    assert bf("mercury", "venus") == () # case sensitive

def test_bf_edge_cases():
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ()

def test_bf_empty_tuple():
    assert bf("Uranus", "Saturn") == ("Jupiter", "Neptune")
    assert bf("Saturn", "Uranus") == ("Jupiter", "Neptune")

def test_bf_single_planet():
    assert bf("Mercury", "Venus") == ("Mercury",)
    assert bf("Venus", "Mercury") == ()
    assert bf("Earth", "Earth") == ()

def test_bf_planet_order():
    assert bf("Earth", "Mars") == ("Mars",)
    assert bf("Mars", "Earth") == ()
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ()