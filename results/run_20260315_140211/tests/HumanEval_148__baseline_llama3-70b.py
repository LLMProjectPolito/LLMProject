import pytest

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_invalid_planet():
    assert bf("Invalid", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Invalid") == ()

def test_bf_same_planet():
    assert bf("Jupiter", "Jupiter") == ()

def test_bf_reverse_order():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")

def test_bf_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_earth_earth():
    assert bf("Earth", "Earth") == ()