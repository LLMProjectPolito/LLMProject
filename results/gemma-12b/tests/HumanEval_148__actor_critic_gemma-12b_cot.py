
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

    if index1 >= index2:
        return ()

    between_planets = planets[index1 + 1:index2]
    return tuple(between_planets)

def test_bf_jupiter_to_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_to_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_to_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_venus_to_saturn():
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")

def test_bf_mars_to_jupiter():
    assert bf("Mars", "Jupiter") == ("Jupiter",)

def test_bf_earth_to_earth():
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet_name():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Invalid", "Neptune") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid", "Invalid") == ()

def test_bf_empty_tuple_invalid_input():
    assert bf("Invalid1", "Invalid2") == ()

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == ("Mars",)

def test_bf_edge_cases():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ()