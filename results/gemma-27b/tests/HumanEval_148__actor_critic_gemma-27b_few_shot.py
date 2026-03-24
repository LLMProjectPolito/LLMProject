
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
    
    start = min(index1, index2) + 1
    end = max(index1, index2)
    
    between_planets = planets[start:end]
    
    return tuple(between_planets)

def test_bf_basic1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_basic2():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_basic3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_same_planet_returns_empty_tuple():
    assert bf("Earth", "Earth") == ()  # When both planets are the same, there are no planets between them.

def test_bf_invalid_planet():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Pluto", "Xyz") == ()

def test_bf_empty_input():
    assert bf("", "Earth") == ()
    assert bf("Earth", "") == ()

def test_bf_reverse_order():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")

def test_bf_first_and_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_last_and_first():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == ("Venus",)

def test_bf_far_apart():
    assert bf("Mercury", "Saturn") == ("Venus", "Earth", "Mars", "Jupiter")

def test_bf_case_insensitive():
    assert bf("earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Earth") == ("Venus",)

def test_bf_none_input():
    assert bf(None, "Earth") == ()
    assert bf("Earth", None) == ()
    assert bf(None, None) == ()