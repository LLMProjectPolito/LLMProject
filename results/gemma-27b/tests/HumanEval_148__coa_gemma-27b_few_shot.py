import pytest
import math


# Focus: Valid/Invalid Planet Names
import pytest

def test_valid_planet_names():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Saturn", "Mars") == ("Jupiter",)

def test_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Alpha Centauri") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Jupiter", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_same_planet_name():
    assert bf("Earth", "Earth") == ()

# Focus: Order of Planets (planet1 & planet2)
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

# Focus: Edge Cases (same planet, planets at extremes)
def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_planets_at_extremes():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_planets_at_extremes_reversed():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")