
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
import pytest

def test_get_max_triples_minimum_n():
    # Smallest positive integer n=1: no triples possible
    assert get_max_triples(1) == 0

def test_get_max_triples_below_triple_threshold():
    # n=3: smallest n that can form a triple, but (1, 0, 1) mod 3 sum is 2
    assert get_max_triples(3) == 0

def test_get_max_triples_first_non_zero():
    # n=4: first n where a triple sum is a multiple of 3
    # a = [1, 3, 7, 13] -> mod 3 = [1, 0, 1, 1]. Triple (1, 1, 1) exists.
    assert get_max_triples(4) == 1

# Focus: Logic Branches
import pytest

def test_get_max_triples_small_n():
    # Case where n < 3: No triples can be formed regardless of values
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_single_group():
    # Case where only one remainder group (C1) has enough elements to form a triple
    # n=4: a = [1, 3, 7, 13] -> mods = [1, 0, 1, 1]. C0=1, C1=3. comb(3,3) = 1
    assert get_max_triples(4) == 1
    # n=5: a = [1, 3, 7, 13, 21] -> mods = [1, 0, 1, 1, 0]. C0=2, C1=3. comb(3,3) = 1
    assert get_max_triples(5) == 1

def test_get_max_triples_multiple_groups():
    # Case where both remainder groups (C0 and C1) can form triples
    # n=8: i=1..8. 
    # i mod 3 == 2: {2, 5, 8} -> C0 = 3
    # i mod 3 == 0 or 1: {1, 3, 4, 6, 7} -> C1 = 5
    # Result: comb(3, 3) + comb(5, 3) = 1 + 10 = 11
    assert get_max_triples(8) == 11

# Focus: Type Scenarios
import pytest

def test_get_max_triples_minimum_boundary():
    """Test with the smallest positive integer n where no triples can exist."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_small_valid_range():
    """Test with n values around the threshold where the first triple becomes possible."""
    # n=3: a=[1, 3, 7], sum=11 (not multiple of 3)
    assert get_max_triples(3) == 0
    # n=4: a=[1, 3, 7, 13], triple (1, 7, 13) sum=21
    assert get_max_triples(4) == 1

def test_get_max_triples_large_integer():
    """Test with a large integer to ensure efficiency and correct handling of large counts."""
    # For n=1000:
    # count_0 (a[i] % 3 == 0) = 1000 // 3 = 333
    # count_1 (a[i] % 3 == 1) = 1000 - 333 = 667
    # Result = comb(333, 3) + comb(667, 3) = 6,101,546 + 49,234,445 = 55,335,991
    assert get_max_triples(1000) == 55335991