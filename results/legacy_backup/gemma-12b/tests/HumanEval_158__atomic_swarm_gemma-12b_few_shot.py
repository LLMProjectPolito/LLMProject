import pytest
import math

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_empty():
    assert find_max([]) == ""

def test_find_max_mixed_types():
    assert find_max(["name", 123, "string"]) == "name"