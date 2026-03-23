import pytest
import math

def test_basic():
    from solution import bf
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_edge_invalid_planets():
    """
    Test case for invalid planet names as input.
    Verifies that an empty tuple is returned when either planet1 or planet2 is not a valid planet name.
    """
    from your_module import bf  # Replace your_module
    result = bf("InvalidPlanet", "Earth")
    assert result == ()

    result = bf("Earth", "InvalidPlanet")
    assert result == ()

    result = bf("InvalidPlanet", "InvalidPlanet")
    assert result == ()

import pytest

def test_bf_invalid_planet_names():
    """
    Test case for invalid planet names.
    """
    from your_module import bf  # Replace your_module
    assert bf("DoesNotExist", "Neptune") == ()
    assert bf("Mercury", "DoesNotExist") == ()
    assert bf("DoesNotExist", "DoesNotExist") == ()
    assert bf("InvalidPlanet", "Earth") == ()
    assert bf("Earth", "InvalidPlanet") == ()