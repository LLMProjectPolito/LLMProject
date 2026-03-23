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

    result = []
    for planet in planets:
        if planet != planet1 and planet != planet2:
            if planet1 != planet2:
                if planet1 < planet < planet2:
                    result.append(planet)
            else:
                result.append(planet)
    return tuple(sorted(result))


def test_valid_planet_names_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_valid_planet_names_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_valid_planet_names_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_valid_planet_names_venus_earth():
    assert bf("Venus", "Earth") == ("Mars")

def test_invalid_planet_name():
    assert bf("Pluto", "Neptune") == ()

def test_same_planet_names():
    assert bf("Earth", "Earth") == ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_planet1_before_planet2():
    assert bf("Mercury", "Venus") == ("Earth", "Mars")

def test_planet1_after_planet2():
    assert bf("Venus", "Mercury") == ("Earth", "Mars")

def test_planet1_equals_planet2():
    assert bf("Earth", "Earth") == ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")