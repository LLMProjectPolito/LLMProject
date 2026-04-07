
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

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Mars", "Jupiter") == ("Earth", "Venus")
    assert bf("Saturn", "Uranus") == ("Jupiter")
    assert bf("Uranus", "Neptune") == ()
    assert bf("Neptune", "Mercury") == planets[:-1]

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Venus", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()
    assert bf("Venus", "Venus") == ()
    assert bf("Mars", "Mars") == ()
    assert bf("Jupiter", "Jupiter") == ()
    assert bf("Saturn", "Saturn") == ()
    assert bf("Uranus", "Uranus") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_planet1_after_planet2():
    assert bf("Neptune", "Mercury") == planets[:-1]
    assert bf("Uranus", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Jupiter", "Earth") == ("Venus", "Mars")
    assert bf("Saturn", "Mars") == ("Earth", "Venus", "Jupiter")

def test_bf_empty_tuple():
    assert bf("Uranus", "Neptune") == ()
    assert bf("Neptune", "Uranus") == ()

def test_bf_edge_cases():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == planets[:-1]