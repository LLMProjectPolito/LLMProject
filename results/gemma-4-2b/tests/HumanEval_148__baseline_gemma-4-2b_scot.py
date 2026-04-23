
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
# The function `bf` takes two planet names as input and returns a tuple of planets
# located between the orbits of the two input planets, sorted by proximity to the sun.
# The planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
# If either planet name is invalid, an empty tuple is returned.
# The test suite should cover various scenarios:
# 1. Valid input: planets in ascending order.
# 2. Valid input: planets in descending order.
# 3. Valid input: planets with different order.
# 4. Invalid input: one or both planets are invalid.
# 5. Edge cases: planets close to each other in the order.

# STEP 2: PLAN
# test_bf_ascending_order
# test_bf_descending_order
# test_bf_different_order
# test_bf_invalid_planet1
# test_bf_invalid_planet2
# test_bf_edge_case_close_planets

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

    if planet1 < planet2:
        between_planets = [p for p in planets if planet1 < p < planet2]
    else:
        between_planets = [p for p in planets if planet2 < p < planet1]

    return tuple(between_planets)


def test_bf_ascending_order():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_descending_order():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_different_order():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Mercury", "Pluto") == ()

def test_bf_edge_case_close_planets():
    assert bf("Mars", "Jupiter") == ("Earth", "Venus")