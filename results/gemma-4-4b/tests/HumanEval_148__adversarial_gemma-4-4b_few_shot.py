
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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
    try:
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
    except ValueError:
        return ()

    start = min(index1, index2) + 1
    end = max(index1, index2)
    
    between_planets = tuple(planets[start:end])
    return between_planets


@pytest.mark.parametrize("input_string, expected_result", [
    ("radar", True),
    ("hello", False),
    ("", True),
])
def test_palindrome_basic(input_string, expected_result):
    assert is_palindrome(input_string) == expected_result


@pytest.mark.parametrize("input_list, expected_result", [
    ([1, 2, 3], 3),
    ([], None),
])
def test_max_positive(input_list, expected_result):
    assert get_max(input_list) == expected_result


@pytest.mark.parametrize("planet1, planet2, expected_result", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Neptune", "Mercury", ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")),
    ("Mars", "Mars", ()),
    ("Pluto", "Neptune", ()),
])
def test_bf(planet1, planet2, expected_result):
    assert bf(planet1, planet2) == expected_result