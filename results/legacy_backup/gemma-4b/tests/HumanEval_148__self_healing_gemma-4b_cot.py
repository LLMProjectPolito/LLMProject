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
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        index1 = planet_order.index(planet1)
        index2 = planet_order.index(planet2)
    except ValueError:
        return ()

    if index1 >= index2:
        return ()

    planets_between = planet_order[index1 + 1:index2]
    planets_between.sort(key=lambda planet: planet_order.index(planet))
    return tuple(planets_between)


def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_venus_earth():
    assert bf("Venus", "Earth") == ("Mars")

def test_bf_mars_jupiter():
    assert bf("Mars", "Jupiter") == ("Saturn")

def test_bf_saturn_uranus():
    assert bf("Saturn", "Uranus") == ("Jupiter")

def test_bf_uranus_neptune():
    assert bf("Uranus", "Neptune") == ("Saturn", "Jupiter")

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_adjacent_planets():
    assert bf("Mars", "Jupiter") == ("Saturn")

def test_bf_far_apart_planets():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")