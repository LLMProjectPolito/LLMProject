import pytest

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_both_invalid():
    assert bf("Pluto", "X") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_mercury_neptune():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_venus_mars():
    assert bf("Venus", "Mars") == ("Earth",)

def test_bf_mars_venus():
    assert bf("Mars", "Venus") == ("Earth",)

def test_bf_saturn_jupiter():
    assert bf("Saturn", "Jupiter") == ()

def test_bf_jupiter_saturn():
    assert bf("Jupiter", "Saturn") == ()