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

def test_adjacent_planets():
    assert bf("Earth", "Mars") == ()

def test_valid_planets_between():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_planet1_first_planet2_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_invalid_planet_names():
    invalid_planets = ["Pluto", "Xantus", "Zorgon"]
    for planet in invalid_planets:
        assert bf(planet, "Neptune") == ()
        assert bf("Mercury", planet) == ()

def test_planet1_after_planet2():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")

def test_planet1_last_planet2_first():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()