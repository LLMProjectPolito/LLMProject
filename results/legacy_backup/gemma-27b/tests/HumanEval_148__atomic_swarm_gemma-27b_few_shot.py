import pytest
import math

def test_bf_basic():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_invalid_input():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Xyz") == ()

import pytest

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Earth", "Xyz") == ()
    assert bf("Invalid", "Venus") == ()