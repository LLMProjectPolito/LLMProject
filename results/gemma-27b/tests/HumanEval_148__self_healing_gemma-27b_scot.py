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

def test_valid_planets_in_order():
    assert bf("Venus", "Earth") == ("Earth",)

def test_valid_planets_reverse_order():
    assert bf("Mars", "Venus") == ("Earth",)

def test_invalid_planet1():
    assert bf("Pluto", "Earth") == ()

def test_invalid_planet2():
    assert bf("Earth", "Pluto") == ()

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_adjacent_planets():
    assert bf("Earth", "Mars") == ("Mars",)

def test_example_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_example_2():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_example_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_edge_case_first_and_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")