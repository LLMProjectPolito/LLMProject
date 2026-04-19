
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
    # Examples provided in the docstring
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Order independence (p1 further than p2)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Boundary cases: Adjacent planets
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Boundary cases: Same planet
    ("Earth", "Earth", ()),
    ("Mercury", "Mercury", ()),
    ("Neptune", "Neptune", ()),
    
    # Boundary cases: Extremes
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Mars", "Xenon", ()),
    ("Sun", "Moon", ()),
    ("", "Mercury", ()),
    ("Jupiter", "", ()),
    ("JUPITER", "NEPTUNE", ()), # Assuming case sensitivity based on prompt
])
def test_bf_logic(p1, p2, expected):
    assert bf(p1, p2) == expected

def test_bf_return_type():
    """Ensure the function always returns a tuple."""
    assert isinstance(bf("Jupiter", "Neptune"), tuple)
    assert isinstance(bf("Invalid", "Invalid"), tuple)
    assert isinstance(bf("Mercury", "Venus"), tuple)

def test_bf_non_string_input():
    """Ensure the function handles non-string inputs gracefully if they aren't valid planet names."""
    # Depending on implementation, this might raise TypeError or return (). 
    # Given the prompt "return empty tuple if not correct planet names", we expect ().
    try:
        assert bf(None, "Earth") == ()
        assert bf(123, 456) == ()
    except TypeError:
        pytest.fail("bf() raised TypeError unexpectedly with non-string input")