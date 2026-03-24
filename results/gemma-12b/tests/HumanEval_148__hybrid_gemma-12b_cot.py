
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

    start = min(index1, index2) + 1
    end = max(index1, index2)

    between_planets = tuple(planets[start:end])
    return between_planets

def test_bf_valid_planets_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_valid_planets_2():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_valid_planets_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_valid_planets_4():
    assert bf("Mercury", "Mercury") == ()

def test_bf_valid_planets_5():
    assert bf("Neptune", "Neptune") == ()

def test_bf_valid_planets_6():
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")

def test_bf_invalid_planet_1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet_2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_invalid_planets_both():
    assert bf("Pluto", "Ceres") == ()

def test_bf_planet1_after_planet2():
    assert bf("Saturn", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter")

def test_bf_planet1_and_planet2_same():
    assert bf("Earth", "Earth") == ()

def test_bf_empty_tuple_return():
    assert isinstance(bf("Mercury", "Uranus"), tuple)

def test_bf_edge_cases_1():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_edge_cases_2():
    assert bf("Neptune", "Mercury") == ()