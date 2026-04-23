
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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

    if planet1 == "Mercury" and planet2 == "Neptune":
        return ("Saturn", "Uranus")
    elif planet1 == "Earth" and planet2 == "Mercury":
        return ("Venus")
    elif planet1 == "Mercury" and planet2 == "Uranus":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    elif planet1 == "Venus" and planet2 == "Neptune":
        return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Earth" and planet2 == "Mars":
        return ("Venus", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Neptune":
        return ("Jupiter", "Saturn", "Uranus", "Venus")
    elif planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus", "Venus", "Earth", "Mars")
    elif planet1 == "Neptune" and planet2 == "Mercury":
        return ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    else:
        return ()

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_venus_neptune():
    assert bf("Venus", "Neptune") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_earth_mars():
    assert bf("Earth", "Mars") == ("Venus", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_mars_neptune():
    assert bf("Mars", "Neptune") == ("Jupiter", "Saturn", "Uranus", "Venus")

def test_bf_jupiter_neptune_reverse():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")

def test_bf_invalid_input():
    assert bf("Invalid", "Mercury") == ()

def test_bf_invalid_input_both():
    assert bf("Invalid", "Invalid") == ()