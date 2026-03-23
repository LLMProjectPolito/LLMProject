import pytest

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ()
    assert bf("Saturn", "Jupiter") == ()
    assert bf("Neptune", "Saturn") == ("Uranus",)
    assert bf("Uranus", "Neptune") == ()
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()
    assert bf("X", "Earth") == ()
    assert bf("123", "Mars") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Earth", "X") == ()
    assert bf("Mars", "123") == ()

def test_bf_both_invalid():
    assert bf("Pluto", "X") == ()
    assert bf("123", "456") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_case_sensitivity():
    assert bf("jupiter", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("jupiter", "neptune") == ()

def test_bf_empty_string():
    assert bf("", "Earth") == ()
    assert bf("Earth", "") == ()
    assert bf("", "") == ()

def test_bf_edge_cases():
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Mercury") == ()
    assert bf("Neptune", "Uranus") == ()
    assert bf("Uranus", "Neptune") == ()