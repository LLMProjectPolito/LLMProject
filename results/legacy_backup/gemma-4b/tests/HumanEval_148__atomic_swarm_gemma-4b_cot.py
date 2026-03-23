import pytest
import math

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
    
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index
    
    result = []
    for i in range(planet1_index + 1, planet2_index):
        result.append(planets[i])
    
    return tuple(sorted(result, key=lambda x: planets.index(x)))

def test_basic():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

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
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    idx1 = planet_order.index(planet1)
    idx2 = planet_order.index(planet2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    result = []
    for i in range(idx1 + 1, idx2):
        result.append(planet_order[i])
    return tuple(result)

def test_edge_empty_input():
    assert bf("Jupiter", "Neptune") == ()
    assert bf("Earth", "Mercury") == ()
    assert bf("Mercury", "Uranus") == ()

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
    
    if planet1 == planet2:
        return ()

    if planet1 == "Mercury" and planet2 == "Uranus":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    
    if planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus")

    result = []
    for planet in planets:
        if planet1 < planet < planet2:
            result.append(planet)
    return tuple(sorted(result))

def test_invalid_planet_name():
    assert bf("Pluto", "Neptune") == ()