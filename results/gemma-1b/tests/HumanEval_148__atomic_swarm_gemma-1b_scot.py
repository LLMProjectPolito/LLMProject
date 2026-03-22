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
    
    orbits1 = {
        "Mercury": 0.397,
        "Venus": 0.723,
        "Earth": 1.000,
        "Mars": 1.524,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.186,
        "Neptune": 30.06
    }
    orbits2 = {
        "Mercury": 0.397,
        "Venus": 0.723,
        "Earth": 1.000,
        "Mars": 1.524,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.186,
        "Neptune": 30.06
    }
    
    planet1_orbit = orbits1[planet1]
    planet2_orbit = orbits2[planet2]
    
    if planet1_orbit < planet2_orbit:
        return (planet1, planet2)
    else:
        return (planet2, planet1)

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
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    planet_orbits = {
        "Mercury": 0.387,
        "Venus": 0.723,
        "Earth": 1.000,
        "Mars": 1.524,
        "Jupiter": 5.206,
        "Saturn": 9.423,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    
    if planet1 in planet_orbits and planet2 in planet_orbits:
        planet_pair = (planet_orbits[planet1], planet_orbits[planet2])
        
        sorted_pairs = sorted(planet_pair, key=lambda x: x[0])
        return sorted_pairs
    else:
        return ()

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
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    planet1_orbit = 0
    planet2_orbit = 0
    
    if planet1 == "Mercury":
        planet1_orbit = 0
    elif planet1 == "Venus":
        planet1_orbit = 1
    elif planet1 == "Earth":
        planet1_orbit = 2
    elif planet1 == "Mars":
        planet1_orbit = 3
    elif planet1 == "Jupiter":
        planet1_orbit = 4
    elif planet1 == "Saturn":
        planet1_orbit = 5
    elif planet1 == "Uranus":
        planet1_orbit = 6
    elif planet1 == "Neptune":
        planet1_orbit = 7
    
    if planet2 == "Mercury":
        planet2_orbit = 0
    elif planet2 == "Venus":
        planet2_orbit = 1
    elif planet2 == "Earth":
        planet2_orbit = 2
    elif planet2 == "Mars":
        planet2_orbit = 3
    elif planet2 == "Jupiter":
        planet2_orbit = 4
    elif planet2 == "Saturn":
        planet2_orbit = 5
    elif planet2 == "Uranus":
        planet2_orbit = 6
    elif planet2 == "Neptune":
        planet2_orbit = 7
    
    if planet1_orbit < planet2_orbit:
        return (planet1, planet2)
    elif planet1_orbit > planet2_orbit:
        return (planet2, planet1)
    else:
        return (planet1, planet2)