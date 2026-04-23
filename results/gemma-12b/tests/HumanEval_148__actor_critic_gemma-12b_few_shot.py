
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

    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()

    planet1 = planet1.capitalize()
    planet2 = planet2.capitalize()

    if planet1 not in planets or planet2 not in planets:
        return ()

    if planet1 == planet2:
        return ()

    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    start_index = min(index1, index2) + 1
    end_index = max(index1, index2)

    between_planets = tuple(planets[start_index:end_index])
    return between_planets

# Pytest tests
def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_case_insensitive():
    assert bf("earth", "mercury") == ("venus",)
    assert bf("EARTH", "MERCURY") == ("venus",)
    assert bf("jupiter", "neptune") == ("saturn", "uranus")

def test_bf_adjacent_planets():
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Earth") == ()

def test_bf_planet1_after_planet2():
    assert bf("Venus", "Mercury") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_planet2_after_planet1():
    assert bf("Mercury", "Venus") == ()

def test_bf_boundary_conditions():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ()

def test_bf_identical_planets():
    assert bf("Mercury", "Mercury") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Venus") == ()
    assert bf("Earth", "Mars2") == ()
    assert bf("Earth", 123) == ()

def test_bf_non_string_input():
    assert bf(123, "Venus") == ()
    assert bf("Earth", 456) == ()
    assert bf(123, 456) == ()