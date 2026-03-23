import pytest
import math


# Focus: Boundary Values
def test_bf_boundary_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_boundary_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_boundary_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

# Focus: Invalid Input
def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Xena") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Xena") == ()

# Focus: Logic Branches
def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")