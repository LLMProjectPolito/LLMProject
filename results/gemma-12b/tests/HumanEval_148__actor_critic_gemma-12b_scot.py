
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
    Returns a tuple of planets located between planet1 and planet2, sorted by proximity to the sun.
    Returns an empty tuple if either planet is invalid or if planet1's index is greater than or equal to planet2's index.
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()

    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    if index1 >= index2:
        return ()  # Prevent out-of-bounds errors and incorrect results

    result = tuple(planets[index1 + 1:index2])
    return result

def test_planets_in_between():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_planets_reversed():
    assert bf("Neptune", "Jupiter") == ()

def test_adjacent_planets():
    assert bf("Earth", "Mars") == ()

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Pluto", "Ceres") == ()

def test_mercury_neptune():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_neptune_mercury():
    assert bf("Neptune", "Mercury") == ()

def test_mercury_neptune_edge():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")