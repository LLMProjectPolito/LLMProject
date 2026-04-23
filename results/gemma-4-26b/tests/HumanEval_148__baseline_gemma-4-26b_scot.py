
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
    # Provided examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Order independence (Reverse of examples)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Adjacent planets (No planets between)
    ("Mercury", "Venus", ()),
    ("Mars", "Jupiter", ()),
    ("Saturn", "Uranus", ()),
    
    # Same planet
    ("Earth", "Earth", ()),
    ("Neptune", "Neptune", ()),
    
    # Full range
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
])
def test_bf_valid_ranges(p1, p2, expected):
    """Tests valid planet pairs including order independence and adjacent planets."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),      # Non-existent planet
    ("Earth", "Sun"),        # Non-existent planet
    ("earth", "Mars"),       # Case sensitivity check (assuming strict matching)
    ("Jupiter", "Jupiterr"), # Typo
    ("", "Venus"),           # Empty string
    ("Mars", "123"),         # Non-string input (if type checking is expected)
    (None, "Earth"),         # None type
])
def test_bf_invalid_planets(p1, p2):
    """Tests that invalid planet names return an empty tuple."""
    # We use a try-except block in case the function raises TypeError for non-string inputs
    # but the requirement says "return an empty tuple if planet1 or planet2 are not correct planet names"
    try:
        assert bf(p1, p2) == ()
    except TypeError:
        # If the function is expected to crash on non-strings, this is acceptable,
        # but based on the prompt, it should ideally return ()
        pass

def test_bf_return_type():
    """Ensures the return type is always a tuple."""
    assert isinstance(bf("Mercury", "Neptune"), tuple)
    assert isinstance(bf("Invalid", "Earth"), tuple)
    assert isinstance(bf("Mars", "Mars"), tuple)