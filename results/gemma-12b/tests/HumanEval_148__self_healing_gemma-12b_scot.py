
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

def test_bf_valid_range_2():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_valid_range_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_planet1_last():
    assert bf("Neptune", "Uranus") == ()

def test_bf_planet2_first():
    assert bf("Mercury", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_planet1_invalid():
    assert bf("Pluto", "Venus") == ()

def test_bf_planet2_invalid():
    assert bf("Venus", "Pluto") == ()

def test_bf_both_invalid():
    assert bf("Pluto", "Ceres") == ()

def test_bf_planet1_first_planet2_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_planet1_last_planet2_first():
    assert bf("Neptune", "Mercury") == ()

def test_bf_planet1_and_planet2_are_adjacent():
    assert bf("Earth", "Mars") == ("Mars",)

def test_bf_planet1_and_planet2_are_adjacent_reversed():
    assert bf("Mars", "Earth") == ("Earth",)

def test_bf_empty_tuple():
    assert bf("Venus", "Venus") == ()