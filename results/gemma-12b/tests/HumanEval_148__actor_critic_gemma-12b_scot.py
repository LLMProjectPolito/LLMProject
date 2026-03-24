
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

    if index1 > index2:
        return ()

    result = tuple(planets[index1 + 1:index2])
    return result

class TestBF:
    def test_venus_neptune(self):
        assert bf("Venus", "Neptune") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    def test_mars_jupiter(self):
        assert bf("Mars", "Jupiter") == ("Venus",)

    def test_jupiter_neptune(self):
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    def test_invalid_order(self):
        assert bf("Neptune", "Jupiter") == ()

    def test_adjacent_planets(self):
        assert bf("Earth", "Mars") == ("Venus",)

    def test_invalid_planet1(self):
        assert bf("Pluto", "Neptune") == ()

    def test_invalid_planet2(self):
        assert bf("Jupiter", "Pluto") == ()

    def test_both_invalid(self):
        assert bf("Pluto", "Ceres") == ()

    def test_edge_case_mercury_neptune(self):
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    def test_edge_case_neptune_mercury(self):
        assert bf("Neptune", "Mercury") == ()

    def test_earth_jupiter(self):
        assert bf("Earth", "Jupiter") == ("Mars", "Saturn")

    def test_case_sensitivity(self):
        assert bf("earth", "Neptune") == ()