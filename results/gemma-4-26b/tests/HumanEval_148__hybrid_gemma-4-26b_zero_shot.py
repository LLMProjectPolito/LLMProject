
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

# Import the function to be tested. 
# Adjust the import path as necessary for your project structure.
try:
    from solution import bf
except ImportError:
    try:
        from __main__ import bf
    except ImportError:
        # Fallback for environments where bf is defined in the global scope
        pass

@pytest.mark.parametrize("planet1, planet2, expected", [
    # --- Standard Cases (Forward Order) ---
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Mars", ("Earth",)),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),

    # --- Order Independence (Reverse Order should return same set, sorted by Sun proximity) ---
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Mars", "Earth", ("Venus",)),
    ("Mars", "Venus", ("Earth",)),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),

    # --- Edge Cases: Adjacent Planets (No planets exist between them) ---
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Saturn", ()),
    ("Uranus", "Neptune", ()),

    # --- Edge Cases: Same Planet ---
    ("Earth", "Earth", ()),
    ("Jupiter", "Jupiter", ()),
    ("Neptune", "Neptune", ()),

    # --- Error Handling: Invalid Planet Names & Typos ---
    ("Pluto", "Mars", ()),
    ("Mars", "JupiterX", ()),
    ("Sun", "Earth", ()),
    ("Earth", "Mars!", ()),
    ("Mars ", "Jupiter", ()),
    (" Venus", "Earth", ()),
    ("Pluto", "Earth", ()),
    ("Earth", "MarsX", ()),
    ("Sun", "Moon", ()),
    ("Jupiter", "Saturn ", ()),

    # --- Error Handling: Case Sensitivity ---
    ("jupiter", "Neptune", ()),
    ("EARTH", "Mars", ()),
    ("Mercury", "venus", ()),

    # --- Error Handling: Non-string inputs and Empty Strings ---
    ("", "Earth", ()),
    ("Mercury", "", ()),
    (None, "Mars", ()),
    (123, "Jupiter", ()),
    (True, "Venus", ()),
    (None, "Earth", ()),
    ("Earth", 123, ()),
    ([], "Mars", ()),
])
def test_bf_logic(planet1, planet2, expected):
    """
    Comprehensive test for planet range detection, order independence, 
    and robust handling of invalid/edge-case inputs.
    """
    assert bf(planet1, planet2) == expected

def test_bf_return_type():
    """
    Ensures the return type is always a tuple, even for single-element results.
    """
    result = bf("Earth", "Mercury")
    assert isinstance(result, tuple)
    assert result == ("Venus",)

def test_bf_sorting_order():
    """
    Explicitly verifies that the planets are returned in order of proximity to the Sun,
    regardless of the input order.
    """
    # Input in reverse order
    result = bf("Mars", "Mercury")
    assert result == ("Venus", "Earth")
    
    # Verify sorting via index mapping
    indices = {
        "Mercury": 0, "Venus": 1, "Earth": 2, "Mars": 3, 
        "Jupiter": 4, "Saturn": 5, "Uranus": 6, "Neptune": 7
    }
    planet_order = [indices[p] for p in result]
    assert planet_order == sorted(planet_order)