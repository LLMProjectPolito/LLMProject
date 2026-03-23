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
    assert bf("Earth", "MarsX") == ()
    assert bf("EarthX", "Mars") == ()
    assert bf("Earth", "EarthX") == ()
    assert bf("EarthX", "Earth") == ()

def test_invalid_input_types():
    assert bf(123, "Neptune") == ()
    assert bf("Jupiter", 456) == ()
    assert bf(123, 456) == ()
    assert bf([1,2], "Neptune") == ()
    assert bf("Jupiter", [1,2]) == ()

def test_empty_string_input():
    assert bf("", "Neptune") == ()
    assert bf("Jupiter", "") == ()
    assert bf("", "") == ()

# Focus: Logic Branches
import pytest

def test_bf_between_planets():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_adjacent_planets():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_multiple_planets():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")