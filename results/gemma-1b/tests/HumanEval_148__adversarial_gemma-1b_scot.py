
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
    if not (planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return ()
    
    planet1_orbit = 0.0
    planet2_orbit = 0.0
    
    if planet1 == "Mercury":
        planet1_orbit = 0.0
    elif planet1 == "Venus":
        planet1_orbit = 0.0
    elif planet1 == "Earth":
        planet1_orbit = 0.0
    elif planet1 == "Mars":
        planet1_orbit = 0.0
    elif planet1 == "Jupiter":
        planet1_orbit = 0.0
    elif planet1 == "Saturn":
        planet1_orbit = 0.0
    elif planet1 == "Uranus":
        planet1_orbit = 0.0
    elif planet1 == "Neptune":
        planet1_orbit = 0.0
    
    if planet2 == "Mercury":
        planet2_orbit = 0.0
    elif planet2 == "Venus":
        planet2_orbit = 0.0
    elif planet2 == "Earth":
        planet2_orbit = 0.0
    elif planet2 == "Mars":
        planet2_orbit = 0.0
    elif planet2 == "Jupiter":
        planet2_orbit = 0.0
    elif planet2 == "Saturn":
        planet2_orbit = 0.0
    elif planet2 == "Uranus":
        planet2_orbit = 0.0
    elif planet2 == "Neptune":
        planet2_orbit = 0.0
    
    if planet1_orbit > planet2_orbit:
        return (planet1, planet2)
    elif planet1_orbit < planet2_orbit:
        return (planet2, planet1)
    else:
        return (planet1, planet2)

# Run the tests
def test_bf():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Earth") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mars", "Jupiter") == ("Mars", "Jupiter")
    assert bf("Saturn", "Uranus") == ("Saturn", "Uranus")
    assert bf("Uranus", "Neptune") == ("Uranus", "Neptune")
    assert bf("Venus", "Mars") == ("Venus", "Mars")
    assert bf("Mercury", "Venus") == ("Mercury", "Venus")
    assert bf("Venus", "Mercury") == ("Venus", "Mercury")
    assert bf("Mercury", "Mars") == ("Mercury", "Mars")
    assert bf("Mars", "Mercury") == ("Mars", "Mercury")
    assert bf("Jupiter", "Saturn") == ("Jupiter", "Saturn")
    assert bf("Saturn", "Jupiter") == ("Saturn", "Jupiter")
    assert bf("Uranus", "Neptune") == ("Uranus", "Neptune")
    assert bf("Neptune", "Uranus") == ("Neptune", "Uranus")
    print("All tests passed!")

test_bf()