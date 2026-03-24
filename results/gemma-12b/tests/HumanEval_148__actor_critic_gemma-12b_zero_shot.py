
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
from your_module import bf  # Replace your_module

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_valid_planets():
    """Tests with valid planet names where planet1 comes before planet2."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Mars", "Jupiter") == ("Earth", "Venus")
    assert bf("Saturn", "Uranus") == ("Jupiter",)

@pytest.mark.parametrize(
    "planet1, planet2",
    [
        ("Pluto", "Neptune"),
        ("Jupiter", "Pluto"),
        ("Invalid", "Neptune"),
        ("Jupiter", "Invalid"),
        ("Invalid1", "Invalid2"),
        ("Earth", "Earth"),
    ],
)
def test_bf_invalid_planets(planet1, planet2):
    """Tests with invalid planet names."""
    assert bf(planet1, planet2) == ()

def test_bf_planet1_after_planet2():
    """Tests where planet1 comes after planet2 in the planets list."""
    assert bf("Neptune", "Mercury") == ()
    assert bf("Uranus", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Saturn", "Earth") == ("Venus", "Mars", "Jupiter")
    assert bf("Jupiter", "Mars") == ("Earth", "Venus")
    assert bf("Mars", "Venus") == ("Earth",)
    assert bf("Venus", "Mercury") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_edge_cases():
    """Tests edge cases where one planet is at the beginning or end of the list."""
    assert bf("Mercury", "Neptune") == planets[1:]
    assert bf("Neptune", "Mercury") == ()
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_identical_planets():
    """Tests where both planets are the same."""
    assert bf("Mercury", "Mercury") == ()