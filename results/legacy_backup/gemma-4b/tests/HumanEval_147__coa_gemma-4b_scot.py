import pytest
import math


# Focus: Boundary Values
import pytest

def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n_4():
    assert get_max_triples(4) == 1

def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1

# Focus: Type Scenarios
import pytest

def test_type_scenario_int_small():
    assert get_max_triples(5) == 1

def test_type_scenario_int_medium():
    assert get_max_triples(10) == 2

def test_type_scenario_int_large():
    assert get_max_triples(100) == 15

# Focus: Logic Branches
import pytest

def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n_4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1