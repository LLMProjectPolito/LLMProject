
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
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
    except ValueError:
        return ()

    if index1 >= index2:
        return ()

    result = []
    for i in range(index1 + 1, index2):
        result.append(planets[i])

    return tuple(result)

### STEP 1: REASONING
# The function `bf` takes two planet names as input and returns a tuple of planets
# whose orbits lie between the two input planets, sorted by proximity to the sun.
# We need to test various scenarios including valid planet names, invalid planet names,
# planets in different orders, and edge cases like planets being adjacent.

### STEP 2: PLAN
# Test cases:
# 1. Valid planets, orbits in correct order: ("Saturn", "Uranus")
# 2. Valid planets, orbits in reverse order: ()
# 3. Valid planets, planets adjacent: ()
# 4. Valid planets, planet1 is Mercury: ("Venus")
# 5. Valid planets, planet1 is Earth: ("Mars", "Jupiter", "Saturn")
# 6. Invalid planet name: ()
# 7. planet1 is invalid, planet2 is valid: ()
# 8. planet1 is valid, planet2 is invalid: ()
# 9. planet1 and planet2 are invalid: ()

### STEP 3: CODE
def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_jupiter_jupiter():
    assert bf("Jupiter", "Jupiter") == ()

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ()

def test_bf_invalid_planet():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet_invalid_planet():
    assert bf("Pluto", "Pluto") == ()

def test_bf_valid_planet_invalid_planet():
    assert bf("Earth", "Pluto") == ()

def test_bf_invalid_planet_valid_planet():
    assert bf("Pluto", "Earth") == ()

def test_bf_adjacent_planets():
    assert bf("Venus", "Earth") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()