
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
    # Standard forward ranges
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Jupiter", ("Earth", "Mars")),
    ("Mercury", "Earth", ("Venus",)),
    # Standard reverse ranges (should return same result as forward)
    ("Earth", "Mercury", ("Venus",)),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mars", "Venus", ("Earth",)),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    # Single intermediary cases
    ("Earth", "Jupiter", ("Mars",)),
    ("Jupiter", "Uranus", ("Saturn",)),
    ("Saturn", "Neptune", ("Uranus",)),
])
def test_bf_valid_ranges(p1, p2, expected):
    """Test that valid planet ranges return the correct intermediate planets sorted by sun proximity."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    ("Mercury", "Venus"),   # Adjacent
    ("Venus", "Earth"),     # Adjacent
    ("Earth", "Mars"),      # Adjacent
    ("Mars", "Jupiter"),    # Adjacent
    ("Jupiter", "Saturn"),  # Adjacent
    ("Saturn", "Uranus"),   # Adjacent
    ("Uranus", "Neptune"),  # Adjacent
    ("Venus", "Mercury"),   # Adjacent reverse
    ("Mars", "Mars"),       # Same planet
    ("Neptune", "Neptune"), # Same planet
])
def test_bf_edge_cases(p1, p2):
    """Test that adjacent or identical planets return an empty tuple."""
    assert bf(p1, p2) == ()

@pytest.mark.parametrize("p1, p2", [
    ("Pluto", "Earth"),       # Dwarf planet
    ("Earth", "Mars-ish"),    # Typo
    ("Mars", "Sun"),          # Not a planet
    ("earth", "Mars"),        # Case sensitivity (lowercase)
    ("Jupiter", "VENUS"),     # Case sensitivity (uppercase)
    ("mErCuRy", "Venus"),     # Case sensitivity (mixed)
    (None, "Earth"),          # Wrong type (None)
    (123, 456),               # Wrong type (int)
    ("", ""),                 # Empty strings
    ("Mars", "Xenon"),        # Random string
])
def test_bf_invalid_inputs(p1, p2):
    """Test that invalid planet names, case mismatches, or wrong types return an empty tuple."""
    # We use a try-except block to ensure that TypeErrors are treated as failures 
    # if the function is expected to handle them and return ().
    try:
        assert bf(p1, p2) == ()
    except TypeError as e:
        pytest.fail(f"bf({p1}, {p2}) raised TypeError unexpectedly: {e}")

def test_bf_full_span():
    """Test the maximum possible range from the innermost to the outermost planet."""
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected
    assert bf("Neptune", "Mercury") == expected

def test_bf_return_type():
    """Ensure the return type is always a tuple, regardless of input validity."""
    assert isinstance(bf("Mercury", "Mars"), tuple), "Should return tuple for valid input"
    assert isinstance(bf("Invalid", "Invalid"), tuple), "Should return tuple for invalid input"
    assert isinstance(bf(None, None), tuple), "Should return tuple for None input"