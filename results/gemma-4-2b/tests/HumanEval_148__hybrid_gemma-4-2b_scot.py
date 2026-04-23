
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

    if planets.index(planet1) < planets.index(planet2):
        between_planets = [planet for planet in planets if planet not in [planet1, planet2] and planets.index(planet) > planets.index(planet1) and planets.index(planet) < planets.index(planet2)]
    else:
        between_planets = [planet for planet in planets if planet not in [planet1, planet2] and planets.index(planet) > planets.index(planet2) and planets.index(planet) < planets.index(planet1)]
    
    return tuple(sorted(between_planets))

def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Earth", "Mercury", ("Venus")),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Mars", "Saturn", ("Jupiter", "Uranus")),
        ("Neptune", "Mercury", ("Neptune", "Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
        ("Venus", "Mars", ("Earth", "Jupiter", "Saturn", "Uranus", "Neptune")),
        ("Saturn", "Jupiter", ("Uranus", "Neptune")),
        ("Uranus", "Venus", ("Earth", "Mars", "Jupiter", "Saturn", "Neptune")),
        ("Neptune", "Venus", ("Neptune", "Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
        ("Mercury", "Mercury", ()):  #Test for same planets
    ],
)
def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        ("InvalidPlanet", "Mercury", ()),
        ("Mercury", "InvalidPlanet", ()),
        ("InvalidPlanet", "InvalidPlanet", ()),
    ],
)
def test_bf_invalid_planets(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
        ("Neptune", "Mercury", ("Neptune", "Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
    ],
)
def test_bf_reverse_order(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        ("Mars", "Mars", ()),
    ],
)
def test_bf_same_planet(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected