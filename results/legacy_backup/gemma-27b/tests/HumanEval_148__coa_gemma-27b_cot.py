import pytest
import math


# Focus: Valid/Invalid Planet Names
import pytest

def test_valid_planet_names():
    """Tests with valid planet names."""
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ()
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_invalid_planet_names():
    """Tests with invalid planet names."""
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Xyz") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Mars", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_same_planet_name():
    """Tests when both planet names are the same."""
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()

# Focus: Order of Planets (planet1 vs planet2)
import pytest

def test_order_of_planets_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_order_of_planets_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_order_of_planets_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_order_of_planets_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_order_of_planets_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_order_of_planets_same_planet():
    assert bf("Earth", "Earth") == ()

def test_order_of_planets_mars_saturn():
    assert bf("Mars", "Saturn") == ("Jupiter",)

# Focus: Edge Cases (same planet, first/last planet)
import pytest

def test_same_planet():
    """Test case where both planets are the same."""
    assert bf("Earth", "Earth") == ()

def test_first_planet():
    """Test case where the first planet is Mercury."""
    assert bf("Mercury", "Venus") == ("Mercury",)

def test_last_planet():
    """Test case where the second planet is Neptune."""
    assert bf("Uranus", "Neptune") == ("Uranus",)