
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
    # Standard cases from problem description
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    
    # Reverse order cases (proximity to sun should remain sorted)
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Mercury", "Earth", ("Venus",)),
    
    # Adjacent planets (nothing in between)
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Mars", ()),
    ("Mercury", "Venus", ()),
    ("Uranus", "Neptune", ()),
    
    # Same planet
    ("Earth", "Earth", ()),
    ("Neptune", "Neptune", ()),
    
    # Full range cases
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    
    # Mid-range cases
    ("Venus", "Jupiter", ("Earth", "Mars")),
    ("Saturn", "Earth", ("Mars", "Jupiter")),
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Saturn", ("Jupiter",)),
])
def test_bf_valid(p1, p2, expected):
    """Tests valid planet names and various ranges."""
    assert bf(p1, p2) == expected

@pytest.mark.parametrize("p1, p2", [
    # Non-existent planets and typos
    ("Pluto", "Earth"),
    ("Earth", "MarsX"),
    ("Sun", "Jupiter"),
    ("Mercurry", "Venus"),
    ("Uranusss", "Neptune"),
    
    # Case sensitivity
    ("jupiter", "Neptune"),
    ("JUPITER", "Neptune"),
    ("Jupiter", "neptune"),
    
    # Empty or invalid types
    ("", "Venus"),
    ("Jupiter", ""),
    (None, "Earth"),
    ("Earth", 123),
])
def test_bf_invalid(p1, p2):
    """Tests that invalid planet names or incorrect types return an empty tuple."""
    try:
        assert bf(p1, p2) == ()
    except TypeError:
        # If the function raises TypeError on non-string inputs, it fails the 
        # requirement to return an empty tuple for incorrect names.
        pytest.fail(f"bf({p1}, {p2}) raised TypeError instead of returning ()")

def test_bf_sequence_integrity():
    """Verifies the internal order of planets is strictly solar proximity for all valid pairs."""
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    for i in range(len(planets)):
        for j in range(len(planets)):
            if i == j:
                assert bf(planets[i], planets[j]) == ()
            else:
                start, end = min(i, j), max(i, j)
                expected = tuple(planets[start+1:end])
                assert bf(planets[i], planets[j]) == expected