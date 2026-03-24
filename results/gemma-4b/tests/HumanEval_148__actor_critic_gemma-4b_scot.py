
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
    try:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
    except ValueError:
        return ()

    if idx1 >= idx2:
        return ()

    result = []
    for i in range(idx1 + 1, idx2):
        result.append(planets[i])

    return tuple(result)

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `bf` takes two planet names and returns a tuple of planets
# whose orbits lie between the given two planets, sorted by proximity to the sun.
# It handles invalid planet names by returning an empty tuple.
# Edge cases include:
#   - planet1 and planet2 are the same.
#   - planet1 is before planet2.
#   - planet1 is after planet2.
#   - planet1 or planet2 are invalid planet names.
#   - The range of planets between planet1 and planet2 is empty.

# STEP 2: PLAN - List test functions names and scenarios.
# test_bf_valid_input
# test_bf_same_planets
# test_bf_planet1_before_planet2
# test_bf_planet1_after_planet2
# test_bf_invalid_planet_name
# test_bf_empty_orbit_range

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_bf_valid_input():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_same_planets():
    assert bf("Earth", "Earth") == ()

def test_bf_planet1_before_planet2():
    assert bf("Mercury", "Venus") == ("Earth", "Mars")

def test_bf_planet1_after_planet2():
    assert bf("Venus", "Mercury") == ()

def test_bf_invalid_planet_name():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Pluto") == ()

def test_bf_empty_orbit_range():
    assert bf("Venus", "Venus") == ()
    assert bf("Mercury", "Venus") == ()