import pytest
import math

import pytest

def test_basic():
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

import pytest

def test_edge():
    """Test case for invalid planet names."""
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

import pytest

def test_invalid_planet_names():
    """Test case with invalid planet names."""
    assert bf("Pluto", "X") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Invalid", "Venus") == ()