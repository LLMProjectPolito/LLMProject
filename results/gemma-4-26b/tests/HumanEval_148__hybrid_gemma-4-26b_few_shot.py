
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

# Assuming the function is imported from your module
# from your_module import bf

def test_bf_docstring_examples():
    """
    Ensures the function strictly adheres to the examples 
    provided in the official documentation.
    """
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard ranges
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Jupiter", "Saturn", ("Uranus",)), # Note: Depending on implementation, 
                                        # if "between" means exclusive, this might be ()
                                        # Adjust expected based on specific function logic.
    # Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Uranus", "Neptune", ()),
    # Same planet (should return empty tuple)
    ("Mars", "Mars", ()),
    ("Jupiter", "Jupiter", ()),
])
def test_bf_valid_ranges(p1, p2, expected):
    """Tests various valid planet combinations, including adjacency and boundaries."""
    assert bf(p1, p2) == expected

def test_bf_order_independence():
    """Tests that the result is identical regardless of argument order (Symmetry)."""
    planets_to_test = [
        ("Earth", "Jupiter"),
        ("Mercury", "Neptune"),
        ("Venus", "Mars")
    ]
    for p1, p2 in planets_to_test:
        assert bf(p1, p2) == bf(p2, p1)

@pytest.mark.parametrize("p1, p2", [
    # Non-existent planets/Typos
    ("Pluto", "Earth"),
    ("Earth", "Sun"),
    ("Mars", "Mar"),
    # Formatting issues
    ("Earth ", "Mars"),      # Trailing space
    ("earth", "Mars"),       # Case sensitivity
    ("JUPITER", "Neptune"),  # Case sensitivity
    # Empty/Invalid types
    ("", "Venus"),
    ("123", "Venus"),
    (None, "Earth"),
    (123, "Mars"),
])
def test_bf_invalid_inputs(p1, p2):
    """
    Tests that invalid names, incorrect casing, whitespace, 
    and non-string types all return an empty tuple.
    """
    # We wrap in a try-except if the function is expected to be robust 
    # against TypeErrors, otherwise, we simply assert the return value.
    try:
        assert bf(p1, p2) == ()
    except TypeError:
        # If the function is NOT designed to handle None/int, 
        # this catch allows the test to pass if the requirement 
        # is simply "don't crash" or if we are testing strictness.
        pytest.fail(f"Function raised TypeError on input: {p1}, {p2}")