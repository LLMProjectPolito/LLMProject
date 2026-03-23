import pytest
import math

def test_bf_invalid_planets():
    assert bf("Pluto", "Neptune") == ()