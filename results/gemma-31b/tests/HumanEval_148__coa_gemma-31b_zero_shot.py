
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


# Focus: Boundary Values
import pytest

def test_bf_adjacent_planets():
    # Boundary: Planets immediately next to each other should return an empty tuple
    assert bf("Mercury", "Venus") == ()
    assert bf("Neptune", "Uranus") == ()

def test_bf_same_planet():
    # Boundary: The same planet as both arguments should return an empty tuple
    assert bf("Earth", "Earth") == ()

def test_bf_extreme_boundaries():
    # Boundary: The first and last planets in the system
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

# Focus: Type Scenarios
import pytest

def test_bf_non_string_types():
    assert bf(123, "Earth") == ()
    assert bf("Mars", None) == ()
    assert bf(["Venus"], "Jupiter") == ()

def test_bf_invalid_type_combinations():
    assert bf(None, None) == ()
    assert bf(3.14, 2.71) == ()

# Focus: Logic Branches
import pytest

def test_bf_valid_ranges():
    # Branch: planet1 closer than planet2
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    # Branch: planet2 closer than planet1 (should still be sorted by proximity to sun)
    assert bf("Earth", "Mercury") == ("Venus",)
    # Branch: Adjacent planets (empty range)
    assert bf("Mercury", "Venus") == ()

def test_bf_invalid_inputs():
    # Branch: planet1 is invalid
    assert bf("Pluto", "Earth") == ()
    # Branch: planet2 is invalid
    assert bf("Mars", "Unknown") == ()
    # Branch: both are invalid
    assert bf("X", "Y") == ()

def test_bf_edge_cases():
    # Branch: Same planet provided
    assert bf("Jupiter", "Jupiter") == ()
    # Branch: Maximum range
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")