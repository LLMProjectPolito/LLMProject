
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
    are not correct planet names. If planet1 and planet2 are adjacent, an empty tuple is returned.
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    start = min(index1, index2) + 1  # Exclude planet at the smaller index
    end = max(index1, index2)
    
    if abs(index1 - index2) == 1:
        return ()
    
    between_planets = tuple(planets[start:end])
    
    return between_planets

# Pytest Suite
def test_bf_basic_1():
    # Test case for planets in ascending order
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_basic_2():
    # Test case for planets in descending order with a single planet in between
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_basic_3():
    # Test case for planets with multiple planets in between
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_same_planet():
    # Test case where both planets are the same
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planets():
    # Test case with invalid planet names
    assert bf("Pluto", "X") == ()

def test_bf_reverse_order():
    # Test that the function works correctly when planets are provided in reverse order.
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")

def test_bf_adjacent_planets():
    # Test case for adjacent planets
    assert bf("Earth", "Mars") == ()

def test_bf_first_and_last():
    # Test case where planet1 is the first and planet2 is the last
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_last_and_first():
    # Test case where planet1 is the last and planet2 is the first
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_first_and_second():
    # Test case where planet1 is the first and planet2 is the second
    assert bf("Mercury", "Venus") == ()

def test_bf_last_and_second_to_last():
    # Test case where planet1 is the last and planet2 is the second to last
    assert bf("Neptune", "Uranus") == ("Saturn")

def test_bf_first_planet_any_other():
    # Test case where planet1 is the first planet and planet2 is any other planet
    assert bf("Mercury", "Mars") == ("Venus", "Earth")

def test_bf_last_planet_any_other():
    # Test case where planet2 is the last planet and planet1 is any other planet
    assert bf("Earth", "Neptune") == ("Mars", "Jupiter", "Saturn", "Uranus")