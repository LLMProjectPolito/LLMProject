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
    
    start_index = planets.index(planet1)
    end_index = planets.index(planet2)
    
    if start_index >= end_index:
        return ()
    
    between_planets = planets[start_index + 1:end_index]
    return tuple(between_planets)

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth")
    assert bf("Mars", "Venus") == ()
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert bf("Saturn", "Earth") == ()
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Uranus", "Mercury") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "X") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_bf_case_sensitivity():
    assert bf("jupiter", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("jupiter", "neptune") == ()

def test_bf_empty_string():
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_edge_cases():
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Neptune", "Uranus") == ()