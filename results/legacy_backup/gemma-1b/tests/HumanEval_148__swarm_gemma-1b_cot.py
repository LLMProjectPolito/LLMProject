import pytest
import math

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Saturn")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")

def test_bf_orbit_between():
    assert "Saturn" in bf("Jupiter", "Neptune")
    assert "Uranus" in bf("Earth", "Mercury")
    assert "Venus" in bf("Mercury", "Uranus")
    assert "Mars" in bf("Venus", "Earth")
    assert "Jupiter" in bf("Venus", "Earth")
    assert "Saturn" in bf("Mars", "Uranus")
    assert "Neptune" in bf("Jupiter", "Uranus")