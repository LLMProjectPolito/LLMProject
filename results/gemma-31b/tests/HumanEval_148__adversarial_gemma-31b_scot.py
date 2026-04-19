
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
# We are testing it as a Blue Team QA Engineer.

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard cases (Forward)
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    
    # Standard cases (Backward - should still be sorted by proximity to sun)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Edge cases: Adjacent planets
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    
    # Edge cases: Same planet
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # Edge cases: Extreme ends
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Invalid planet names
    ("Pluto", "Earth", ()),      # Pluto is no longer a major planet
    ("Earth", "Xenon", ()),      # Completely fake name
    ("Mars", "mars", ()),        # Case sensitivity check
    ("Sun", "Moon", ()),         # Not planets
    ("", "", ()),                # Empty strings
    (None, "Earth", ()),         # None type (if handled by function)
])
def test_bf_logic(p1, p2, expected):
    """Test the core logic of the bf function across various valid and invalid inputs."""
    # We wrap the call in a try-except to handle potential TypeErrors if the function 
    # doesn't handle None/non-string inputs gracefully, treating it as a bug (failure).
    try:
        result = bf(p1, p2)
        assert result == expected, f"Failed for inputs {p1}, {p2}. Expected {expected}, got {result}"
    except Exception as e:
        pytest.fail(f"Function raised an unexpected exception {type(e).__name__} for inputs {p1}, {p2}")

def test_bf_return_type():
    """Ensure the function always returns a tuple, even when empty."""
    # Valid range
    assert isinstance(bf("Mercury", "Earth"), tuple)
    # Invalid range
    assert isinstance(bf("Invalid", "Invalid"), tuple)
    # Adjacent range
    assert isinstance(bf("Mercury", "Venus"), tuple)

def test_bf_immutability():
    """Ensure the result is a tuple (immutable) and not a list."""
    result = bf("Jupiter", "Neptune")
    assert type(result) is tuple
    with pytest.raises(TypeError):
        # This should fail because tuples do not support item assignment
        result[0] = "Mars"