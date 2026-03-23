```python
import pytest

def bf(planet1, planet2):
    """
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
    """
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    planet1_orbit = "Mercury"
    planet2_orbit = "Neptune"
    
    planets = []
    
    if planet1 == "Mercury":
        planets.append("Venus")
        planets.append("Earth")
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
    elif planet2 == "Mercury":
        planets.append("Venus")
        planets.append("Earth")
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
    elif planet1 == "Venus":
        planets.append("Earth")
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
    elif planet2 == "Venus":
        planets.append("Earth")
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
    elif planet1 == "Earth":
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet2 == "Earth":
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet1 == "Mars":
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet2 == "Mars":
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet1 == "Jupiter":
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet2 == "Jupiter":
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet1 == "Saturn":
        planets.append("Uranus")
        planets.append("Neptune")
    else:
        return ()
    
    return tuple(planets)