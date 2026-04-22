
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    start = min(idx1, idx2) + 1
    end = max(idx1, idx2)
    
    # If planets are adjacent or the same, start will be >= end
    if start >= end:
        return ()
        
    return tuple(planets[start:end])


# --- Pytest Suite ---

def test_provided_examples():
    """Tests the examples provided in the problem description."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_reversed_order():
    """Tests that the function works regardless of which planet is passed first."""
    # Neptune to Jupiter (reverse of example 1)
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    # Mercury to Earth (reverse of example 2)
    assert bf("Mercury", "Earth") == ("Venus",)

def test_adjacent_planets():
    """Tests that planets next to each other return an empty tuple."""
    assert bf("Mars", "Jupiter") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Uranus", "Neptune") == ()

def test_same_planet():
    """Tests that passing the same planet twice returns an empty tuple."""
    assert bf("Earth", "Earth") == ()
    assert bf("Saturn", "Saturn") == ()

def test_invalid_planet_names():
    """Tests that incorrect planet names return an empty tuple."""
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "MarsX") == ()
    assert bf("Sun", "Moon") == ()
    assert bf("", "Mercury") == ()
    assert bf("Jupiter", "jupiter") == ()  # Case sensitivity check

def test_non_string_inputs():
    """Tests how the function handles non-string inputs."""
    assert bf(None, "Earth") == ()
    assert bf(123, "Mars") == ()
    assert bf("Venus", ["Earth"]) == ()

def test_full_range():
    """Tests the maximum possible range (Mercury to Neptune)."""
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Mercury", "Neptune") == expected