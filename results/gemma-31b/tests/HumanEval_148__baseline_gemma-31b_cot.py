
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
    # Provided examples
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Edge Case: Adjacent planets (should return empty tuple)
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
    
    # Edge Case: Same planet (should return empty tuple)
    ("Earth", "Earth", ()),
    ("Mars", "Mars", ()),
    
    # Edge Case: Extreme ends of the solar system
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Edge Case: Invalid planet names
    ("Pluto", "Earth", ()),
    ("Earth", "Pluto", ()),
    ("Sun", "Moon", ()),
    ("Jupiter", "Mars-X", ()),
    ("", "Venus", ()),
    ("Venus", ""),
    
    # Edge Case: Case sensitivity (assuming the function expects exact matches as per examples)
    ("earth", "mercury", ()),
    ("EARTH", "MERCURY", ()),
    ("eArTh", "mErCuRy", ()),
    
    # Edge Case: Non-string inputs (if the function doesn't handle type checking, this might raise TypeError, 
    # but based on the prompt "takes two planet names as strings", we test string-like behavior)
    (None, "Earth", ()),
    ("Earth", None, ()),
])
def test_bf(p1, p2, expected):
    """
    Test the bf function with various combinations of planet names, 
    including valid, invalid, adjacent, and reversed orders.
    """
    # We wrap in a try-except because if the function doesn't handle None, 
    # it might crash. The prompt says it returns an empty tuple for incorrect names.
    try:
        result = bf(p1, p2)
        assert result == expected
        assert isinstance(result, tuple), f"Expected return type to be tuple, got {type(result)}"
    except TypeError:
        # If the function crashes on None/non-string, it fails the "return empty tuple" requirement
        pytest.fail(f"bf({p1}, {p2}) raised TypeError instead of returning an empty tuple")

def test_bf_sorting_order():
    """
    Explicitly verify that the output is always sorted by proximity to the sun,
    regardless of the order of input planets.
    """
    order = ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    # Forward order
    assert bf("Mercury", "Uranus") == order
    # Reverse order
    assert bf("Uranus", "Mercury") == order

def test_bf_no_endpoints_included():
    """
    Verify that the input planets themselves are not included in the resulting tuple.
    """
    res = bf("Earth", "Jupiter")
    assert "Earth" not in res
    assert "Jupiter" not in res
    assert res == ("Mars",)