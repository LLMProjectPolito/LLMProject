
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

def test_bf_provided_examples():
    """Tests the specific examples provided in the docstring."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_reversed_order():
    """Tests that the order of input planets does not change the resulting tuple."""
    # Neptune to Jupiter should return the same as Jupiter to Neptune
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    # Mercury to Earth should return the same as Earth to Mercury
    assert bf("Mercury", "Earth") == ("Venus",)

def test_bf_adjacent_planets():
    """Tests planets that are next to each other (should return an empty tuple)."""
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Earth") == ()
    assert bf("Earth", "Mars") == ()
    assert bf("Mars", "Jupiter") == ()
    assert bf("Jupiter", "Saturn") == ()
    assert bf("Saturn", "Uranus") == ()
    assert bf("Uranus", "Neptune") == ()

def test_bf_same_planet():
    """Tests when both input planets are the same."""
    assert bf("Mars", "Mars") == ()
    assert bf("Jupiter", "Jupiter") == ()

def test_bf_invalid_planet_names():
    """Tests that invalid planet names return an empty tuple."""
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Mars-ish") == ()
    assert bf("Sun", "Moon") == ()
    assert bf("", "Mercury") == ()
    assert bf("Jupiter", "Jupiterr") == ()

def test_bf_case_sensitivity():
    """
    Tests if the function is case-sensitive. 
    Based on the prompt, planet names are specific strings.
    """
    # If the function expects exact matches, lowercase should return empty tuple
    assert bf("jupiter", "neptune") == ()
    assert bf("JUPITER", "NEPTUNE") == ()

@pytest.mark.parametrize("p1, p2, expected", [
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
    ("Mars", "Uranus", ("Jupiter", "Saturn")),
])
def test_bf_various_ranges(p1, p2, expected):
    """Parametrized test for various valid ranges."""
    assert bf(p1, p2) == expected