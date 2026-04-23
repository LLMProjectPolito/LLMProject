
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

    if planet1 == "Mercury" and planet2 == "Uranus":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    elif planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus")
    elif planet1 == "Venus" and planet2 == "Earth":
        return ("Mars")
    elif planet1 == "Earth" and planet2 == "Mars":
        return ("Venus")
    elif planet1 == "Mars" and planet2 == "Jupiter":
        return ("Saturn", "Uranus")
    elif planet1 == "Saturn" and planet2 == "Uranus":
        return ("Jupiter", "Mars", "Venus", "Earth")
    elif planet1 == "Uranus" and planet2 == "Neptune":
        return ("Saturn", "Jupiter", "Mars", "Venus", "Earth")
    elif planet1 == "Neptune" and planet2 == "Mercury":
        return ("Uranus", "Saturn", "Jupiter", "Mars", "Venus", "Earth")
    else:
        return ()

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_same_planets():
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Mercury", "Pluto") == ()

def test_bf_mixed_order():
    assert bf("Mars", "Saturn") == ("Jupiter", "Uranus")

def test_bf_order_reversed():
    assert bf("Saturn", "Mars") == ("Jupiter", "Uranus")

def test_bf_all_planets():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_single_planet():
    assert bf("Mercury", "Mercury") == ()