import pytest
import math


# Focus: Boundary Values
def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_empty():
    assert find_max([]) == ""

# Focus: Type Scenarios
def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_empty():
    assert find_max([]) == ""

# Focus: Logic Branches
def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_empty():
    assert find_max([]) == ""