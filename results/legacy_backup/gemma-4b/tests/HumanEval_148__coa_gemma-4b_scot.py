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

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `bf` should return a tuple of planets whose orbits lie between two given planets, sorted by proximity to the sun.
### Boundary values are the start and end planets. We need to test cases where planet1 is the closest, planet2 is the furthest, and planet1 is the furthest.
### STEP 2: PLAN - List test functions names and scenarios.
### test_bf_closest
### test_bf_furthest
### test_bf_reverse_order
### STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("planet1, planet2", [
    ("Mercury", "Neptune"),
    ("Earth", "Mercury"),
    ("Mercury", "Uranus"),
])
def test_bf_closest(planet1, planet2):
    assert bf(planet1, planet2) == tuple(sorted([p for p in ["Venus", "Earth", "Mars", "Jupiter", "Saturn"] if planet1 < p < planet2]))

@pytest.mark.parametrize("planet1, planet2", [
    ("Mercury", "Neptune"),
    ("Earth", "Mercury"),
    ("Mercury", "Uranus"),
])
def test_bf_furthest(planet1, planet2):
    assert bf(planet1, planet2) == tuple(sorted([p for p in ["Venus", "Earth", "Mars", "Jupiter", "Saturn"] if planet1 > p > planet2]))

@pytest.mark.parametrize("planet1, planet2", [
    ("Jupiter", "Neptune"),
    ("Earth", "Mercury"),
    ("Mercury", "Uranus"),
])
def test_bf_reverse_order(planet1, planet2):
    assert bf(planet2, planet1) == tuple(sorted([p for p in ["Venus", "Earth", "Mars", "Jupiter", "Saturn"] if planet2 < p < planet1]))

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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
    except ValueError:
        return ()

    if idx1 >= idx2:
        return ()

    result = []
    for i in range(idx1 + 1, idx2):
        result.append(planets[i])

    return tuple(result)

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The tests should focus solely on the 'Type Scenarios' dimension, 
### specifically testing different combinations of planet names 
### to ensure the function returns the correct planets in the correct order.
### STEP 2: PLAN - List test functions names and scenarios.
### test_bf_valid_range
### test_bf_invalid_range
### test_bf_same_planet
### STEP 3: CODE - Write the high-quality pytest suite.
def test_bf_valid_range():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_invalid_range():
    assert bf("Jupiter", "Earth") == ()
    assert bf("Mercury", "Venus") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()

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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
    except ValueError:
        return ()

    if idx1 >= idx2:
        return ()

    result = []
    for i in range(idx1 + 1, idx2):
        result.append(planets[i])

    return tuple(result)

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `bf` filters planets based on their orbital position between two given planets.
### The function should handle invalid planet names by returning an empty tuple.
### The function should sort the filtered planets by their proximity to the sun.
### STEP 2: PLAN - List test functions names and scenarios.
### Test case 1: Jupiter and Neptune - checks the correct planets are returned.
### Test case 2: Earth and Mercury - checks the correct planet is returned.
### Test case 3: Mercury and Uranus - checks multiple planets are returned in the correct order.
### STEP 3: CODE - Write the high-quality pytest suite.

def test_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")