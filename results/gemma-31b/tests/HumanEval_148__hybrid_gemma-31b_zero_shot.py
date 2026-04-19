
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
    '''
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    start = min(idx1, idx2)
    end = max(idx1, idx2)
    
    return planets[start + 1 : end]

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("p1, p2, expected", [
    # Standard cases (Forward order)
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Jupiter", ("Earth", "Mars")),
    
    # Standard cases (Reverse order - must still be sorted by sun proximity)
    ("Earth", "Mercury", ("Venus",)),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    
    # Edge cases: Adjacent planets (no planets in between)
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Uranus", "Neptune", ()),
    
    # Edge cases: Same planet
    ("Mars", "Mars", ()),
    ("Earth", "Earth", ()),
    
    # Boundary: Start and End of the solar system
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Invalid planet names (Dwarf planets, stars, moons, or gibberish)
    ("Pluto", "Earth", ()),
    ("Mars", "Sun", ()),
    ("Earth", "Xenon", ()),
    ("Moon", "Neptune", ()),
    ("Mars", "Unknown", ()),
    
    # Case sensitivity (should be strict)
    ("mercury", "Venus", ()),
    ("EARTH", "MARS", ()),
    ("jupiter", "SATURN", ()),
    
    # Incorrect types and empty inputs
    (None, "Earth", ()),
    (123, "Venus", ()),
    ("Mars", 45.6, ()),
    ("", "", ()),
    (1, 2, ()),
])
def test_bf_comprehensive_logic(p1, p2, expected):
    """Test core logic, edge cases, and invalid inputs in one comprehensive matrix."""
    result = bf(p1, p2)
    assert result == expected
    assert isinstance(result, tuple), f"Expected output to be a tuple, got {type(result)}"

def test_bf_order_preservation():
    """Explicitly verify that the output is always sorted by proximity to the sun."""
    planets_order = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    result = bf("Neptune", "Mercury")
    
    for i in range(len(result) - 1):
        assert planets_order.index(result[i]) < planets_order.index(result[i+1])

def test_bf_symmetry():
    """Ensure that bf(A, B) is identical to bf(B, A)."""
    p1, p2 = "Mercury", "Neptune"
    assert bf(p1, p2) == bf(p2, p1)

def test_bf_output_immutability():
    """Verify that the result is a tuple and cannot be mutated."""
    result = bf("Mercury", "Earth")
    assert type(result) is tuple
    with pytest.raises(TypeError):
        # Tuples do not support item assignment
        result[0] = "SomethingElse"

def test_bf_purity():
    """Ensure that the function does not mutate the input arguments."""
    p1, p2 = "Jupiter", "Neptune"
    bf(p1, p2)
    assert p1 == "Jupiter"
    assert p2 == "Neptune"