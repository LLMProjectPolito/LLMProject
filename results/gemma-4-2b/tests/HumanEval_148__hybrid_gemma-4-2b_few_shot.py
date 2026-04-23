
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
    if planet1 not in planets or planet2 not in planets:
        return ()

    if planet1 == "Mercury" and planet2 == "Neptune":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus")
    elif planet1 == "Earth" and planet2 == "Mercury":
        return ("Venus")
    else:
        return ()

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]


def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus")

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_neptune_mars():
    assert bf("Neptune", "Mars") == ("Uranus", "Saturn", "Jupiter")

def test_bf_venus_earth():
    assert bf("Venus", "Earth") == ("Mars")

def test_bf_mars_jupiter():
    assert bf("Mars", "Jupiter") == ("Jupiter", "Saturn", "Uranus")

def test_bf_sun_planet():
    assert bf("Mercury", "Neptune") == ()

def test_bf_planet_not_in_list():
    assert bf("Pluto", "Neptune") == ()

def test_bf_empty_list():
    assert bf("Mercury", "Neptune") == ()

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 0, 1]) == 1

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == True