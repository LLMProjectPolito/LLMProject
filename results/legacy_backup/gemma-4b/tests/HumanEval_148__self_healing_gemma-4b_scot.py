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
# STEP 1: REASONING - The function `bf` takes two planet names and returns a tuple of planets between their orbits, sorted by proximity to the sun.  Invalid planet names should return an empty tuple.  The order of planets is fixed.
# STEP 2: PLAN -
# - Test cases for valid planet names and correct order.
# - Test cases for invalid planet names.
# - Test cases where planet1 is closer to the sun than planet2.
# - Test cases where planet1 is further from the sun than planet2.
# - Test cases with planets at the boundaries.
# STEP 3: CODE -
###
def test_bf_valid_input():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Earth") == ("Mars")
    assert bf("Mars", "Jupiter") == ("Saturn")

def test_bf_invalid_planet_name():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("NonExistent", "Neptune") == ()
    assert bf("Earth", "NonExistent") == ()

def test_bf_planet1_closer():
    assert bf("Mercury", "Venus") == ("Earth")

def test_bf_planet1_further():
    assert bf("Venus", "Mercury") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_adjacent_planets():
    assert bf("Mars", "Jupiter") == ("Saturn")

def test_bf_empty_list():
    assert bf("Mercury", "Mercury") == ()