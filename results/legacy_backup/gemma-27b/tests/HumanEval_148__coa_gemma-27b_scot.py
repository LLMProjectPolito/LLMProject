import pytest
import math


# Focus: Valid/Invalid Planet Names
import pytest

def test_valid_planet_names():
    """
    Test cases to verify the function returns an empty tuple when given invalid planet names.
    """
    assert bf("Pluto", "X") == ()
    assert bf("Invalid", "Earth") == ()
    assert bf("Earth", "InvalidPlanet") == ()
    assert bf("FakePlanet1", "FakePlanet2") == ()

def test_valid_planet_names_mixed_case():
    """
    Test cases to verify the function handles planet names with mixed casing.
    """
    assert bf("jupiter", "Neptune") == ()
    assert bf("Earth", "neptune") == ()
    assert bf("mercury", "Venus") == ()

def test_valid_planet_names_empty_strings():
    """
    Test cases to verify the function handles empty strings as planet names.
    """
    assert bf("", "Earth") == ()
    assert bf("Earth", "") == ()
    assert bf("", "") == ()

# Focus: Order of Planets (planet1 & planet2)
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

    start = min(index1, index2) + 1
    end = max(index1, index2)

    between_planets = tuple(planets[start:end])
    return between_planets

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function 'bf' aims to return planets between two given planets in their orbital order.
# We need to test various orderings of planet1 and planet2, including cases where planet1 is before planet2,
# planet1 is after planet2, and invalid planet names are provided.

# STEP 2: PLAN - List test functions names and scenarios.
# test_order_planet1_before_planet2: planet1 comes before planet2 in the solar system.
# test_order_planet2_before_planet1: planet2 comes before planet1 in the solar system.
# test_invalid_planet_names:  One or both planet names are invalid.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_order_planet1_before_planet2():
    assert bf("Earth", "Mars") == ("Venus",)
    assert bf("Mercury", "Venus") == ()
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_order_planet2_before_planet1():
    assert bf("Mars", "Earth") == ("Venus",)
    assert bf("Venus", "Mercury") == ()
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert bf("Uranus", "Mercury") == ("Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_invalid_planet_names():
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Xyz") == ()
    assert bf("Pluto", "Xyz") == ()
    assert bf("Earth", "earth") == () #case sensitivity

# Focus: Edge Cases (same planet, planets at extremes)
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

    start = min(index1, index2) + 1
    end = max(index1, index2)

    between_planets = tuple(planets[start:end])
    return between_planets

# Test functions
def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_planets_at_extremes():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_planets_at_extremes_reversed():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")