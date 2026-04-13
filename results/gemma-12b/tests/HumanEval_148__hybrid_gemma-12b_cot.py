
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

    if index1 >= index2:
        return ()

    between_planets = planets[index1 + 1:index2]
    return tuple(between_planets)

class TestBF:
    def test_valid_planets_1(self):
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    def test_valid_planets_2(self):
        assert bf("Earth", "Mercury") == ("Venus",)

    def test_valid_planets_3(self):
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

    def test_invalid_planet_1(self):
        assert bf("Pluto", "Neptune") == ()

    def test_invalid_planet_2(self):
        assert bf("Jupiter", "Pluto") == ()

    def test_invalid_planets_both(self):
        assert bf("Pluto", "Ceres") == ()

    def test_same_planet(self):
        assert bf("Earth", "Earth") == ()

    def test_planet1_after_planet2(self):
        assert bf("Neptune", "Mercury") == ()

    def test_edge_case_mercury_venus(self):
        assert bf("Mercury", "Venus") == ()

    def test_edge_case_venus_earth(self):
        assert bf("Venus", "Earth") == ()

    def test_edge_case_neptune_uranus(self):
        assert bf("Neptune", "Uranus") == ()