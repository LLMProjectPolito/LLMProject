
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

# STEP 1: REASONING
# The function `bf` takes two planet names as strings and returns a tuple of planets
# located between them in terms of proximity to the sun, sorted by proximity.
# The planets are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
# The function should handle invalid planet names by returning an empty tuple.
# The test suite needs to cover:
# 1. Valid planet names with planet1 before planet2.
# 2. Valid planet names with planet2 before planet1.
# 3. Valid planet names where planet1 and planet2 are adjacent.
# 4. Invalid planet names.
# 5. Edge cases like planet1 and planet2 being the same.

# STEP 2: PLAN
# Test functions:
# - test_valid_planets_planet1_before_planet2: Checks planets between Jupiter and Neptune.
# - test_valid_planets_planet2_before_planet1: Checks planets between Mercury and Earth.
# - test_valid_planets_adjacent: Checks planets between Earth and Mercury.
# - test_invalid_planet_names: Checks with invalid planet names.
# - test_same_planet_names: Checks when planet1 and planet2 are the same.
# - test_mercury_neptune: Checks the full range.

# STEP 3: CODE
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

    return tuple(planets[start:end])

class TestBF:
    def test_valid_planets_planet1_before_planet2(self):
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    def test_valid_planets_planet2_before_planet1(self):
        assert bf("Mercury", "Earth") == ("Venus",)

    def test_valid_planets_adjacent(self):
        assert bf("Earth", "Mercury") == ("Venus",)

    def test_invalid_planet_names(self):
        assert bf("Pluto", "Neptune") == ()
        assert bf("Jupiter", "Xantus") == ()
        assert bf("Pluto", "Xantus") == ()

    def test_same_planet_names(self):
        assert bf("Earth", "Earth") == ()

    def test_mercury_neptune(self):
        assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")