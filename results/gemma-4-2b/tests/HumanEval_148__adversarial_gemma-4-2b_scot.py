
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

    start_index = planets.index(planet1)
    end_index = planets.index(planet2)

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    between_planets = planets[start_index + 1:end_index]
    between_planets.sort()
    return tuple(between_planets)

def test_valid_input_planets_in_between():
    assert bf("Earth", "Mars") == ("Venus")
    assert bf("Venus", "Earth") == ("Mars")
    assert bf("Mars", "Jupiter") == ("Earth", "Venus")
    assert bf("Jupiter", "Saturn") == ("Mars", "Earth", "Venus")
    assert bf("Saturn", "Uranus") == ("Jupiter", "Mars", "Earth", "Venus")
    assert bf("Uranus", "Neptune") == ("Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_valid_input_planets_with_a_gap():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth", "Mercury")
    assert bf("Earth", "Jupiter") == ("Mars", "Venus", "Mercury")
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus", "Mars", "Earth", "Venus")

def test_valid_input_planets_with_multiple_planets_in_between():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Venus", "Neptune") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Earth", "Neptune") == ("Mars", "Jupiter", "Saturn", "Uranus", "Venus")

def test_invalid_input_incorrect_planet_names():
    assert bf("Mercury", "Pluto") == ()
    assert bf("Pluto", "Mercury") == ()
    assert bf("Pluto", "Pluto") == ()

def test_edge_case_same_planet_names():
    assert bf("Mercury", "Mercury") == ()

def test_order_of_planets_in_input():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert bf("Saturn", "Neptune") == ("Jupiter", "Mars", "Earth", "Venus")