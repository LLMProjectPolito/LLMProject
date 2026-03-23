import pytest
import math


# Focus: Boundary Values
def test_bf_boundary_mercury_venus():
    assert bf("Mercury", "Venus") == ()

def test_bf_boundary_venus_earth():
    assert bf("Venus", "Earth") == ()

def test_bf_boundary_earth_mars():
    assert bf("Earth", "Mars") == ()

# Focus: Invalid Input
def test_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Earth", "Marsian") == ()
    assert bf("InvalidPlanet", "Neptune") == ()
    assert bf("Jupiter", "InvalidPlanet") == ()
    assert bf("InvalidPlanet", "InvalidPlanet") == ()

def test_invalid_input_types():
    assert bf(123, "Neptune") == ()
    assert bf("Jupiter", 456) == ()
    assert bf(123, 456) == ()
    assert bf([1,2], "Neptune") == ()
    assert bf("Jupiter", [1,2]) == ()

# Focus: Logic Branches
def test_bf_between_jupiter_and_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_between_earth_and_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_between_mercury_and_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")