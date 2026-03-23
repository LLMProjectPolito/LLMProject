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

def test_bf_valid_planets_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_valid_planets_2():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_valid_planets_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_valid_planets_4():
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")

def test_bf_valid_planets_5():
    assert bf("Mars", "Jupiter") == ("Earth",)

def test_bf_invalid_planet_1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet_2():
    assert bf("Earth", "Pluto") == ()

def test_bf_invalid_planet_both():
    assert bf("Pluto", "Ceres") == ()

def test_bf_invalid_planet_name():
    assert bf("Invalid", "Neptune") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid", "Invalid") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()

def test_bf_planet1_after_planet2():
    assert bf("Neptune", "Jupiter") == ()
    assert bf("Uranus", "Saturn") == ()

def test_bf_edge_case_mercury_venus():
    assert bf("Mercury", "Venus") == ()

def test_bf_edge_case_venus_earth():
    assert bf("Venus", "Earth") == ()

def test_bf_edge_case_neptune_uranus():
    assert bf("Neptune", "Uranus") == ()

def test_bf_edge_case_mercury_neptune():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")