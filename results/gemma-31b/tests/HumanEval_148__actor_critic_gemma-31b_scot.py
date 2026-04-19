
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

# The function bf is assumed to be defined in the environment.

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard cases: Forward order
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Mars", ("Venus", "Earth")),
    ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
    
    # Standard cases: Backward order (should still be sorted by sun proximity)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Saturn", "Venus", ("Earth", "Mars", "Jupiter")),
    
    # Wide range
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Edge cases: Adjacent planets (no planets between them)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Edge cases: Same planet
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Xenon", "Ytterbium", ()),
    ("Mars", "Sun", ()),
    
    # Case sensitivity: Exact match is required per "correct planet names"
    ("earth", "mercury", ()),
    ("EARTH", "MARS", ()),
    ("earth", "Mars", ()),
    ("Earth", "earth", ()), # Boundary case: Mixed case for the same planet
])
def test_bf_logic(p1, p2, expected):
    """Test the core logic of the bf function with various valid and invalid inputs."""
    # Call the function once and store the result to improve efficiency
    result = bf(p1, p2)
    # The equality check implicitly verifies that the result is a tuple
    assert result == expected

def test_bf_non_string_inputs():
    """Test how the function handles non-string inputs."""
    # Based on the prompt "return empty tuple if not correct planet names"
    assert bf(1, "Earth") == ()
    assert bf("Earth", None) == ()
    assert bf(None, None) == ()

def test_bf_empty_strings():
    """Test how the function handles empty strings."""
    assert bf("", "Earth") == ()
    assert bf("Earth", "") == ()
    assert bf("", "") == ()