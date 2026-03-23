# STEP 1: REASONING
# The goal is to create a comprehensive pytest suite for the `bf` function.
# The function takes two planet names as input and returns a tuple of planets
# between them in their orbital order. We need to test various scenarios:
# - Valid planet names in different orders.
# - Invalid planet names.
# - Edge cases where one of the planets is the first or last.
# - Cases where the input planets are the same.
# The tests should verify the correctness of the returned tuple, including
# the order and the planets included.

# STEP 2: PLAN
# 1. test_valid_planets_normal_order: Test with valid planet names in normal order (e.g., "Jupiter", "Neptune").
# 2. test_valid_planets_reverse_order: Test with valid planet names in reverse order (e.g., "Earth", "Mercury").
# 3. test_valid_planets_wide_range: Test with a wide range of planets (e.g., "Mercury", "Uranus").
# 4. test_invalid_planet1: Test with an invalid planet1 name.
# 5. test_invalid_planet2: Test with an invalid planet2 name.
# 6. test_invalid_planets_both: Test with both planet names invalid.
# 7. test_same_planet: Test with the same planet name for both inputs.
# 8. test_first_planet: Test with the first planet as input.
# 9. test_last_planet: Test with the last planet as input.
# 10. test_adjacent_planets: Test with adjacent planets.

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

    start_index = planets.index(planet1)
    end_index = planets.index(planet2)

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    result = tuple(planets[start_index + 1:end_index])
    return result

@pytest.mark.parametrize("planet1, planet2, expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Venus", ()),
])
def test_valid_planets(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

@pytest.mark.parametrize("planet1, planet2", [
    ("Pluto", "Neptune"),
    ("Jupiter", "Alpha Centauri"),
])
def test_invalid_planets(planet1, planet2):
    assert bf(planet1, planet2) == ()

@pytest.mark.parametrize("planet1, planet2", [
    ("Invalid", "Invalid"),
])
def test_invalid_planets_both(planet1, planet2):
    assert bf(planet1, planet2) == ()

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_first_planet():
    assert bf("Mercury", "Venus") == ("Venus",)

def test_last_planet():
    assert bf("Neptune", "Uranus") == ("Uranus",)

def test_adjacent_planets():
    assert bf("Earth", "Mars") == ("Mars",)