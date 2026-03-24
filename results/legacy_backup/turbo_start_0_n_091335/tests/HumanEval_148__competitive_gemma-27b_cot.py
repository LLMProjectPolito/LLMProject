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

def test_bf_mercury_mars():
    assert bf("Mercury", "Mars") == ("Venus", "Earth")

def test_bf_venus_saturn():
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")

def test_bf_uranus_mars():
    assert bf("Uranus", "Mars") == ("Neptune",)

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_case_sensitive():
    assert bf("jupiter", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()