import pytest
import math

def test_basic():
    assert solve("#a@C") == "#A@c"

def test_edge():
    assert solve("1234") == "4321"

def test_no_letters():
    assert solve("1234") == "4321"