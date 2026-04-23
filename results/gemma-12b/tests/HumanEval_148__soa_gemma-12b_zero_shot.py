
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
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Invalid", "Valid") == ()
    assert bf("Valid", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()
    assert bf("Mercury", "Mercury2") == ()
    assert bf("Mercury2", "Mercury") == ()

def test_bf_empty_input():
    assert bf("", "") == ()

def test_bf_case_sensitivity():
    assert bf("mercury", "neptune") == ()
    assert bf("Mercury", "neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("jupiter", "neptune") == ()
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_planet_order():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus", "Mercury")
    assert bf("Venus", "Neptune") == ("Mercury", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Uranus", "Venus") == ("Saturn", "Jupiter", "Mars", "Earth", "Mercury")
    assert bf("Saturn", "Mars") == ("Jupiter", "Earth", "Venus", "Mercury")
    assert bf("Mars", "Venus") == ("Earth", "Mercury")
    assert bf("Earth", "Jupiter") == ("Venus", "Mercury")
    assert bf("Venus", "Jupiter") == ("Mercury")
    assert bf("Mercury", "Jupiter") == ()

def test_bf_single_planet():
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Earth") == ()
    assert bf("Earth", "Mars") == ()
    assert bf("Mars", "Jupiter") == ()
    assert bf("Jupiter", "Saturn") == ()
    assert bf("Saturn", "Uranus") == ()
    assert bf("Uranus", "Neptune") == ()
    assert bf("Neptune", "Mercury") == ()