import pytest
import math

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

def test_basic():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

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
# The function `bf` filters planets between two given planets.
# An edge case is when planet1 and planet2 are the same, or planet1 is after planet2 in the list.
# Another edge case is when either planet1 or planet2 is not a valid planet name.
# The function should return an empty tuple in these cases.

# STEP 2: PLAN - List test functions names and scenarios.
# test_same_planets: planet1 == planet2
# test_planet1_after_planet2: planet1 is after planet2
# test_invalid_planet1: planet1 is not a valid planet name
# test_invalid_planet2: planet2 is not a valid planet name
# test_valid_range: planet1 and planet2 are valid and within the range

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_same_planets():
    assert bf("Jupiter", "Jupiter") == ()

def test_planet1_after_planet2():
    assert bf("Neptune", "Mercury") == ()

def test_invalid_planet1():
    assert bf("Pluto", "Mercury") == ()

def test_invalid_planet2():
    assert bf("Earth", "Pluto") == ()

def test_valid_range():
    assert bf("Mercury", "Venus") == ("Earth",)
    assert bf("Earth", "Mars") == ("Venus", "Mars")
    assert bf("Mars", "Jupiter") == ("Venus", "Earth", "Mars", "Jupiter")
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

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
    if planet1 > planet2:
        planet1, planet2 = planet2, planet1
    result = []
    for planet in planets:
        if planet > planet1 and planet < planet2:
            result.append(planet)
    return tuple(result)

### SCoT Steps:
# STEP 1: REASONING - The function should return an empty tuple if either planet1 or planet2 is not a valid planet name.
# STEP 2: PLAN - Test with an invalid planet name.
# STEP 3: CODE -
def test_invalid_planet_name():
    assert bf("Pluto", "Neptune") == ()