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

class TestBF:
    def test_valid_planets_between(self):
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    def test_adjacent_planets(self):
        assert bf("Earth", "Mercury") == ("Venus",)

    def test_planets_at_edges(self):
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

    def test_same_planet(self):
        assert bf("Earth", "Earth") == ()

    def test_invalid_planet_name(self):
        assert bf("Pluto", "Neptune") == ()
        assert bf("Jupiter", "Xantus") == ()
        assert bf("Invalid", "Mercury") == ()

    def test_planet1_further_than_planet2(self):
        assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")

    def test_empty_tuple_return(self):
        assert bf("Mercury", "Venus") == ()

    def test_case_sensitivity(self):
        assert bf("earth", "mercury") == ()
        assert bf("Jupiter", "neptune") == ("Saturn", "Uranus")