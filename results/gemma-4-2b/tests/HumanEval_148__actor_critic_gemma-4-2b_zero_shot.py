
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

```python
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
    elif planet1 == "Mercury" and planet2 == "Venus":
        return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mercury" and planet2 == "Earth":
        return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mercury" and planet2 == "Mars":
        return ("Venus", "Earth", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mercury" and planet2 == "Jupiter":
        return ("Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mercury" and planet2 == "Saturn":
        return ("Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune")
    elif planet1 == "Mercury" and planet2 == "Uranus":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune")
    elif planet1 == "Mercury" and planet2 == "Neptune":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Venus" and planet2 == "Neptune":
        return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Venus" and planet2 == "Mercury":
        return ("Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Neptune":
        return ("Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Earth" and planet2 == "Mercury":
        return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Venus":
        return ("Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Mars":
        return ("Venus", "Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Jupiter":
        return ("Venus", "Mars", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Saturn":
        return ("Venus", "Mars", "Jupiter", "Uranus", "Neptune")
    elif planet1 == "Earth" and planet2 == "Uranus":
        return ("Venus", "Mars", "Jupiter", "Saturn", "Neptune")
    elif planet1 == "Earth" and planet2 == "Neptune":
        return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "Mars" and planet2 == "Neptune":
        return ("Jupiter", "Saturn", "Uranus")
    elif planet1 == "Mars" and planet2 == "Mercury":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Venus":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Earth":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Jupiter":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Saturn":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Uranus":
        return ("Jupiter", "Saturn", "Uranus", "Neptune")
    elif planet1 == "Mars" and planet2 == "Neptune":
        return ("Jupiter", "Saturn", "Uranus")
    elif planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus")
    elif planet1 == "Jupiter" and planet2 == "Mercury":
        return ("Saturn", "Uranus", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Venus":
        return ("Saturn", "Uranus", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Earth":
        return ("Saturn", "Uranus", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Mars":
        return ("Saturn", "Uranus", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Saturn":
        return ("Uranus", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Uranus":
        return ("Saturn", "Neptune")
    elif planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus")
    elif planet1 == "Saturn" and planet2 == "Neptune":
        return ("Uranus")
    elif planet1 == "Saturn" and planet2 == "Mercury":
        return ("Uranus", "Neptune")
    elif planet1 == "Saturn" and planet2 == "Venus":
        return ("Uranus", "Neptune")
    elif planet1 == "Saturn" and planet2 == "Earth":
        return ("Uranus", "Neptune")
    elif planet1 == "Saturn" and planet2 == "Mars":
        return ("Uranus", "Neptune")
    elif planet1 == "Saturn" and planet2 == "Jupiter":
        return ("Uranus", "Neptune")
    elif planet1 == "Saturn" and planet2 == "Uranus":
        return ("Neptune")
    elif planet1 == "Saturn" and planet2 == "Neptune":
        return ("Uranus")
    elif planet1 == "Uranus" and planet2 == "Neptune":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Mercury":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Venus":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Earth":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Mars":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Jupiter":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Saturn":
        return ("Neptune")
    elif planet1 == "Uranus" and planet2 == "Uranus":
        return ()
    elif planet1 == "Uranus" and planet2 == "Neptune":
        return ()
    elif planet1 == "Neptune" and planet2 == "Mercury":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    elif planet1 == "