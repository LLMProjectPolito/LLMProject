
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

@pytest.mark.parametrize("p1, p2, expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Venus", ("Earth",)),
    ("Saturn", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Mercury", "Venus", ()),
    ("Earth", "Earth", ()),
])
def test_bf_valid_planets(p1, p2, expected):
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),
    ("Earth", "Pluto"),
    ("Mars", "Sun"),
    ("Moon", "Neptune"),
    ("Invalid", "Invalid"),
    ("", "Mercury"),
    ("Jupiter", ""),
    (None, "Earth"),
    ("Earth", None),
])
def test_bf_invalid_planets(p1, p2):
    assert bf(p1, p2) == ()

def test_bf_case_sensitivity():
    # Assuming the function is case-sensitive based on the prompt's capitalization
    assert bf("mercury", "Earth") == ()
    assert bf("MERCURY", "EARTH") == ()