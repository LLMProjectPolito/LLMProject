
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

def test_get_max_triples_first_dual_bin_contribution():
    """
    Test the smallest n where both residues (0 and 1 mod 3) 
    contribute to the total count of triples.
    For n=8:
    a[i] mod 3 sequence: 1, 0, 1, 1, 0, 1, 1, 0
    Count of 0s: 3, Count of 1s: 5
    Triples: comb(3, 3) + comb(5, 3) = 1 + 10 = 11.
    """
    assert get_max_triples(8) == 11

def test_get_max_triples_small_n():
    assert get_max_triples(2) == 0

def test_get_max_triples_minimum_triple_boundary():
    # For n=3, a = [1, 3, 7]. The only triple sum is 1 + 3 + 7 = 11, 
    # which is not a multiple of 3. This tests the smallest possible 
    # case where a triple exists but the condition is not met.
    assert get_max_triples(3) == 0