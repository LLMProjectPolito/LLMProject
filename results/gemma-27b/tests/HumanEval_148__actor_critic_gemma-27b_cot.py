
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

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def test_bf_valid_planets_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_valid_planets_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_valid_planets_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_valid_planets_venus_mars():
    assert bf("Venus", "Mars") == ("Earth",)

def test_bf_valid_planets_mars_venus():
    assert bf("Mars", "Venus") == ()

def test_bf_valid_planets_saturn_jupiter():
    assert bf("Saturn", "Jupiter") == ()

def test_bf_valid_planets_neptune_saturn():
    assert bf("Neptune", "Saturn") == ("Uranus",)

def test_bf_valid_planets_mercury_neptune():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_valid_planets_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_valid_planets_neptune_neptune():
    assert bf("Neptune", "Neptune") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("X", "Earth") == ()
    assert bf("123", "Mars") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Earth", "X") == ()
    assert bf("Mars", "123") == ()

def test_bf_empty_string():
    assert bf("", "Earth") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_case_insensitive():
    assert bf("jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Jupiter", "neptune") == ("Saturn", "Uranus")
    assert bf("jupiter", "neptune") == ("Saturn", "Uranus")

def test_bf_planets_at_edges():
    assert bf("Mercury", "Venus") == ()
    assert bf("Neptune", "Uranus") == ()

def test_bf_long_string():
    assert bf("Mercury" * 100, "Neptune") == ()
    assert bf("Neptune", "Venus" * 100) == ()

def test_bf_invalid_input_types():
    assert bf(123, 456) == ()
    assert bf(None, "Earth") == ()
    assert bf("Earth", None) == ()
    assert bf(123, None) == ()

def test_bf_all_planets():
    for planet1 in planets:
        for planet2 in planets:
            if planet1 == planet2:
                assert bf(planet1, planet2) == ()
            else:
                result = bf(planet1, planet2)
                if planet1 < planet2:
                    expected = tuple(p for p in planets if planet1 < p < planet2)
                else:
                    expected = tuple(p for p in planets if planet2 < p < planet1)
                assert result == expected

def test_bf_reverse_order():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Saturn", "Earth") == ("Uranus", "Neptune")
    assert bf("Mars", "Mercury") == ("Earth", "Venus")