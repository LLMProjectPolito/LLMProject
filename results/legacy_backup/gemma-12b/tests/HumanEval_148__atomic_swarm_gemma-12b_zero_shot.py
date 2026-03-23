import pytest
import math

def test_basic():
    from solution import bf
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_edge_invalid_planets():
    """Tests the edge case where both input planets are invalid."""
    from solution import bf
    result = bf("Pluto", "Ceres")
    assert result == ()

def test_invalid_planet_names():
    from solution import bf
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Earth", "Marsian") == ()
    assert bf("Invalid", "Valid") == ()
    assert bf("Valid", "Invalid") == ()