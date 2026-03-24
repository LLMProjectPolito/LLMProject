
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
from typing import List, Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, str]:
    """
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
    """
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()

    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()

    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()

    planet1_orbit = "Mercury"
    planet2_orbit = "Neptune"

    planets = []
    if planet1 == planet1_orbit:
        planets.append(planet1)
    if planet2 == planet2_orbit:
        planets.append(planet2)

    planets.sort(key=lambda x: abs(x - planet1_orbit))

    return tuple(planets)


def test_bf_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_2():
    assert bf("Jupiter", "Venus") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_all():
    assert bf("Mercury", "Neptune") == ("Saturn", "Uranus")
    assert bf("Venus", "Mars") == ("Earth", "Mercury", "Jupiter", "Saturn", "Uranus")
    assert bf("Earth", "Uranus") == ("Venus", "Mercury", "Mars", "Jupiter", "Saturn")
    assert bf("Mars", "Neptune") == ("Saturn", "Uranus")
    assert bf("Jupiter", "Mercury") == ("Saturn", "Uranus")
    assert bf("Saturn", "Neptune") == ("Uranus", "Mercury", "Venus", "Earth", "Mars", "Jupiter")
    assert bf("Uranus", "Neptune") == ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Venus", "Earth") == ("Mars", "Jupiter", "Saturn", "Uranus", "Mercury")
    assert bf("Mars", "Jupiter") == ("Saturn", "Uranus", "Mercury", "Venus", "Earth")
    assert bf("Jupiter", "Saturn") == ("Uranus", "Mercury", "Venus", "Earth", "Mars")
    assert bf("Saturn", "Uranus") == ("Mercury", "Venus", "Earth", "Mars", "Jupiter")
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Neptune") == ("Saturn", "Uranus")
    assert bf("Venus", "Mars") == ("Earth", "Mercury", "Jupiter", "Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mars", "Jupiter") == ("Saturn", "Uranus", "Mercury", "Venus", "Earth")
    assert bf("Jupiter", "Saturn") == ("Uranus", "Mercury", "Venus", "Earth", "Mars")
    assert bf("Saturn", "Uranus") == ("Mercury", "Venus", "Earth", "Mars", "Jupiter")
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Neptune") == ("Saturn", "Uranus")
    assert bf("Venus", "Mars") == ("Earth", "Mercury", "Jupiter", "Saturn", "Uranus")
    assert bf("Earth", "Uranus") == ("Venus", "Mercury", "Mars", "Jupiter", "Saturn")
    assert bf("Mars", "Neptune") == ("Saturn", "Uranus")
    assert bf("Jupiter", "Mercury") == ("Saturn", "Uranus")
    assert bf("Saturn", "Neptune") == ("Uranus", "Mercury", "Venus", "Earth", "Mars")
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Neptune") == ("Saturn", "Uranus")
    print("All tests passed!")