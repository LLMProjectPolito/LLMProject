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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    planet1_orbit = "Mercury"
    planet2_orbit = "Neptune"
    
    if planet1 == planet1_orbit:
        return (planet2, planet2_orbit)
    elif planet2 == planet2_orbit:
        return (planet1, planet1_orbit)
    else:
        return ()

def test_bf_positive():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_empty():
    assert bf("", "") == ()

def test_bf_invalid_input():
    assert bf("Mercury", "Uranus") == ()

def test_bf_invalid_input_2():
    assert bf("Jupiter", "Venus") == ()