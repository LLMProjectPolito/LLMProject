
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

def test_valid_planets():
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Earth") == ("Mercury",)
    assert bf("Mars", "Venus") == ("Earth",)
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn", "Mars", "Earth", "Venus", "Mercury")
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Neptune") == ()
    assert bf("Mercury", "Mercury") == ()

def test_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "X") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Mars", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_case_sensitivity():
    assert bf("jupiter", "Neptune") == ()
    assert bf("Earth", "neptune") == ()
    assert bf("mercury", "venus") == ()

def test_empty_input():
    assert bf("", "Venus") == ()
    assert bf("Earth", "") == ()
    assert bf("", "") == ()

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_edge_cases():
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Neptune", "Uranus") == ("Saturn", "Jupiter", "Mars", "Earth", "Venus", "Mercury")