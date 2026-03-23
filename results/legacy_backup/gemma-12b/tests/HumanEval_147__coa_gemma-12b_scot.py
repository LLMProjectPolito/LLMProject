import pytest
import math


# Focus: Boundary Values
import pytest

def test_get_max_triples_boundary_n_1():
    """Test with n = 1 (boundary case)."""
    assert get_max_triples(1) == 0

def test_get_max_triples_boundary_n_2():
    """Test with n = 2 (boundary case)."""
    assert get_max_triples(2) == 0

def test_get_max_triples_boundary_n_3():
    """Test with n = 3 (boundary case)."""
    assert get_max_triples(3) == 0

# Focus: Logic Branches
def test_get_max_triples_n_equals_5():
    """Test case for n = 5, expecting output 1."""
    assert get_max_triples(5) == 1

def test_get_max_triples_n_equals_6():
    """Test case for n = 6, expecting output 2."""
    assert get_max_triples(6) == 2

def test_get_max_triples_n_equals_3():
    """Test case for n = 3, expecting output 0."""
    assert get_max_triples(3) == 0

# Focus: Type Scenarios
def test_get_max_triples_n_is_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_is_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_is_3():
    assert get_max_triples(3) == 0