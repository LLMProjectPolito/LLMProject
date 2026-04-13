
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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    planet1_orbit = planet1
    planet2_orbit = planet2
    
    if planet1_orbit < planet2_orbit:
        return (planet1, planet2)
    else:
        return (planet2, planet1)

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_venus_mercury():
    assert bf("Venus", "Mercury") == ("Earth")

def test_bf_mercury_venus():
    assert bf("Mercury", "Venus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_jupiter_venus():
    assert bf("Jupiter", "Venus") == ("Saturn", "Uranus")

def test_bf_saturn_venus():
    assert bf("Saturn", "Venus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_uranus_venus():
    assert bf("Uranus", "Venus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ("Saturn", "Uranus")

def test_bf_mars_venus():
    assert bf("Mars", "Venus") == ("Venus")

def test_bf_jupiter_venus():
    assert bf("Jupiter", "Venus") == ("Saturn", "Uranus")

def test_bf_saturn_venus():
    assert bf("Saturn", "Venus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_uranus_venus():
    assert bf("Uranus", "Venus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_neptune_mars():
    assert bf("Neptune", "Mars") == ("Saturn", "Uranus")

def test_bf_mars_jupiter():
    assert bf("Mars", "Jupiter") == ("Jupiter", "Saturn")

def test_bf_jupiter_mars():
    assert bf("Jupiter", "Mars") == ("Saturn", "Uranus")

def test_bf_saturn_jupiter():
    assert bf("Saturn", "Jupiter") == ("Jupiter", "Saturn")

def test_bf_uranus_neptune():
    assert bf("Uranus", "Neptune") == ("Neptune", "Saturn", "Uranus")

def test_bf_earth_mercury_invalid():
    assert bf("Earth", "Mercury") == ()

def test_bf_mercury_invalid():
    assert bf("Mercury", "Mercury") == ()

def test_bf_invalid_input():
    assert bf("Earth", 1) == ()