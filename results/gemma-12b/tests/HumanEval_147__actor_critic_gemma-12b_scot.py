
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

def test_get_max_triples_n_negative():
    """Test with a negative input. The function should return 0."""
    assert get_max_triples(-5) == 0

@pytest.mark.parametrize("n, expected", [(5, 1), (6, 2), (7, 3)])
def test_get_max_triples_n_range(n, expected):
    """Test for n = 5, 6, 7. Expected values are 1, 2, 3 respectively."""
    assert get_max_triples(n) == expected

def test_get_max_triples_n_intermediate():
    """Test with intermediate values of n."""
    assert get_max_triples(8) == 6
    assert get_max_triples(9) == 8
    assert get_max_triples(11) == 14
    assert get_max_triples(12) == 17

def test_get_max_triples_n_large():
    """Test with a large value of n (20, 50, 100) to check for potential overflow or performance issues."""
    assert get_max_triples(20) == 114
    assert get_max_triples(50) == 434
    assert get_max_triples(100) == 1617

def test_get_max_triples_n_0():
    """Test with n = 0. The function should return 0."""
    assert get_max_triples(0) == 0

@pytest.mark.parametrize("n", [1, 2, 3])
def test_get_max_triples_n_less_than_4(n):
    """Test with n < 4. The function should return 0."""
    assert get_max_triples(n) == 0