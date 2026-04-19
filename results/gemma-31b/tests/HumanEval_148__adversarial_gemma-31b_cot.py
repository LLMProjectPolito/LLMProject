
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
    
    # Boundary cases: Adjacent planets
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # Boundary cases: Same planet
    ("Mercury", "Mercury", ()),
    ("Neptune", "Neptune", ()),
    ("Earth", "Earth", ()),
    
    # Order independence (p1 further than p2)
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mars", "Venus", ()),
    
    # Full range
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Jupiter", "Mars-ish", ()),
    ("", "Earth", ()),
    
    # Case sensitivity (Assuming strict matching based on problem description)
    ("earth", "mercury", ()),
    ("EARTH", "MARS", ()),
    ("earth", "Venus", ()),
])
def test_bf_logic(p1, p2, expected):
    """Test the core logic and edge cases for planet orbit ranges."""
    result = bf(p1, p2)
    assert result == expected
    assert isinstance(result, tuple), f"Expected return type tuple, got {type(result)}"

@pytest.mark.parametrize("p1, p2", [
    (None, "Earth"),
    ("Earth", None),
    (123, "Mars"),
    ("Mars", 456),
    ([], "Jupiter"),
    ("Jupiter", {}),
])
def test_bf_type_safety(p1, p2):
    """Test how the function handles non-string inputs."""
    try:
        result = bf(p1, p2)
        assert result == ()
        assert isinstance(result, tuple)
    except Exception as e:
        pytest.fail(f"bf raised {type(e).__name__} unexpectedly with non-string inputs: {e}")

def test_bf_return_type_consistency():
    """Ensure that the function always returns a tuple, even when empty."""
    assert isinstance(bf("Invalid1", "Invalid2"), tuple)
    assert isinstance(bf("Mercury", "Venus"), tuple)
    assert isinstance(bf("Earth", "Mercury"), tuple)