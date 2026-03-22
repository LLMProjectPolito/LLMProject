import pytest
import math


# Focus: Boundary Values
def test_get_max_triples_boundary_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_boundary_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_boundary_n_3():
    assert get_max_triples(3) == 0

# Focus: Logic Branches
def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n_7():
    assert get_max_triples(7) == 3

# Focus: Type Scenarios
def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n_10():
    assert get_max_triples(10) == 6