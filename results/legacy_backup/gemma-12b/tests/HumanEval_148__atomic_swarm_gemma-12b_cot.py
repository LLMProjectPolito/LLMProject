import pytest
import math

def test_basic():
    from your_module import bf  # Replace your_module
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_empty_range():
    """Test with planet1 and planet2 being the same, resulting in an empty range."""
    from your_module import bf  # Replace your_module
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    result = bf("Mercury", "Mercury")
    assert result == ()

def test_bf_invalid_planet_names():
    """Test with invalid planet names."""
    from your_module import bf  # Replace your_module
    assert bf("Pluto", "Venus") == ()
    assert bf("Earth", "Xenon") == ()
    assert bf("InvalidPlanet", "Mercury") == ()
    assert bf("Mercury", "InvalidPlanet") == ()
    assert bf("InvalidPlanet", "InvalidPlanet") == ()

def test_bf_wrong_type():
    """Test with wrong types for planet names."""
    from your_module import bf  # Replace your_module
    assert bf(123, "Venus") == ()
    assert bf("Earth", 456) == ()
    assert bf([1, 2], "Venus") == ()
    assert bf("Earth", [3, 4]) == ()
    assert bf(123, 456) == ()

def test_bf_same_planet():
    """Test when both planets are the same."""
    from your_module import bf  # Replace your_module
    assert bf("Earth", "Earth") == ()

def test_bf_planet1_after_planet2():
    """Test when planet1 is after planet2 in the solar system."""
    from your_module import bf  # Replace your_module
    assert bf("Neptune", "Mercury") == ()