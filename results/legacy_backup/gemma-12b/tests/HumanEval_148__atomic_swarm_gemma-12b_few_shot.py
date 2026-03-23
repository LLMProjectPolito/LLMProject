import pytest
import math

def test_bf_basic():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet():
    assert bf("Pluto", "Neptune") == ()