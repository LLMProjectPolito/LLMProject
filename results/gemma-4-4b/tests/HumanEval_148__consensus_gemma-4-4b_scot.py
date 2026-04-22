
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
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    if index1 > index2:
        index1, index2 = index2, index1
    
    between_planets = planets[index1 + 1:index2]
    return tuple(between_planets)

@pytest.fixture
def planets():
    return ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def test_bf_jupiter_neptune(planets):
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury(planets):
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus(planets):
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_reverse_order(planets):
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_same_planet(planets):
    assert bf("Earth", "Earth") == ()

def test_bf_planet1_before_planet2(planets):
    assert bf("Mars", "Saturn") == ("Jupiter")

def test_bf_planet2_before_planet1(planets):
    assert bf("Saturn", "Mars") == ("Jupiter")

def test_bf_invalid_planet1(planets):
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2(planets):
    assert bf("Mercury", "Pluto") == ()

def test_bf_both_invalid_planets(planets):
    assert bf("Pluto", "Pluto") == ()