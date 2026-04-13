
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

import pytest
from your_module import get_max_triples  # Replace your_module

def test_get_max_triples_n_0():
    assert get_max_triples(0) == 0  # Edge case: n = 0, no triples possible

@pytest.mark.parametrize("n", [1, 2])
def test_get_max_triples_n_less_than_3(n):
    assert get_max_triples(n) == 0  # Edge cases: n = 1, 2, no triples possible

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 0  # Edge case: n = 3, no triples possible

@pytest.mark.parametrize("n", [5, 6, 7])
def test_get_max_triples_n_range(n):
    assert get_max_triples(n) == n - 4  # Tests for n = 5, 6, 7

@pytest.mark.parametrize("n", [10, 15])
def test_get_max_triples_n_larger_range(n):
    assert get_max_triples(n) == (n * (n - 1) * (n - 2)) // 6  # Tests for n = 10, 15

def test_get_max_triples_large_n():
    assert get_max_triples(100) == 1617  # Large n test to check for performance/overflow

def test_get_max_triples_negative_n():
    with pytest.raises(TypeError):
        get_max_triples(-5)  # Test for negative input

def test_get_max_triples_non_integer_n():
    with pytest.raises(TypeError):
        get_max_triples(3.14)  # Test for non-integer input