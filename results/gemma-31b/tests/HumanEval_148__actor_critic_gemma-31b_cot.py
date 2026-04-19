
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
    # Standard cases from examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Order independence (p1 > p2 vs p1 < p2)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Edge cases: Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Earth", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Jupiter", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    
    # Edge cases: Same planet
    ("Earth", "Earth", ()),
    ("Mercury", "Mercury", ()),
    ("Neptune", "Neptune", ()),
    
    # Edge cases: First and last planets
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Edge cases: Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Mars", "Mars-ish", ()),
    ("", "Venus", ()),
    ("Jupiter", "", ()),
    ("JUPITER", "NEPTUNE", ()), 
    ("jupiter", "neptune", ()),

    # String Sanitization: Leading/trailing whitespace
    (" Earth ", "Mars", ()),
    ("Mercury", " Venus ", ()),
    (" Neptune", "Jupiter", ()),

    # Input Validation: Non-string types
    (None, "Earth", ()),
    ("Earth", None, ()),
    (123, "Mars", ()),
    ("Mars", 456, ()),
    ([], "Jupiter", ()),
    ("Jupiter", {}, ()),
    (True, False, ()),
])
def test_bf(p1, p2, expected):
    """
    Tests the bf function with various combinations of valid and invalid planet names,
    including non-string types and formatting issues, ensuring the returned tuple 
    contains planets between the two inputs sorted by proximity to the sun.
    """
    assert bf(p1, p2) == expected