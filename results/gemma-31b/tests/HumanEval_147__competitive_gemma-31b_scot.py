
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
from math import comb

def calculate_expected(n):
    """
    Helper to calculate expected result based on the mathematical property:
    a[i] = i^2 - i + 1
    a[i] % 3 == 0 if i % 3 == 2
    a[i] % 3 == 1 if i % 3 == 0 or i % 3 == 1
    a[i] % 3 == 2 is never possible.
    
    Triples sum to multiple of 3 if:
    - All three are 0 mod 3
    - All three are 1 mod 3
    """
    c0 = (n + 1) // 3
    c1 = n - c0
    return comb(c0, 3) + comb(c1, 3)

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 4),
    (8, 11),
])
def test_small_values(n, expected):
    assert get_max_triples(n) == expected

def test_example_case():
    # Example from docstring: n = 5 -> Output: 1
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n", [10, 20, 50, 100, 1000])
def test_larger_values(n):
    assert get_max_triples(n) == calculate_expected(n)

def test_minimum_positive_integer():
    # n is a positive integer, so n=1 is the minimum
    assert get_max_triples(1) == 0

def test_boundary_triple_size():
    # n=3 is the first case where a triple is even possible
    # a = [1, 3, 7] -> mods [1, 0, 1]. Sum = 2. Not multiple of 3.
    assert get_max_triples(3) == 0

def test_first_valid_triple():
    # n=4: a = [1, 3, 7, 13] -> mods [1, 0, 1, 1]. 
    # Triple (1, 7, 13) sums to 21 (multiple of 3).
    assert get_max_triples(4) == 1