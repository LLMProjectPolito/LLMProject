import pytest

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_valid_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Mars", "Jupiter") == ("Earth",)
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Pluto") == ()
    assert bf("Earth", "Venussss") == ()
    assert bf("Venussss", "Earth") == ()
    assert bf("Pluto", "Venussss") == ()
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_planet_order():
    assert bf("Venus", "Earth") == ("Mercury",)
    assert bf("Earth", "Venus") == ()
    assert bf("Mars", "Venus") == ("Earth",)
    assert bf("Venus", "Mars") == ()

def test_bf_edge_cases():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Saturn", "Mercury") == ("Uranus", "Jupiter", "Mars", "Earth", "Venus")
    assert bf("Mercury", "Saturn") == ("Venus", "Earth", "Mars", "Jupiter")