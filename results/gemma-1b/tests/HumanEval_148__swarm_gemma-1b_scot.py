
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
        "Mercury": 0.39,
        "Venus": 0.72,
        "Earth": 1.0,
        "Mars": 1.5,
        "Jupiter": 5.2,
        "Saturn": 9.4,
        "Uranus": 19.0,
        "Neptune": 30.0
    }
    orbits2 = {
        "Mercury": 0.39,
        "Venus": 0.72,
        "Earth": 1.0,
        "Mars": 1.5,
        "Jupiter": 5.2,
        "Saturn": 9.4,
        "Uranus": 19.0,
        "Neptune": 30.0
    }
    
    planet_pairs = []
    for p1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        for p2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
            if p1 != p2:
                orbits1[p1] = orbits1.get(p1, 0) + 1
                orbits2[p2] = orbits2.get(p2, 0) + 1
                if orbits1[p1] < orbits2[p2]:
                    planet_pairs.append((p1, p2))
    
    if not planet_pairs:
        return ()
    
    planet_pairs.sort(key=lambda x: orbits1[x[0]])
    return tuple(planet_pairs)

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