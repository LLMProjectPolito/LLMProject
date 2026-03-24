
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

    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()

    planet1 = planet1.capitalize()
    planet2 = planet2.capitalize()

    if planet1 not in planets or planet2 not in planets:
        return ()

    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    start_index = min(index1, index2) + 1
    end_index = max(index1, index2)

    between_planets = tuple(planets[start_index:end_index])
    return between_planets

@pytest.mark.parametrize("planet1, planet2, expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Neptune", "Mercury", ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
    ("Venus", "Earth", ("Earth",)),
    ("Earth", "Venus", ("Venus",)),
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Mercury", "Mercury", ()),
    ("mercury", "venus", ("venus",)),
    ("NEPTUNE", "mercury", ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
    ("Jupiter", "jupiter", ()),
    ("Earth", "Earth", ()),
    ("Invalid", "Mercury", ()),
    ("Mercury", "Invalid", ()),
    (123, "Mercury", ()),
    ("Mercury", 123, ()),
])
def test_bf(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected