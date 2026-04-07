
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
import math

def test_get_max_triples():
    assert get_max_triples(5) == 1

def test_edge_n_equals_1(n):
    """Test case for n = 1, which should return 0."""
    from your_module import get_max_triples  # Replace your_module
    assert get_max_triples(1) == 0

def test_get_max_triples_invalid_input():
    """Test with n = 0, which should return 0."""
    from your_module import get_max_triples  # Replace your_module
    assert get_max_triples(0) == 0