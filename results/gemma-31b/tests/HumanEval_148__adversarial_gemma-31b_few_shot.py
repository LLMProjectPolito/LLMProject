
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

def test_bf_examples():
    """Test the examples provided in the docstring."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_adjacent_planets():
    """Planets immediately next to each other should return an empty tuple."""
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Uranus", "Neptune") == ()

def test_bf_same_planet():
    """Providing the same planet twice should return an empty tuple."""
    assert bf("Mars", "Mars") == ()

def test_bf_full_span():
    """Test the maximum possible range."""
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected

def test_bf_invalid_planet_names():
    """Test that invalid planet names return an empty tuple."""
    # Typo
    assert bf("Jupitrr", "Neptune") == ()
    # Pluto (not in the provided list of eight)
    assert bf("Pluto", "Earth") == ()
    # Random string
    assert bf("Mars", "Pizza") == ()
    # Empty string
    assert bf("", "Earth") == ()

def test_bf_case_sensitivity():
    """
    Test how the function handles case sensitivity. 
    Based on the prompt, planet names are capitalized.
    """
    assert bf("mercury", "Earth") == ()
    assert bf("MERCURY", "EARTH") == ()

def test_bf_type_safety():
    """Test that non-string inputs are handled gracefully."""
    assert bf(None, "Earth") == ()
    assert bf(123, 456) == ()
    assert bf(["Earth"], "Mars") == ()

@pytest.mark.parametrize("p1, p2, expected", [
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Saturn", ("Jupiter",)),
    ("Earth", "Jupiter", ("Mars",)),
])
def test_bf_various_ranges(p1, p2, expected):
    """Parametrized test for various mid-range combinations."""
    assert bf(p1, p2) == expected