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
    return tuple(between_planets)

# STEP 2: PLAN - List test functions names and scenarios.
# Test Cases:
# 1. Valid planets, planet1 before planet2: bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
# 2. Valid planets, planet1 after planet2: bf("Earth", "Mercury") ==> ("Venus")
# 3. Valid planets, planet1 and planet2 far apart: bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
# 4. planet1 and planet2 are the same: bf("Earth", "Earth") ==> ()
# 5. Invalid planet1: bf("Pluto", "Earth") ==> ()
# 6. Invalid planet2: bf("Earth", "Pluto") ==> ()
# 7. Both planets invalid: bf("Pluto", "X") ==> ()
# 8. Adjacent planets: bf("Earth", "Mars") ==> ("Mars",)
# 9. First and last planets: bf("Mercury", "Neptune") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
# 10. Edge case: bf("Neptune", "Mercury") ==> ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize(
    "planet1, planet2, expected",
    [
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Earth", "Mercury", ("Venus",)),
        ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
        ("Earth", "Earth", ()),
        ("Pluto", "Earth", ()),
        ("Earth", "Pluto", ()),
        ("Pluto", "X", ()),
        ("Earth", "Mars", ("Mars",)),
        ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
        ("Neptune", "Mercury", ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
    ],
)
def test_bf(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected