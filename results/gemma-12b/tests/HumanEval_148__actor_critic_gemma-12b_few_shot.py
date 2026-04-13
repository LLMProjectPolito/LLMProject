
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

def bf(planet1, planet2):
    '''
    Returns a tuple of planets located between planet1 and planet2 (exclusive),
    sorted by proximity to the sun. Returns an empty tuple if either planet
    is not a valid planet name.
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if not isinstance(planet1, str) or not isinstance(planet2, str):
        raise TypeError("Planet names must be strings.")

    if planet1 not in planets or planet2 not in planets:
        raise ValueError("Invalid planet name(s).")

    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    start_index = min(index1, index2) + 1
    end_index = max(index1, index2)

    between_planets = tuple(planets[start_index:end_index])
    return between_planets