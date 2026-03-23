import pytest
import math


# Focus: Valid/Invalid Planet Names
import pytest

def test_valid_planet_names_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_valid_planet_names_2():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_valid_planet_names_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_invalid_planet_name_1():
    assert bf("Pluto", "Neptune") == ()

def test_invalid_planet_name_2():
    assert bf("Earth", "Xyz") == ()

def test_invalid_planet_names_3():
    assert bf("Invalid", "AnotherInvalid") == ()

# Focus: Order of Planets (planet1 & planet2)
import pytest

def test_order_of_planets_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_order_of_planets_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_order_of_planets_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

# Focus: Edge Cases (same planet, planets at extremes)
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
    
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    start = min(index1, index2) + 1
    end = max(index1, index2)
    
    between_planets = tuple(planets[start:end])
    return between_planets

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_planets_at_extremes():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_planets_at_extremes_reversed():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")