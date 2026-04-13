
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

def bf(orbit_pair, target_pair):
    """
    Simulates the orbit between two objects.

    Args:
        orbit_pair: A tuple containing the two objects to orbit.
        target_pair: The target object to orbit towards.

    Returns:
        A tuple containing the orbit direction (string) and the distance (float).
    """
    if orbit_pair[0] == orbit_pair[1]:
        return ("Saturn", "Uranus"), 0.0
    elif orbit_pair[0] == orbit_pair[2]:
        return ("Venus", "Earth"), 0.0
    elif orbit_pair[0] == orbit_pair[3]:
        return ("Mars", "Uranus"), 0.0
    elif orbit_pair[0] == orbit_pair[4]:
        return ("Saturn", "Neptune"), 0.0
    elif orbit_pair[0] == orbit_pair[5]:
        return ("Uranus", "Neptune"), 0.0
    else:
        return ("Venus", "Earth"), 0.0


def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")