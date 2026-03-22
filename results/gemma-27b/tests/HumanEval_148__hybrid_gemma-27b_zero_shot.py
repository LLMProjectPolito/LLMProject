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

@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Earth", "Mercury", ("Venus",)),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Venus", "Mars", ("Earth",)),
        ("Mars", "Venus", ("Earth",)),
        ("Neptune", "Mercury", tuple()),
        ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
        ("Earth", "Earth", tuple()),
        ("Jupiter", "Jupiter", tuple()),
        ("Pluto", "Earth", tuple()),
        ("Earth", "Pluto", tuple()),
        ("Venus", "Venus", tuple()),
        ("Saturn", "Mars", ("Jupiter",)),
        ("Mars", "Saturn", ("Jupiter",)),
        ("Uranus", "Earth", ("Saturn", "Jupiter", "Mars", "Venus")),
        ("Earth", "Uranus", ("Mars", "Jupiter", "Saturn")),
        ("Mercury", "Venus", tuple()),
        ("Venus", "Mercury", tuple()),
        ("Neptune", "Neptune", tuple()),
        ("Mercury", "Mercury", tuple()),
        ("Saturn", "Saturn", tuple()),
        ("Pluto", "Earth", tuple()),
        ("Earth", "Pluto", tuple()),
        ("Uranus", "Jupiter", ("Saturn",)),
        ("Jupiter", "Uranus", ("Saturn",)),
        ("Mars", "Jupiter", ("Earth", "Venus")),
        ("Jupiter", "Mars", ("Earth", "Venus")),
        ("Mars", "Mars", tuple()),
        ("Jupiter", "Jupiter", tuple()),
        ("Saturn", "Saturn", tuple()),
        ("Uranus", "Uranus", tuple()),
    ]
)
def test_bf(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected