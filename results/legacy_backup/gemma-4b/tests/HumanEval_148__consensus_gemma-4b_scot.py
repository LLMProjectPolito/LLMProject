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
# whose orbits are between the two input planets, sorted by proximity to the sun.
# It handles invalid planet names by returning an empty tuple.
# The order of planets in the output tuple is important.

# STEP 2: PLAN - List test functions names and scenarios.
# test_bf_valid_input
# test_bf_invalid_input
# test_bf_same_planet
# test_bf_reverse_order
# test_bf_adjacent_planets
# test_bf_multiple_planets_between
# test_bf_no_planets_between

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_bf_valid_input():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_invalid_input():
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Earth", "Zorgon") == ()
    assert bf("Pluto", "Neptune") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_reverse_order():
    assert bf("Neptune", "Jupiter") == ()

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == ("Venus")

def test_bf_multiple_planets_between():
    assert bf("Mars", "Saturn") == ("Venus", "Earth", "Jupiter")

def test_bf_no_planets_between():
    assert bf("Mercury", "Venus") == ()