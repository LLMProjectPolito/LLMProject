
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

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
])
def test_boundary_conditions(n, expected):
    """Tests cases where n is too small to form any triple or results in 0 combinations."""
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n, expected", [
    (4, 1),   # Residues: [1, 0, 1, 1] -> C0=1, C1=3 -> 0 + 1 = 1
    (5, 1),   # Residues: [1, 0, 1, 1, 0] -> C0=2, C1=3 -> 0 + 1 = 1 (Example Case)
    (6, 4),   # Residues: [1, 0, 1, 1, 0, 1] -> C0=2, C1=4 -> 0 + 4 = 4
    (10, 36), # Residues: C0=3, C1=7 -> 1 + 35 = 36
])
def test_known_values(n, expected):
    """Tests specific n values to verify the mathematical pattern and example cases."""
    assert get_max_triples(n) == expected

def test_large_scale_accuracy():
    """
    Verifies accuracy for a larger n using math.comb as the ground truth.
    Pattern for residues mod 3: [1, 0, 1] repeating.
    Count of 0s (n0) follows the sequence: i=2, 5, 8... which is 3k-1.
    n0 = floor((n + 1) / 3)
    """
    n = 100
    n0 = (n + 1) // 3
    n1 = n - n0
    expected = math.comb(n0, 3) + math.comb(n1, 3)
    assert get_max_triples(n) == expected

def test_monotonicity():
    """Verifies that the number of triples is non-decreasing as n increases."""
    results = [get_max_triples(i) for i in range(1, 51)]
    for i in range(len(results) - 1):
        assert results[i] <= results[i+1], f"Failed monotonicity at n={i+1}"

def test_type_integrity():
    """Ensures the function returns an integer for valid inputs."""
    assert isinstance(get_max_triples(5), int)
    assert isinstance(get_max_triples(1), int)