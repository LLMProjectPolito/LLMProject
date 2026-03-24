import pytest

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_neptune_neptune():
    assert bf("Neptune", "Neptune") == ()

def test_bf_venus_mars():
    assert bf("Venus", "Mars") == ("Earth",)

def test_bf_mars_jupiter():
    assert bf("Mars", "Jupiter") == ("Jupiter",)

def test_bf_invalid_planet1():
    assert bf("Pluto", "Earth") == ()

def test_bf_invalid_planet2():
    assert bf("Earth", "Pluto") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Ceres") == ()

def test_bf_planet1_after_planet2():
    assert bf("Saturn", "Venus") == ("Uranus", "Neptune")

def test_bf_planet1_and_planet2_same():
    assert bf("Earth", "Earth") == ()

def test_bf_mercury_venus():
    assert bf("Mercury", "Venus") == ()

def test_bf_venus_earth():
    assert bf("Venus", "Earth") == ()