
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


# Focus: Boundary Values
def test_get_max_triples_min_n():
    # Boundary: Minimum positive integer n
    assert get_max_triples(1) == 0

def test_get_max_triples_min_triple_size():
    # Boundary: Minimum n required to form a single triple
    # a = [1, 3, 7], sum = 11 (not a multiple of 3)
    assert get_max_triples(3) == 0

def test_get_max_triples_first_valid_triple():
    # Boundary: Smallest n that produces a non-zero result
    # a = [1, 3, 7, 13], triple (1, 7, 13) sums to 21
    assert get_max_triples(4) == 1

# Focus: Logic Branches
import pytest

def test_get_max_triples_insufficient_n():
    # Branch: n < 3, where no triples can possibly be formed
    assert get_max_triples(2) == 0

def test_get_max_triples_single_remainder_group():
    # Branch: n is large enough to form a triple from one remainder group (C1), but not the other (C0)
    # n=4: a = [1, 3, 7, 13] -> mods = [1, 0, 1, 1]. C0=1, C1=3.
    # Combinations: comb(1, 3) + comb(3, 3) = 0 + 1 = 1
    assert get_max_triples(4) == 1

def test_get_max_triples_both_remainder_groups():
    # Branch: n is large enough to form triples from both remainder groups (C0 and C1)
    # n=8: i=2,5,8 (mod 0) -> C0=3; i=1,3,4,6,7 (mod 1) -> C1=5
    # Combinations: comb(3, 3) + comb(5, 3) = 1 + 10 = 11
    assert get_max_triples(8) == 11

# Focus: Large Input Values
import pytest

def test_get_max_triples_large_n1():
    # n = 100,000
    # c0 = floor(100001 / 3) = 33333
    # c1 = 100000 - 33333 = 66667
    # result = comb(33333, 3) + comb(66667, 3)
    # comb(33333, 3) = (33333 * 33332 * 33331) // 6 = 6172469135805
    # comb(66667, 3) = (66667 * 66666 * 66665) // 6 = 49383333333335
    # Total = 55555802469140
    assert get_max_triples(100000) == 55555802469140

def test_get_max_triples_large_n2():
    # n = 1,000,000
    # c0 = floor(1000001 / 3) = 333333
    # c1 = 1000000 - 333333 = 666667
    # result = comb(333333, 3) + comb(666667, 3)
    # comb(333333, 3) = (333333 * 333332 * 333331) // 6 = 6172839506172833
    # comb(666667, 3) = (666667 * 666666 * 666665) // 6 = 49382716049382717
    # Total = 55555555555555550
    assert get_max_triples(1000000) == 55555555555555550