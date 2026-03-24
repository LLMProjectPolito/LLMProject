
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

# STEP 1: REASONING
# The function `bf` takes two planet names and returns a tuple of planets
# whose orbits lie between the given two planets, sorted by proximity to the sun.
# It handles invalid planet names by returning an empty tuple.
# The order of planets is fixed: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
# We need to test various scenarios including valid and invalid planet names,
# different orderings of input planets, and edge cases like planets being adjacent.

# STEP 2: PLAN
# Test cases:
# 1. Valid planets, intermediate order: bf("Jupiter", "Neptune")
# 2. Valid planets, reverse order: bf("Neptune", "Jupiter")
# 3. Valid planets, adjacent order: bf("Earth", "Mercury")
# 4. Valid planets, starting from Mercury: bf("Mercury", "Uranus")
# 5. Invalid planet name: bf("Jupiter", "Pluto")
# 6. Invalid planet name: bf("Pluto", "Neptune")
# 7. Same planet names: bf("Earth", "Earth")
# 8. Planets at the ends: bf("Mercury", "Neptune")
# 9. Planets close to the sun: bf("Venus", "Earth")

# STEP 3: CODE
###
def test_valid_intermediate():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_valid_reverse():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")

def test_valid_adjacent():
    assert bf("Earth", "Mercury") == ("Venus")

def test_valid_starting_mercury():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_invalid_planet_name_1():
    assert bf("Jupiter", "Pluto") == ()

def test_invalid_planet_name_2():
    assert bf("Pluto", "Neptune") == ()

def test_same_planet_names():
    assert bf("Earth", "Earth") == ()

def test_planets_at_the_ends():
    assert bf("Mercury", "Neptune") == ()

def test_planets_close_to_sun():
    assert bf("Venus", "Earth") == ("Mercury",)