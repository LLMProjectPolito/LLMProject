import pytest

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_invalid_both():
    assert bf("Pluto", "Ceres") == ()

def test_bf_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_neptune_neptune():
    assert bf("Neptune", "Neptune") == ()

def test_bf_venus_mars():
    assert bf("Venus", "Mars") == ("Earth",)

def test_bf_mars_venus():
    assert bf("Mars", "Venus") == ()

def test_bf_uranus_jupiter():
    assert bf("Uranus", "Jupiter") == ("Saturn",)