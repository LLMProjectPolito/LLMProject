
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
    except ValueError:
        return ()

    if idx1 >= idx2:
        return ()

    result = []
    for i in range(idx1 + 1, idx2):
        result.append(planets[i])

    return tuple(result)

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_venus_earth():
    assert bf("Venus", "Earth") == ("Mars")

def test_bf_mars_jupiter():
    assert bf("Mars", "Jupiter") == ("Saturn")

def test_bf_saturn_uranus():
    assert bf("Saturn", "Uranus") == ("Jupiter")

def test_bf_uranus_neptune():
    assert bf("Uranus", "Neptune") == ("Saturn", "Jupiter")

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_adjacent_planets():
    assert bf("Mars", "Jupiter") == ("Saturn")

def test_bf_far_apart_planets():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_empty_string():
    assert bf("", "Neptune") == ()

def test_bf_none_planet1():
    assert bf(None, "Neptune") == ()

def test_bf_none_planet2():
    assert bf("Jupiter", None) == ()