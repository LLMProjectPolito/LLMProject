
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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    planet1_orbit = float('inf')
    planet2_orbit = float('inf')
    
    if planet1 == "Mercury":
        planet1_orbit = 0.397
    elif planet1 == "Venus":
        planet1_orbit = 0.723
    elif planet1 == "Earth":
        planet1_orbit = 1.0
    elif planet1 == "Mars":
        planet1_orbit = 1.524
    elif planet1 == "Jupiter":
        planet1_orbit = 5.201
    elif planet1 == "Saturn":
        planet1_orbit = 9.446
    elif planet1 == "Uranus":
        planet1_orbit = 19.222
    elif planet1 == "Neptune":
        planet1_orbit = 30.35
    
    if planet2 == "Mercury":
        planet2_orbit = 0.397
    elif planet2 == "Venus":
        planet2_orbit = 0.723
    elif planet2 == "Earth":
        planet2_orbit = 1.0
    elif planet2 == "Mars":
        planet2_orbit = 1.524
    elif planet2 == "Jupiter":
        planet2_orbit = 5.201
    elif planet2 == "Saturn":
        planet2_orbit = 9.446
    elif planet2 == "Uranus":
        planet2_orbit = 19.222
    elif planet2 == "Neptune":
        planet2_orbit = 30.35
    
    if planet1_orbit < planet2_orbit:
        return (planet1, planet2)
    else:
        return (planet1, planet2)