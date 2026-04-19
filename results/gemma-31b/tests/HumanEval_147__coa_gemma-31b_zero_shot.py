
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
def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 0

# Focus: Logic Branches
import pytest

def test_get_max_triples_insufficient_n():
    # Logic Branch: n < 3, where no triples can be formed regardless of values
    assert get_max_triples(2) == 0

def test_get_max_triples_single_group_dominant():
    # Logic Branch: n is large enough for triples, but only one modulo group (C1) has >= 3 elements
    # n = 4: a = [1, 3, 7, 13] -> mods = [1, 0, 1, 1]
    # C0 = 1, C1 = 3. Triples: comb(1, 3) + comb(3, 3) = 0 + 1 = 1
    assert get_max_triples(4) == 1

def test_get_max_triples_both_groups_dominant():
    # Logic Branch: Both modulo groups (C0 and C1) have >= 3 elements
    # n = 8: a = [1, 3, 7, 13, 21, 31, 43, 57] -> mods = [1, 0, 1, 1, 0, 1, 1, 0]
    # C0 = 3, C1 = 5. Triples: comb(3, 3) + comb(5, 3) = 1 + 10 = 11
    assert get_max_triples(8) == 11

# Focus: Type Scenarios
import pytest

def test_get_max_triples_minimum_n():
    """Test with the smallest possible positive integer n."""
    assert get_max_triples(1) == 0

def test_get_max_triples_boundary_triple_size():
    """Test with n=3, the minimum size required to form a triple."""
    assert get_max_triples(3) == 0

def test_get_max_triples_large_n():
    """Test with a larger n to verify combinatorial logic (n=10)."""
    # For n=10: 
    # a[i] % 3 == 0 for i in {2, 5, 8} (count = 3)
    # a[i] % 3 == 1 for i in {1, 3, 4, 6, 7, 9, 10} (count = 7)
    # Combinations: comb(3, 3) + comb(7, 3) = 1 + 35 = 36
    assert get_max_triples(10) == 36