import pytest
from your_module import get_max_triples  # Import the function from your module

def test_get_max_triples_edge_cases():
    with pytest.raises(ValueError):
        get_max_triples(0)
    with pytest.raises(ValueError):
        get_max_triples(-1)
    with pytest.raises(ValueError):
        get_max_triples(float('nan'))

def test_get_max_triples_boundary_conditions():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 1
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1

def test_get_max_triples_normal_cases():
    assert get_max_triples(6) == 0
    assert get_max_triples(7) == 2
    assert get_max_triples(10) == 3

def test_get_max_triples_invalid_cases():
    with pytest.raises(TypeError):
        get_max_triples('a')
    with pytest.raises(TypeError):
        get_max_triples(1.2)
    with pytest.raises(TypeError):
        get_max_triples([5])

def test_get_max_triples_medium_input():
    n = 15
    expected_result = 10
    assert get_max_triples(n) == expected_result

def test_get_max_triples_large_input():
    n = 100
    expected_result = 5050  # Calculate the expected result manually or use a calculator
    assert get_max_triples(n) == expected_result