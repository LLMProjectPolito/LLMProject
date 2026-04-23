
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
    If planet1 and planet2 are adjacent, the function returns an empty tuple.
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

    if abs(index1 - index2) == 1:
        return ()

    between_planets = planets[index1 + 1:index2]
    return tuple(between_planets)

@pytest.fixture
def planets():
    return ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def test_bf_planets_between_valid():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Mars", "Jupiter") == ("Earth",)

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Invalid", "Neptune") == ()
    assert bf("Mercury", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_bf_reversed_order():
    assert bf("Neptune", "Mercury") == ()
    assert bf("Uranus", "Venus") == ()
    assert bf("Saturn", "Earth") == ()

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == ()
    assert bf("Mars", "Earth") == ()
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()

def test_bf_first_and_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ()