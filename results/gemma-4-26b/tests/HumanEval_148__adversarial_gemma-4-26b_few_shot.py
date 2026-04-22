
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

# Assuming the function is in a file named solution.py
# from solution import bf

@pytest.mark.parametrize("p1, p2, expected", [
    # --- Happy Path (Standard cases from docstring) ---
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # --- Order Independence (The set of planets should be the same regardless of order) ---
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    
    # --- Boundary Cases: Adjacent Planets (Should return empty tuple) ---
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # --- Boundary Cases: Same Planet (Should return empty tuple) ---
    ("Earth", "Earth", ()),
    ("Neptune", "Neptune", ()),
    
    # --- Boundary Cases: Full Range ---
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
])
def test_bf_logic_and_boundaries(p1, p2, expected):
    """Tests standard logic, order independence, and adjacent/same planet boundaries."""
    assert bf(p1, p2) == expected


@pytest.mark.parametrize("p1, p2", [
    # --- Invalid Planet Names ---
    ("Pluto", "Earth"),          # Pluto is not in the list
    ("Mars", "Zorg"),            # Random string
    ("Sun", "Earth"),            # Sun is a star, not a planet in the list
    ("", "Venus"),               # Empty string
    (" Jupiter", "Neptune"),     # Leading whitespace
    ("Jupiter ", "Neptune"),     # Trailing whitespace
    
    # --- Case Sensitivity (Testing if the function is strict) ---
    ("jupiter", "Neptune"),      # Lowercase
    ("JUPITER", "Neptune"),      # Uppercase
    ("Earth", "mercury"),        # Mixed case
    
    # --- Non-String Types (Robustness check) ---
    (None, "Earth"),             # NoneType
    (123, "Mars"),               # Integer
    (["Venus"], "Earth"),        # List
    (True, "Jupiter"),           # Boolean
])
def test_bf_invalid_inputs(p1, p2):
    """Tests that invalid names, case mismatches, and wrong types return an empty tuple."""
    assert bf(p1, p2) == ()


def test_bf_return_type():
    """Ensures the function strictly returns a tuple, not a list or other iterable."""
    result = bf("Jupiter", "Neptune")
    assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"
    
    empty_result = bf("Pluto", "Earth")
    assert isinstance(empty_result, tuple), f"Expected tuple for invalid input, got {type(empty_result)}"