
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

    start_index = planets.index(planet1)
    end_index = planets.index(planet2)

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    result = tuple(planets[start_index + 1:end_index])
    return result

def test_valid_planets_in_order():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_valid_planets_reverse_order():
    assert bf("Earth", "Mercury") == ("Venus")

def test_valid_planets_adjacent():
    assert bf("Earth", "Mars") == ()

def test_valid_planets_wide_range():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_invalid_planets_both():
    assert bf("Pluto", "X") == ()

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_empty_input():
    assert bf("", "") == ()