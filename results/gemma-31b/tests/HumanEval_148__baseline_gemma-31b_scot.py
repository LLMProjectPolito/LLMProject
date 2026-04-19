
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

# The function bf is already defined in the environment.
# We are writing the test suite for it.

@pytest.mark.parametrize("p1, p2, expected", [
    # Provided Examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Order Independence (p1 further than p2)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Adjacent Planets (No planets in between)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Same Planet
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # Boundary: Full Range
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Invalid Planet Names
    ("Pluto", "Earth", ()),        # Pluto is no longer in the list
    ("Earth", "Xenon", ()),        # Completely fake name
    ("Mars", "mars", ()),          # Case sensitivity check
    ("Jupiter", "Jupitrr", ()),    # Typo
    ("A", "B", ()),                # Both invalid
    ("", "", ()),                  # Empty strings
])
def test_bf_logic(p1, p2, expected):
    """Test the bf function with various valid and invalid planet combinations."""
    result = bf(p1, p2)
    assert result == expected
    assert isinstance(result, tuple), f"Expected result to be a tuple, got {type(result)}"

def test_bf_return_type():
    """Ensure the function always returns a tuple regardless of input."""
    assert isinstance(bf("Earth", "Mars"), tuple)
    assert isinstance(bf("Invalid", "Invalid"), tuple)
    assert isinstance(bf("Mercury", "Neptune"), tuple)

def test_bf_immutability():
    """Ensure the function does not modify the input strings."""
    p1, p2 = "Earth", "Jupiter"
    bf(p1, p2)
    assert p1 == "Earth"
    assert p2 == "Jupiter"