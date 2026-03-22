import pytest

def test_bf_valid_planets():
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
    assert bf("Mars", "Jupiter") == ("Earth",)
    assert bf("Saturn", "Uranus") == ()
    assert bf("Uranus", "Neptune") == ()
    assert bf("Neptune", "Mercury") == planets[:-1]

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Earth", "MarsX") == ()
    assert bf("MarsX", "Earth") == ()
    assert bf("MarsX", "MarsX") == ()
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

def test_bf_same_planet():
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    assert bf("Mercury", "Mercury") == ()
    assert bf("Venus", "Venus") == ()
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()
    assert bf("Jupiter", "Jupiter") == ()
    assert bf("Saturn", "Saturn") == ()
    assert bf("Uranus", "Uranus") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_planet_order():
    assert bf("Neptune", "Mercury") != ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Uranus", "Venus") == ()
    assert bf("Venus", "Uranus") == ()
    assert bf("Saturn", "Mars") == ()
    assert bf("Mars", "Saturn") == ()
    assert bf("Earth", "Jupiter") == ("Mars",)
    assert bf("Jupiter", "Earth") == ()