
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

def test_get_max_triples_minimal_n():
    """
    Test the smallest possible n that can form a triple (n=3).
    a = [1, 3, 7]. The only triple is (1, 3, 7), sum = 11, 
    which is not divisible by 3. Expected output: 0.
    """
    assert get_max_triples(3) == 0

def test_get_max_triples_first_dual_contribution():
    """
    Edge case n=8: The first instance where both possible triple types 
    (three 0 mod 3 and three 1 mod 3) contribute to the total.
    a = [1, 3, 7, 13, 21, 31, 43, 57]
    a % 3 = [1, 0, 1, 1, 0, 1, 1, 0]
    c0 = 3, c1 = 5
    Combinations: comb(3, 3) + comb(5, 3) = 1 + 10 = 11
    """
    assert get_max_triples(8) == 11