
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

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ()
    assert bf("Saturn", "Jupiter") == ()
    assert bf("Neptune", "Saturn") == ("Uranus",)
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("X", "Earth") == ()
    assert bf("Earth", "X") == ()
    with pytest.raises(ValueError):
        bf("123", "Mars")
    with pytest.raises(ValueError):
        bf("Mars", "456")
    with pytest.raises(ValueError):
        bf("Pluto", "X")
    with pytest.raises(ValueError):
        bf("123", "456")

def test_bf_empty_string():
    with pytest.raises(ValueError):
        bf("", "Earth")
    with pytest.raises(ValueError):
        bf("Jupiter", "")
    with pytest.raises(ValueError):
        bf("", "")

def test_bf_case_insensitivity():
    assert bf("jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_planets_at_edges():
    assert bf("Mercury", "Venus") == ()
    assert bf("Neptune", "Uranus") == ()

def test_bf_invalid_input_types():
    with pytest.raises(TypeError):
        bf(123, "Earth")
    with pytest.raises(TypeError):
        bf("Earth", 456)
    with pytest.raises(TypeError):
        bf(None, "Earth")
    with pytest.raises(TypeError):
        bf("Earth", None)
    with pytest.raises(TypeError):
        bf(123, 456)
    with pytest.raises(TypeError):
        bf(None, None)

def test_bf_long_planet_names():
    with pytest.raises(ValueError):
        bf("Mercury" * 10, "Venus")
    with pytest.raises(ValueError):
        bf("Venus", "Neptune" * 10)

def test_bf_adjacent_reverse():
    assert bf("Venus", "Earth") == ()