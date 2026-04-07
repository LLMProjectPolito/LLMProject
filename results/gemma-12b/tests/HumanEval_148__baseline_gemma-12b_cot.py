
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

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Mars", "Jupiter") == ("Earth",)
    assert bf("Saturn", "Uranus") == ()
    assert bf("Uranus", "Neptune") == ()
    assert bf("Neptune", "Mercury") == planets[:-1]

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Earth", "Venussss") == ()
    assert bf("Venussss", "Earth") == ()
    assert bf("Plutoss", "Pluto") == ()
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_planet1_after_planet2():
    assert bf("Neptune", "Mercury") == planets[:-1]
    assert bf("Uranus", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Saturn", "Earth") == ("Venus", "Mars", "Jupiter")

def test_bf_planets_order():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Venus", "Uranus") == ("Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Earth", "Saturn") == ("Mars", "Jupiter")
    assert bf("Mars", "Uranus") == ("Jupiter", "Saturn")
    assert bf("Jupiter", "Saturn") == ()
    assert bf("Saturn", "Neptune") == ()
    assert bf("Uranus", "Uranus") == ()