
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
import math

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
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    orbits1 = {
        "Mercury": 0.388,
        "Venus": 0.721,
        "Earth": 1.000,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.546,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    orbits2 = {
        "Mercury": 0.388,
        "Venus": 0.721,
        "Earth": 1.000,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    
    planet1_orbit = orbits1[planet1]
    planet2_orbit = orbits2[planet2]
    
    result = []
    for planet in ["Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]:
        if abs(planet1_orbit - planet2_orbit) <= 1.0:
            result.append(planet)
    
    return tuple(result)

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
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    orbits1 = {
        "Mercury": 0.388,
        "Venus": 0.721,
        "Earth": 1.000,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    orbits2 = {
        "Mercury": 0.388,
        "Venus": 0.721,
        "Earth": 1.000,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    
    planet1_orbit = orbits1[planet1]
    planet2_orbit = orbits2[planet2]
    
    result = []
    for planet in ["Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]:
        if abs(planet1_orbit - planet2_orbit) <= 1.0:
            result.append(planet)
    
    return tuple(result)