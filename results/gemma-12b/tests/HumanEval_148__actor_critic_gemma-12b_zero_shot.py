
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
    assert bf("Uranus", "Neptune") == ("Saturn")
    assert bf("Neptune", "Mercury") == ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Invalid", "Valid") == ()
    assert bf("Valid", "Invalid") == ()
    assert bf("InvalidPlanet", "AnotherInvalid") == ()

def test_bf_case_sensitivity():
    assert bf("mercury", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("EARTH", "mars") == ()
    assert bf("Jupiter", "NEPTUNE") == ()
    assert bf("jUpItEr", "uRaNuS") == ()
    assert bf("earth", "Earth") == ()
    assert bf("EARTH", "earth") == ()

def test_bf_empty_string():
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_reversed_planet_order():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert bf("Uranus", "Venus") == ("Saturn", "Jupiter", "Mars", "Earth")
    assert bf("Saturn", "Mercury") == ("Jupiter", "Uranus", "Neptune")
    assert bf("Venus", "Earth") == ("Mercury",)
    assert bf("Mars", "Jupiter") == ("Earth", "Venus")

def test_bf_one_valid_one_invalid():
    assert bf("Earth", "Pluto") == ()
    assert bf("Pluto", "Earth") == ()

def test_bf_one_empty_one_valid():
    assert bf("", "Earth") == ()
    assert bf("Earth", "") == ()

def test_bf_large_planet_set():
    # Test with a larger set of planets to check for performance issues
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")