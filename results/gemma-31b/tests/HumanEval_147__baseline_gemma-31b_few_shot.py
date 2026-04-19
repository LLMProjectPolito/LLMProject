
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

def test_get_max_triples_example():
    """Test the example provided in the docstring."""
    assert get_max_triples(5) == 1

def test_get_max_triples_too_small():
    """Test cases where n is too small to form any triple."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_boundary_three():
    """
    Test n=3. 
    a = [1, 3, 7] -> mods = [1, 0, 1]. 
    Sum = 1+0+1 = 2 (not multiple of 3).
    """
    assert get_max_triples(3) == 0

def test_get_max_triples_boundary_four():
    """
    Test n=4. 
    a = [1, 3, 7, 13] -> mods = [1, 0, 1, 1]. 
    Triple (1, 7, 13) sum is 21 (multiple of 3).
    """
    assert get_max_triples(4) == 1

def test_get_max_triples_six():
    """
    Test n=6.
    a = [1, 3, 7, 13, 21, 31] -> mods = [1, 0, 1, 1, 0, 1]
    C0 (mod 0) = 2, C1 (mod 1) = 4.
    Combinations: comb(2, 3) + comb(4, 3) = 0 + 4 = 4.
    """
    assert get_max_triples(6) == 4

def test_get_max_triples_eight():
    """
    Test n=8.
    a mods = [1, 0, 1, 1, 0, 1, 1, 0]
    C0 = 3, C1 = 5.
    Combinations: comb(3, 3) + comb(5, 3) = 1 + 10 = 11.
    """
    assert get_max_triples(8) == 11

def test_get_max_triples_large():
    """
    Test a larger value of n.
    n = 10.
    C0 = floor((10+1)/3) = 3 (i=2, 5, 8)
    C1 = 10 - 3 = 7
    Combinations: comb(3, 3) + comb(7, 3) = 1 + (7*6*5 / 6) = 1 + 35 = 36.
    """
    assert get_max_triples(10) == 36