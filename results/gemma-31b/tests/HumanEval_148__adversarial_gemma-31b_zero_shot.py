
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

# The function to be tested
def bf(planet1, planet2):
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    start = min(idx1, idx2)
    end = max(idx1, idx2)
    
    return planets[start + 1 : end]

class TestPlanetBetween:
    """
    Blue Team QA Suite for bf() function.
    Focuses on boundary conditions, input validation, and ordering.
    """

    @pytest.mark.parametrize("p1, p2, expected", [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Earth", "Mercury", ("Venus",)),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ])
    def test_standard_cases(self, p1, p2, expected):
        """Verify provided examples and basic functionality."""
        assert bf(p1, p2) == expected

    @pytest.mark.parametrize("p1, p2", [
        ("Mercury", "Venus"),
        ("Venus", "Earth"),
        ("Earth", "Mars"),
        ("Mars", "Jupiter"),
        ("Jupiter", "Saturn"),
        ("Saturn", "Uranus"),
        ("Uranus", "Neptune"),
    ])
    def test_adjacent_planets(self, p1, p2):
        """Planets immediately next to each other should return an empty tuple."""
        assert bf(p1, p2) == ()
        assert bf(p2, p1) == ()

    @pytest.mark.parametrize("planet", [
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
    ])
    def test_same_planet(self, planet):
        """Providing the same planet twice should return an empty tuple."""
        assert bf(planet, planet) == ()

    @pytest.mark.parametrize("p1, p2", [
        ("Pluto", "Earth"),       # Former planet
        ("Mars", "Sun"),          # Star, not planet
        ("Earth", "Moon"),        # Satellite, not planet
        ("Jupiter", "Xenon"),     # Random string
        ("", "Mercury"),          # Empty string
        ("Earth", "EARTH"),       # Case sensitivity check
        (None, "Mars"),           # None type
        (123, "Venus"),           # Integer type
    ])
    def test_invalid_inputs(self, p1, p2):
        """Any invalid planet name or data type should result in an empty tuple."""
        assert bf(p1, p2) == ()

    def test_full_range(self):
        """Test the maximum possible range (Mercury to Neptune)."""
        expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        assert bf("Mercury", "Neptune") == expected
        assert bf("Neptune", "Mercury") == expected

    def test_symmetry(self):
        """Ensure that bf(a, b) always equals bf(b, a)."""
        p1, p2 = "Earth", "Neptune"
        assert bf(p1, p2) == bf(p2, p1)