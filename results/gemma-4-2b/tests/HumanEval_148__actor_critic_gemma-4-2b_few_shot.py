
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


def test_bf_Jupiter_Neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_Earth_Mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_Mercury_Uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_Neptune_Mercury():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Mercury", "Pluto") == ()

def test_bf_valid_range():
    assert bf("Mars", "Saturn") == ("Jupiter")

def test_bf_all_planets():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_planet1_first_planet_planet2_last_planet():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_planet1_last_planet_planet2_first_planet():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == ("Venus")

def test_bf_adjacent_planets_reversed():
    assert bf("Mars", "Earth") == ("Venus")

def test_bf_planet1_before_planet2_same_index():
    assert bf("Venus", "Venus") == ()

def test_bf_planet1_after_planet2_same_index():
    assert bf("Neptune", "Neptune") == ()

def test_bf_reverse_order_planets():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")