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
                if abs(orbits1[p1] - orbits2[p2]) <= 1:
                    planet_pairs.append((p1, p2))
    
    if not planet_pairs:
        return ()
    
    return tuple(sorted(planet_pairs))

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
    for planet in ["Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Neptune"]:
        if abs(planet_orbit - planet_orbit) <= planet_orbit:
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
        "Earth": 1.0,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    orbits2 = {
        "Mercury": 0.388,
        "Venus": 0.721,
        "Earth": 1.0,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    
    planet1_orbit = orbits1[planet1]
    planet2_orbit = orbits2[planet2]
    
    result = []
    for planet in ["Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Neptune"]:
        if abs(planet_orbit - planet_orbit) <= planet_orbit:
            result.append(planet)
    
    return tuple(sorted(result))

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
        "Earth": 1.0,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    orbits2 = {
        "Mercury": 0.388,
        "Venus": 0.721,
        "Earth": 1.0,
        "Mars": 1.521,
        "Jupiter": 5.206,
        "Saturn": 9.534,
        "Uranus": 19.196,
        "Neptune": 30.066
    }
    
    planet1_orbit = orbits1[planet1]
    planet2_orbit = orbits2[planet2]
    
    result = []
    for planet in ["Saturn", "Uranus", "Venus", "Earth", "Mars", "Jupiter", "Neptune"]:
        if abs(planet_orbit - planet_orbit) <= planet_orbit:
            result.append(planet)
    
    return tuple(sorted(result))