
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
def test_bf_numeric_types():
    assert bf(1, 2) == ()
    assert bf(1.5, "Earth") == ()

def test_bf_none_type():
    assert bf(None, "Mars") == ()
    assert bf("Jupiter", None) == ()
    assert bf(None, None) == ()

def test_bf_collection_types():
    assert bf(["Earth"], ["Mars"]) == ()
    assert bf({"planet": "Earth"}, "Mars") == ()

# Focus: Boundary Values
import pytest

def test_bf_adjacent_planets():
    # Planets immediately next to each other should return an empty tuple
    assert bf("Mercury", "Venus") == ()
    assert bf("Neptune", "Uranus") == ()

def test_bf_same_planet():
    # The same planet as both arguments should return an empty tuple
    assert bf("Earth", "Earth") == ()

def test_bf_extreme_boundaries():
    # The furthest possible boundaries (Mercury and Neptune)
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected

# Focus: Logic Branches
import pytest

def test_bf_logic_branches():
    # Branch: planet2 is closer to the sun than planet1
    assert bf("Earth", "Mercury") == ("Venus",)
    
    # Branch: one or both planet names are invalid
    assert bf("Mars", "Pluto") == ()
    assert bf("Xenon", "Earth") == ()
    
    # Branch: planets are adjacent or the same (no planets in between)
    assert bf("Mercury", "Venus") == ()
    assert bf("Jupiter", "Jupiter") == ()