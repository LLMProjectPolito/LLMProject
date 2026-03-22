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

def test_bf():
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Valid Cases
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ("Earth",)
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()

    # Invalid Cases
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Xandar", "Venus") == ()
    assert bf("Venus", "Xandar") == ()
    assert bf("", "Earth") == ()
    assert bf("Earth", "") == ()
    assert bf("", "") == ()

    # Case Sensitivity
    assert bf("earth", "Mercury") == ()
    assert bf("Mercury", "Earth") == ()
    assert bf("earth", "earth") == ()

    # Edge Cases - First and Last Planets
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Neptune", "Uranus") == ()
    assert bf("Uranus", "Neptune") == ()