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
    are not correct planet names, or if planet1 and planet2 are the same.
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus",)
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()

    if planet1 == planet2:
        return ()

    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    if index1 >= index2:
        return ()

    between_planets = planets[index1 + 1:index2]
    return tuple(between_planets)


def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Earth", "Mars") == ()  # Added test case for adjacent planets

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Invalid", "Neptune") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid", "Invalid") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()

def test_bf_boundary_conditions():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ()