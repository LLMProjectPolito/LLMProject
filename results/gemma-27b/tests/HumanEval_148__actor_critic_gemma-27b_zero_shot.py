
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

    if index1 == index2:
        return ()

    start = min(index1, index2) + 1
    end = max(index1, index2)

    between_planets = tuple(planets[start:end])
    return between_planets

def test_bf_jupiter_neptune():
    # Test case: Planets are Jupiter and Neptune, expecting Saturn and Uranus
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    # Test case: Planets are Earth and Mercury, expecting Venus
    assert len(bf("Earth", "Mercury")) == 1
    assert bf("Earth", "Mercury")[0] == "Venus"

def test_bf_mercury_uranus():
    # Test case: Planets are Mercury and Uranus, expecting Venus, Earth, Mars, Jupiter, Saturn
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_invalid_planet1():
    # Test case: Invalid planet name for planet1, expecting empty tuple
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    # Test case: Invalid planet name for planet2, expecting empty tuple
    assert bf("Jupiter", "Pluto") == ()

def test_bf_same_planet():
    # Test case: Same planet name for both planets, expecting empty tuple
    assert bf("Earth", "Earth") == ()

def test_bf_mercury_neptune():
    # Test case: Planets are Mercury and Neptune, expecting all planets in between
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_mars_saturn():
    # Test case: Planets are Mars and Saturn, expecting Jupiter
    assert bf("Mars", "Saturn") == ("Jupiter",)

def test_bf_venus_earth():
    # Test case: Planets are Venus and Earth, expecting empty tuple (adjacent planets)
    assert bf("Venus", "Earth") == ()

def test_bf_earth_venus():
    # Test case: Planets are Earth and Venus, expecting empty tuple (adjacent planets, reversed order)
    assert bf("Earth", "Venus") == ()

def test_bf_mercury_venus():
    # Test case: Planets are Mercury and Venus, expecting empty tuple (adjacent planets)
    assert bf("Mercury", "Venus") == ()

def test_bf_neptune_uranus():
    # Test case: Planets are Neptune and Uranus, expecting empty tuple (adjacent planets)
    assert bf("Neptune", "Uranus") == ()

def test_bf_first_and_last():
    # Test case: Planets are Mercury and Neptune, expecting all planets in between
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_planet2_later():
    # Test case: planet1 is later in the list than planet2
    assert bf("Venus", "Earth") == ()