
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

def bf(orbit, planet):
    """
    This is a placeholder function for demonstration purposes.
    Replace with your actual function.
    """
    if orbit == "Jupiter" and planet == "Neptune":
        return "Saturn"
    elif orbit == "Earth" and planet == "Mercury":
        return "Uranus"
    elif orbit == "Mercury" and planet == "Uranus":
        return "Venus"
    elif orbit == "Venus" and planet == "Earth":
        return "Mars"
    elif orbit == "Venus" and planet == "Uranus":
        return "Jupiter"
    elif orbit == "Mars" and planet == "Uranus":
        return "Saturn"
    elif orbit == "Jupiter" and planet == "Neptune":
        return "Uranus"
    elif orbit == "Neptune" and planet == "Saturn":
        return "Uranus"
    else:
        return "Unknown"

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Earth" in bf("Venus", "Venus")
    assert "Mars" in bf("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert "Jupiter" in bf("Saturn", "Uranus")
    assert "Neptune" in bf("Uranus", "Saturn")
    assert "Mercury" in bf("Venus", "Mercury")
    assert "Mars" in bf("Mercury", "Uranus")
    assert "Jupiter" in bf("Mars", "Uranus")
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Neptune", "Saturn")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Earth" in bf("Venus", "Venus")
    assert "Mars" in bf("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert "Jupiter" in bf("Saturn", "Uranus")
    assert "Neptune" in bf("Uranus", "Saturn")
    assert "Mercury" in bf("Venus", "Mercury")
    assert "Mars" in bf("Mercury", "Uranus")
    assert "Jupiter" in bf("Mars", "Uranus")
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Neptune", "Saturn")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Earth" in bf("Venus", "Venus")
    assert "Mars" in bf("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert "Jupiter" in bf("Saturn", "Uranus")
    assert "Neptune" in bf("Uranus", "Saturn")
    assert "Mercury" in bf("Venus", "Mercury")
    assert "Mars" in bf("Mercury", "Uranus")
    assert "Jupiter" in bf("Mars", "Uranus")
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Neptune", "Saturn")