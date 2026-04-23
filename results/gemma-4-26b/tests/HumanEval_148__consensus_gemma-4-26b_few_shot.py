
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
    # --- Provided Examples ---
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # --- Symmetry (Order independence) ---
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Saturn", "Mars", ("Jupiter",)),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # --- Boundary Cases: Adjacent Planets (No planets between) ---
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),
    
    # --- Boundary Cases: Same Planet ---
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # --- Invalid Planet Names (Strings) ---
    ("Pluto", "Earth", ()),
    ("Earth", "MarsX", ()),
    ("Sun", "Mercury", ()),
    ("", "Venus", ()),
    ("Jupiter", " ", ()),
    ("jupiter", "Neptune", ()),
    ("JUPITER", "Neptune", ()),
    ("Earth", "mercury", ()),
    ("Earth", " Venus", ()),
    ("Earth", "Venus ", ()),
    
    # --- Invalid Types (Robustness check) ---
    (None, "Earth", ()),
    (123, "Venus", ()),
    ([], "Mars", ()),
    (True, "Mars", ()),
])
def test_bf(p1, p2, expected):
    """
    Tests the bf function for correct orbit calculation, symmetry, 
    handling of adjacent planets, same planets, and robustness against invalid inputs.
    """
    assert bf(p1, p2) == expected

def test_bf_return_type():
    """
    Ensures the function always returns a tuple, even for empty or invalid results.
    """
    assert isinstance(bf("Mercury", "Venus"), tuple)
    assert isinstance(bf("Invalid", "Planet"), tuple)
    assert isinstance(bf(None, 123), tuple)