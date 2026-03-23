import pytest
import math


# Focus: Boundary Values
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
    
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index
    
    result = []
    for i in range(planet1_index + 1, planet2_index):
        result.append(planets[i])
    
    return tuple(sorted(result, key=lambda x: planets.index(x)))

@pytest.mark.boundary
def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

@pytest.mark.boundary
def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

@pytest.mark.boundary
def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

# Focus: Type Scenarios
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
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    
    index1 = planet_order.index(planet1)
    index2 = planet_order.index(planet2)
    
    if index1 > index2:
        index1, index2 = index2, index1
    
    result = []
    for planet in planet_order:
        if index1 < planet_order.index(planet) < index2:
            result.append(planet)
    
    return tuple(result)

@pytest.mark.usefixtures("type_scenarios")
def test_bf_valid_input_1():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

@pytest.mark.usefixtures("type_scenarios")
def test_bf_valid_input_2():
    assert bf("Earth", "Mercury") == ("Venus")

@pytest.mark.usefixtures("type_scenarios")
def test_bf_valid_input_3():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

# Focus: Logic Branches
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
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    index1 = planet_order.index(planet1)
    index2 = planet_order.index(planet2)
    if index1 > index2:
        index1, index2 = index2, index1
    result = []
    for i in range(index1 + 1, index2):
        result.append(planet_order[i])
    return tuple(result)

@pytest.mark.parametrize("planet1, planet2, expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Venus", "Earth", ("Mercury")),
    ("Neptune", "Jupiter", ()),
    ("Invalid", "Earth", ()),
])
def test_logic_branches_bf(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected