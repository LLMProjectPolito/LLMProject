
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

    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)

    result = tuple(planets[planet1_index + 1:planet2_index])
    return result

def test_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_valid_planets_reverse():
    assert bf("Neptune", "Jupiter") == ()

def test_adjacent_planets_no_planets_between():
    assert bf("Earth", "Mars") == ()

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_both_invalid():
    assert bf("Pluto", "Ceres") == ()

def test_edge_case_mercury_neptune():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_edge_case_neptune_mercury():
    assert bf("Neptune", "Mercury") == ()

def test_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_single_planet_between():
    assert bf("Mars", "Jupiter") == ("Earth",)