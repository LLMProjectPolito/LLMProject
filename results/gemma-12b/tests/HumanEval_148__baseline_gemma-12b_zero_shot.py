
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

def test_bf_jupiter_neptune():
    """Test case: Jupiter and Neptune"""
    result = bf("Jupiter", "Neptune")
    assert result == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    """Test case: Earth and Mercury"""
    result = bf("Earth", "Mercury")
    assert result == ("Venus",)

def test_bf_mercury_uranus():
    """Test case: Mercury and Uranus"""
    result = bf("Mercury", "Uranus")
    assert result == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_venus_mars():
    """Test case: Venus and Mars"""
    result = bf("Venus", "Mars")
    assert result == ("Earth",)

def test_bf_mars_jupiter():
    """Test case: Mars and Jupiter"""
    result = bf("Mars", "Jupiter")
    assert result == ("Saturn",)

def test_bf_saturn_uranus():
    """Test case: Saturn and Uranus"""
    result = bf("Saturn", "Uranus")
    assert result == ("Uranus",)

def test_bf_uranus_neptune():
    """Test case: Uranus and Neptune"""
    result = bf("Uranus", "Neptune")
    assert result == ()

def test_bf_neptune_mercury():
    """Test case: Neptune and Mercury"""
    result = bf("Neptune", "Mercury")
    assert result == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_mercury_mercury():
    """Test case: Mercury and Mercury"""
    result = bf("Mercury", "Mercury")
    assert result == ()

def test_bf_invalid_planet1():
    """Test case: Invalid planet1"""
    result = bf("Pluto", "Neptune")
    assert result == ()

def test_bf_invalid_planet2():
    """Test case: Invalid planet2"""
    result = bf("Jupiter", "Pluto")
    assert result == ()

def test_bf_invalid_planets():
    """Test case: Invalid planets"""
    result = bf("Pluto", "Eris")
    assert result == ()

def test_bf_planet1_equals_planet2():
    """Test case: planet1 equals planet2"""
    result = bf("Earth", "Earth")
    assert result == ()

def test_bf_planet1_after_planet2():
    """Test case: planet1 after planet2"""
    result = bf("Neptune", "Mercury")
    assert result == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")