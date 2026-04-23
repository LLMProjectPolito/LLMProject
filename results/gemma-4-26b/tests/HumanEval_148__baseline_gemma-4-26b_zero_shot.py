
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

    # --- Reverse Order (Order of arguments shouldn't affect the set of planets between) ---
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Earth", ("Venus",)),
    ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),

    # --- Adjacent Planets (No planets exist between them) ---
    ("Mercury", "Venus", ()),
    ("Venus", "Earth", ()),
    ("Earth", "Mars", ()),
    ("Mars", "Jupiter", ()),
    ("Jupiter", "Saturn", ()),
    ("Saturn", "Uranus", ()),
    ("Uranus", "Neptune", ()),

    # --- Same Planet ---
    ("Mercury", "Mercury", ()),
    ("Earth", "Earth", ()),
    ("Neptune", "Neptune", ()),

    # --- Invalid Planet Names ---
    ("Pluto", "Earth", ()),          # Not in the solar system list
    ("Earth", "MarsX", ()),          # Typo
    ("Sun", "Mercury", ()),          # Sun is not a planet
    ("", "Venus", ()),               # Empty string
    ("Jupiter", "Jupiterian", ()),   # Partial match/Invalid
    ("Mars", "123", ()),             # Numeric string
    ("Venus ", "Earth"),             # String with whitespace

    # --- Full Range ---
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
])
def test_bf(p1, p2, expected):
    """
    Tests the bf function with various scenarios including provided examples,
    reverse order, adjacent planets, same planets, invalid inputs, and full range.
    """
    assert bf(p1, p2) == expected