
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
def test_get_max_triples_n1():
    # Boundary: Minimum positive integer n
    assert get_max_triples(1) == 0

def test_get_max_triples_n3():
    # Boundary: Minimum n required to form a single triple
    assert get_max_triples(3) == 0

def test_get_max_triples_n4():
    # Boundary: Minimum n required to form a valid triple (sum is multiple of 3)
    assert get_max_triples(4) == 1

# Focus: Logic Branches
import pytest

def test_get_max_triples_insufficient_n():
    """Test cases where n is too small to form any triple."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_single_branch():
    """Test cases where only one remainder group (0 or 1) has enough elements to form a triple."""
    # n=4: a mod 3 = [1, 0, 1, 1] -> c0=1, c1=3. Triples: comb(3, 3) = 1
    assert get_max_triples(4) == 1
    # n=5: a mod 3 = [1, 0, 1, 1, 0] -> c0=2, c1=3. Triples: comb(3, 3) = 1
    assert get_max_triples(5) == 1

def test_get_max_triples_dual_branch():
    """Test cases where both remainder groups (0 and 1) can independently form triples."""
    # n=8: a mod 3 = [1, 0, 1, 1, 0, 1, 1, 0] -> c0=3, c1=5
    # Triples: comb(3, 3) + comb(5, 3) = 1 + 10 = 11
    assert get_max_triples(8) == 11

# Focus: Type Scenarios
def test_get_max_triples_minimum_n():
    """Test with the smallest possible positive integer n."""
    assert get_max_triples(1) == 0

def test_get_max_triples_below_triple_threshold():
    """Test with n smaller than the minimum required to form a triple."""
    assert get_max_triples(2) == 0

def test_get_max_triples_at_triple_threshold():
    """Test with n exactly at the minimum required to form a triple, where the sum is not a multiple of 3."""
    assert get_max_triples(3) == 0