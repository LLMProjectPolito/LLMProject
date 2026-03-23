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
    bf("Earth", "Mercury") ==> ("Venus",)
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planets or planet2 not in planets:
        return ()

    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    start = min(index1, index2) + 1
    end = max(index1, index2)

    between_planets = planets[start:end]
    return tuple(between_planets)

class TestBF:
    def test_jupiter_neptune(self):
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    def test_earth_mercury(self):
        assert bf("Earth", "Mercury") == ("Venus",)

    def test_mercury_uranus(self):
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

    def test_neptune_mars(self):
        assert bf("Neptune", "Mars") == ("Uranus", "Saturn", "Jupiter", "Earth", "Venus")

    def test_same_planet(self):
        assert bf("Earth", "Earth") == ()

    def test_invalid_planet1(self):
        assert bf("Pluto", "Venus") == ()

    def test_invalid_planet2(self):
        assert bf("Venus", "Pluto") == ()

    def test_invalid_both(self):
        assert bf("Pluto", "Ceres") == ()

    def test_mercury_mercury(self):
        assert bf("Mercury", "Mercury") == ()

    def test_neptune_neptune(self):
        assert bf("Neptune", "Neptune") == ()

    def test_venus_jupiter(self):
        assert bf("Venus", "Jupiter") == ("Earth", "Mars", "Saturn")