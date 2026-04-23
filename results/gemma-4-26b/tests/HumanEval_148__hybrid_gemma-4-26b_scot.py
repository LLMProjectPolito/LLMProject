
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
# We import it from __main__ to allow testing in interactive/execution contexts.

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard ranges
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Order independence (Descending input)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    
    # Boundary/Edge cases
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")), # Max range
    ("Mars", "Jupiter", ()),  # Adjacent
    ("Saturn", "Uranus", ()), # Adjacent
    ("Earth", "Earth", ()),   # Same planet
])
def test_bf_valid_ranges(p1, p2, expected):
    """Tests core logic for valid planet names and various orbital ranges."""
    from __main__ import bf
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    # Invalid planet names
    ("Pluto", "Earth"),       # Not a solar system planet
    ("Earth", "MarsX"),       # Typo
    ("Jupiter", "Sun"),       # Sun is not a planet
    ("", "Venus"),            # Empty string
    
    # Case sensitivity
    ("earth", "Mercury"),
    ("JUPITER", "Neptune"),
    
    # Whitespace handling
    ("  Mars  ", "Jupiter"),
    ("Venus", "  Earth  "),
])
def test_bf_invalid_inputs(p1, p2):
    """Tests that invalid names, case mismatches, and whitespace return an empty tuple."""
    from __main__ import bf
    assert bf(p1, p2) == ()

@pytest.mark.parametrize("p1, p2", [
    (None, "Earth"),
    (123, "Jupiter"),
    ("Mars", None),
    ([], "Venus"),
])
def test_bf_non_string_inputs(p1, p2):
    """Tests defensive handling of non-string inputs."""
    from __main__ import bf
    # Based on requirements, invalid inputs should return an empty tuple.
    # We use a try-except to ensure the test passes if the function raises a TypeError 
    # instead of returning (), as both are acceptable ways to handle bad types.
    try:
        assert bf(p1, p2) == ()
    except TypeError:
        pass

def test_bf_integrity():
    """
    Ensures the return type is always a tuple and the elements 
    are strictly sorted by solar proximity.
    """
    from __main__ import bf
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Test case: Wide range with reverse input
    result = bf("Neptune", "Mercury")
    
    # 1. Check Type
    assert isinstance(result, tuple), "Result must be a tuple"
    
    # 2. Check Content
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert result == expected
    
    # 3. Check strict solar order via indices
    indices = [planets_order.index(p) for p in result]
    assert indices == sorted(indices), "Planets in result are not in solar proximity order"