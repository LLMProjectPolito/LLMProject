import pytest
import math


# Focus: Valid/Invalid Planet Names
import pytest

def test_valid_planet_names():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Saturn", "Earth") == ("Jupiter",)

def test_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Xyz") == ()
    assert bf("Invalid", "Venus") == ()
    assert bf("Mars", "Not a planet") == ()
    assert bf("FakePlanet", "FakePlanet2") == ()

def test_same_planet_name():
    assert bf("Earth", "Earth") == ()

# Focus: Order of Planets (planet1 vs planet2)
import pytest

def test_order_of_planets_jupiter_neptune():
    from solution import bf
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_order_of_planets_earth_mercury():
    from solution import bf
    assert bf("Earth", "Mercury") == ("Venus",)

def test_order_of_planets_mercury_uranus():
    from solution import bf
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

# Focus: Edge Cases (same planet, first/last planet)
import pytest

def test_same_planet():
    assert bf("Earth", "Earth") == ()

def test_first_planet():
    assert bf("Mercury", "Venus") == ()

def test_last_planet():
    assert bf("Neptune", "Neptune") == ()