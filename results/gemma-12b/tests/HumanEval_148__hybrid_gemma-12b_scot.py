
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
from your_module import bf  # Replace your_module

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def get_planet_index(planet):
    """Helper function to get the index of a planet in the planets list."""
    try:
        return planets.index(planet)
    except ValueError:
        return -1

@pytest.fixture
def valid_planets():
    return planets

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


class TestBF:
    def test_valid_planets_between(self, valid_planets):
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    def test_adjacent_planets(self):
        assert bf("Earth", "Mercury") == ("Venus",)

    def test_planets_at_edges(self, valid_planets):
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

    def test_same_planet(self):
        assert bf("Earth", "Earth") == ()

    def test_invalid_planet_name(self):
        assert bf("Pluto", "Neptune") == ()
        assert bf("Jupiter", "Xantus") == ()
        assert bf("Pluto", "Xantus") == ()

    def test_planet1_further_than_planet2(self):
        assert bf("Neptune", "Mars") == ()

    def test_mercury_neptune(self, valid_planets):
        assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    def test_neptune_mercury(self):
        assert bf("Neptune", "Mercury") == ()

    def test_empty_result(self):
        assert bf("Uranus", "Uranus") == ()

    def test_case_sensitivity(self):
        assert bf("earth", "Neptune") == ()
        assert bf("Jupiter", "neptune") == ("Saturn", "Uranus")

    def test_both_invalid_planet_names(self):
        assert bf("Pluto", "Xena") == ()