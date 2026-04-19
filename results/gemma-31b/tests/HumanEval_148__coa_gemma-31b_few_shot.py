
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
import math


# Focus: Type Scenarios
def test_bf_non_string_inputs():
    assert bf(1, "Earth") == ()
    assert bf("Mars", 2.5) == ()
    assert bf(None, "Jupiter") == ()

def test_bf_collection_inputs():
    assert bf(["Mercury"], "Venus") == ()
    assert bf("Earth", ("Mars",)) == ()

# Focus: Logic Branches
def test_bf_order_variants():
    # Branch: planet1 is closer to the sun than planet2
    assert bf("Mercury", "Mars") == ("Venus", "Earth")
    # Branch: planet2 is closer to the sun than planet1
    assert bf("Mars", "Mercury") == ("Venus", "Earth")

def test_bf_invalid_names():
    # Branch: planet1 is invalid
    assert bf("Pluto", "Earth") == ()
    # Branch: planet2 is invalid
    assert bf("Earth", "Sun") == ()
    # Branch: both are invalid
    assert bf("X", "Y") == ()

def test_bf_empty_range():
    # Branch: planets are adjacent (no planets between)
    assert bf("Earth", "Mars") == ()
    # Branch: planets are the same
    assert bf("Jupiter", "Jupiter") == ()

# Focus: Boundary Values
def test_bf_adjacent_planets():
    # Boundary: Planets immediately next to each other should return an empty tuple
    assert bf("Mercury", "Venus") == ()
    assert bf("Neptune", "Uranus") == ()

def test_bf_same_planet():
    # Boundary: The same planet as both arguments should return an empty tuple
    assert bf("Earth", "Earth") == ()

def test_bf_extreme_boundaries():
    # Boundary: The first and last planets in the sequence
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected