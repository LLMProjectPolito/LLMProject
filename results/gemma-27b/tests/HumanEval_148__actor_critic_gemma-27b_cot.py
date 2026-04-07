
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

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus"), "Should return Saturn and Uranus"
    assert bf("Earth", "Mercury") == ("Venus"), "Should return Venus"
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Should return Venus, Earth, Mars, Jupiter, Saturn"
    assert bf("Venus", "Mars") == ("Earth"), "Should return Earth"
    assert bf("Mars", "Venus") == (), "Should return empty tuple"
    assert bf("Saturn", "Jupiter") == (), "Should return empty tuple"
    assert bf("Neptune", "Saturn") == ("Uranus"), "Should return Uranus"
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Should return all planets between Mercury and Neptune"
    assert bf("Mercury", "Mercury") == (), "Should return empty tuple for same planet"
    assert bf("Neptune", "Neptune") == (), "Should return empty tuple for same planet"

def test_bf_invalid_planet():
    invalid_planets = ["Pluto", "X", "123", ""]
    for planet in invalid_planets:
        assert bf(planet, "Earth") == (), f"Should return empty tuple with invalid planet1: {planet}"
        assert bf("Earth", planet) == (), f"Should return empty tuple with invalid planet2: {planet}"

def test_bf_empty_string():
    assert bf("", "Earth") == (), "Should return empty tuple with empty planet1"
    assert bf("Jupiter", "") == (), "Should return empty tuple with empty planet2"
    assert bf("", "") == (), "Should return empty tuple with both empty"

def test_bf_case_sensitivity():
    assert bf("jupiter", "Neptune") == (), "Should return empty tuple for lowercase planet1"
    assert bf("Jupiter", "neptune") == (), "Should return empty tuple for lowercase planet2"
    assert bf("jupiter", "neptune") == (), "Should return empty tuple for both lowercase"

def test_bf_planets_out_of_order():
    expected = ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Neptune", "Mercury") == expected, "Should return planets in reverse order"

def test_bf_multiple_planets_between():
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Jupiter") == expected, "Should return a longer chain of planets"

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == (), "Should return empty tuple for adjacent planets"
    assert bf("Mars", "Earth") == (), "Should return empty tuple for adjacent planets in reverse order"

def test_bf_none_inputs():
    assert bf(None, "Earth") == (), "Should return empty tuple with planet1 as None"
    assert bf("Jupiter", None) == (), "Should return empty tuple with planet2 as None"
    assert bf(None, None) == (), "Should return empty tuple with both planets as None"

def test_bf_first_and_last_planets():
    assert bf("Mercury", "Mars") == ("Venus", "Earth"), "Should return planets between Mercury and Mars"
    assert bf("Saturn", "Neptune") == ("Uranus"), "Should return planets between Saturn and Neptune"