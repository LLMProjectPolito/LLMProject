
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


# Focus: Invalid Inputs
import pytest

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Earth") == ()
    assert bf("Mars", "Xenon") == ()
    assert bf("InvalidPlanet", "InvalidPlanet") == ()
    assert bf("", "Mercury") == ()

def test_bf_invalid_types():
    assert bf(123, "Earth") == ()
    assert bf("Mars", None) == ()
    assert bf(["Jupiter"], "Saturn") == ()
    assert bf(None, None) == ()

# Focus: Logic Branches
import pytest

def test_bf_ordering_branches():
    # Branch: planet1 is closer to sun than planet2
    assert bf("Mercury", "Mars") == ("Venus", "Earth")
    # Branch: planet2 is closer to sun than planet1 (should still be sorted by proximity to sun)
    assert bf("Mars", "Mercury") == ("Venus", "Earth")
    # Branch: planets are adjacent (no planets between)
    assert bf("Earth", "Mars") == ()
    # Branch: planets are the same
    assert bf("Jupiter", "Jupiter") == ()

def test_bf_invalid_input_branches():
    # Branch: planet1 is invalid
    assert bf("Pluto", "Earth") == ()
    # Branch: planet2 is invalid
    assert bf("Earth", "Mars-X") == ()
    # Branch: both are invalid
    assert bf("Sun", "Moon") == ()
    # Branch: case sensitivity or typo
    assert bf("mercury", "Venus") == ()

# Focus: Boundary Values
import pytest

def test_bf_boundary_adjacent():
    # Planets immediately next to each other should return an empty tuple
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Uranus", "Neptune") == ()

def test_bf_boundary_same_planet():
    # The same planet as both arguments should return an empty tuple
    assert bf("Earth", "Earth") == ()
    assert bf("Jupiter", "Jupiter") == ()

def test_bf_boundary_extremes():
    # The furthest possible boundaries (first and last planets)
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected