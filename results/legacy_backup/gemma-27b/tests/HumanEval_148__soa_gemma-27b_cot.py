import pytest

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ()
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Saturn", "Earth") == ("Jupiter", "Mars")
    assert bf("Uranus", "Saturn") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "X") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_bf_case_sensitivity():
    assert bf("jupiter", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("jupiter", "neptune") == ()

def test_bf_empty_string():
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_edge_cases():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")