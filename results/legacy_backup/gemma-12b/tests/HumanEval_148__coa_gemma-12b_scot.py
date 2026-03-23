import pytest
import math


# Focus: Boundary Values
import pytest

def test_bf_boundary_mercury_venus():
    """Test boundary values: Mercury and Venus"""
    assert bf("Mercury", "Venus") == ()

def test_bf_boundary_venus_earth():
    """Test boundary values: Venus and Earth"""
    assert bf("Venus", "Earth") == ()

def test_bf_boundary_neptune_uranus():
    """Test boundary values: Neptune and Uranus"""
    assert bf("Neptune", "Uranus") == ()

# Focus: Invalid Input
def test_invalid_planet_names():
    """Test case: Invalid planet names provided."""
    from your_module import bf  # Replace your_module
    assert bf("InvalidPlanet1", "Neptune") == ()
    assert bf("Jupiter", "InvalidPlanet2") == ()
    assert bf("InvalidPlanet1", "InvalidPlanet2") == ()

def test_invalid_planet_name_mix():
    """Test case: One valid and one invalid planet name."""
    from your_module import bf  # Replace your_module
    assert bf("Earth", "InvalidPlanet") == ()
    assert bf("InvalidPlanet", "Earth") == ()

def test_empty_input():
    """Test case: Empty strings as input."""
    from your_module import bf  # Replace your_module
    assert bf("", "") == ()

# Focus: Logic Branches
def test_bf_planets_between_jupiter_and_neptune():
    """Test case for planets between Jupiter and Neptune."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_planets_between_earth_and_mercury():
    """Test case for planets between Earth and Mercury."""
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_planets_between_mercury_and_uranus():
    """Test case for planets between Mercury and Uranus."""
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")