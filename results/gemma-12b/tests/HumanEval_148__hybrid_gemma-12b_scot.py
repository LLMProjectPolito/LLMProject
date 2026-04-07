
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

def get_planet_index(planet_name):
    """Helper function to get the index of a planet in the planets list."""
    try:
        return planets.index(planet_name)
    except ValueError:
        return -1

class TestBF:
    @pytest.mark.parametrize("planet1, planet2, expected", [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Earth", "Mercury", ("Venus",)),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Neptune", "Jupiter", ("Uranus", "Saturn")),
        ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
        ("Mercury", "Mercury", ()),
        ("Earth", "Earth", ()),
        ("Neptune", "Mercury", ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
        ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ])
    def test_valid_planets_between(self, planet1, planet2, expected):
        """Tests valid planet combinations with planets in between."""
        result = bf(planet1, planet2)
        assert result == expected

    def test_adjacent_planets(self):
        """Tests adjacent planets."""
        assert bf("Earth", "Mercury") == ("Venus",)

    def test_planets_at_edges(self):
        """Tests planets at the edges of the solar system."""
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

    def test_same_planet(self):
        """Tests when both planets are the same."""
        assert bf("Earth", "Earth") == ()

    @pytest.mark.parametrize("planet1, planet2, expected", [
        ("Pluto", "Neptune", ()),
        ("Jupiter", "Xantus", ()),
        ("Pluto", "Xantus", ()),
    ])
    def test_invalid_planet_name(self, planet1, planet2, expected):
        """Tests invalid planet names."""
        assert bf(planet1, planet2) == expected

    def test_case_sensitivity(self):
        """Tests case sensitivity."""
        assert bf("earth", "mercury") == ("venus",)
        assert bf("Jupiter", "neptune") == ("Saturn", "Uranus")