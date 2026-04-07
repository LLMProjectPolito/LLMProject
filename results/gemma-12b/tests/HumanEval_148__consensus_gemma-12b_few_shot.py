
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

def test_bf_valid_range_reverse():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")

def test_bf_valid_range_adjacent():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_valid_range_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_valid_range_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_valid_range_neptune_neptune():
    assert bf("Neptune", "Neptune") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Eris") == ()

def test_bf_planet1_before_planet2():
    assert bf("Venus", "Earth") == ("Mercury",)

def test_bf_planet1_equal_planet2():
    assert bf("Earth", "Earth") == ()

def test_bf_planet1_last_planet2_first():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_planet1_first_planet2_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_empty_string_planet1():
    assert bf("", "Neptune") == ()

def test_bf_empty_string_planet2():
    assert bf("Mercury", "") == ()

def test_bf_both_empty_strings():
    assert bf("", "") == ()

def test_bf_planet1_with_space():
    assert bf(" Mercury", "Neptune") == ()

def test_bf_planet2_with_space():
    assert bf("Mercury", " Neptune") == ()

def test_bf_planet1_and_planet2_with_space():
    assert bf(" Mercury", " Neptune") == ()

def test_bf_case_sensitive():
    assert bf("mercury", "Neptune") == ()
    assert bf("Mercury", "neptune") == ()
    assert bf("MERCURY", "NEPTUNE") == ()