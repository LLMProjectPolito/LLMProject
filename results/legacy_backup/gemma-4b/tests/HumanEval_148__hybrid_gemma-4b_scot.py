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
# whose orbits lie between the two input planets, sorted by proximity to the sun.
# It handles invalid planet names by returning an empty tuple.
# The order of planets in the solar system is fixed.
# We need to test various scenarios including valid and invalid planet names,
# different orderings of input planets, and edge cases like planets being adjacent.

# STEP 2: PLAN
# Test cases:
# 1. Valid input, planets in correct order: ("Saturn", "Uranus")
# 2. Valid input, planets in reverse order: ()
# 3. Valid input, planets adjacent: ("Venus")
# 4. Valid input, planet1 is Mercury, planet2 is Uranus: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
# 5. Invalid planet name: ()
# 6. Invalid planet name for both: ()
# 7. planet1 is Neptune, planet2 is Mercury: ()
# 8. planet1 is Venus, planet2 is Earth: ("Mars", "Jupiter", "Saturn", "Uranus")

# Test function names:
# test_bf_valid_order, test_bf_reverse_order, test_bf_adjacent, test_bf_mercury_uranus, test_bf_invalid_planet, test_bf_invalid_both, test_bf_neptune_mercury, test_bf_venus_earth


# STEP 3: CODE
###
def test_bf_valid_order():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_reverse_order():
    assert bf("Earth", "Mercury") == ()

def test_bf_adjacent():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_mercury_uranus():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_invalid_planet():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_both():
    assert bf("Pluto", "Pluto") == ()

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ()

def test_bf_venus_earth():
    assert bf("Venus", "Earth") == ("Mars", "Jupiter", "Saturn", "Uranus")