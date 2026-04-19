
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

@pytest.mark.parametrize("n, expected", [
    (1, 0),  # a = [1], no triples
    (2, 0),  # a = [1, 3], no triples
    (3, 0),  # a = [1, 3, 7], mod 3: [1, 0, 1], no triples
    (4, 1),  # a = [1, 3, 7, 13], mod 3: [1, 0, 1, 1], triple (1, 7, 13)
    (5, 1),  # Example case: a = [1, 3, 7, 13, 21], mod 3: [1, 0, 1, 1, 0], triple (1, 7, 13)
    (6, 4),  # a = [1, 3, 7, 13, 21, 31], mod 3: [1, 0, 1, 1, 0, 1], count0=2, count1=4. C(4,3)=4
    (7, 10), # mod 3: [1, 0, 1, 1, 0, 1, 1], count0=2, count1=5. C(5,3)=10
    (8, 20), # mod 3: [1, 0, 1, 1, 0, 1, 1, 0], count0=3, count1=5. C(3,3)+C(5,3)=1+10=11? 
             # Wait: i=2,5,8 are 0 mod 3. i=1,3,4,6,7 are 1 mod 3.
             # count0 = 3, count1 = 5. C(3,3) + C(5,3) = 1 + 10 = 11.
    (9, 21), # count0 = 3, count1 = 6. C(3,3) + C(6,3) = 1 + 20 = 21.
])
def test_get_max_triples_basic(n, expected):
    # Re-calculating n=8 manually:
    # a[1]=1(1), a[2]=3(0), a[3]=7(1), a[4]=13(1), a[5]=21(0), a[6]=31(1), a[7]=43(1), a[8]=57(0)
    # Remainder 0: {3, 21, 57} -> count=3
    # Remainder 1: {1, 7, 13, 31, 43} -> count=5
    # Triples: C(3,3) + C(5,3) = 1 + 10 = 11.
    # Correcting the parametrization for n=8.
    if n == 8:
        expected = 11
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    # For n = 100:
    # count0 = 100 // 3 = 33
    # count1 = 100 - 33 = 67
    # Result = C(33, 3) + C(67, 3)
    # C(33, 3) = (33 * 32 * 31) / 6 = 11 * 16 * 31 = 5456
    # C(67, 3) = (67 * 66 * 65) / 6 = 67 * 11 * 65 = 47905
    # Total = 5456 + 47905 = 53361
    assert get_max_triples(100) == 53361

def test_get_max_triples_minimum_n():
    # The problem states n is a positive integer.
    assert get_max_triples(1) == 0

def test_get_max_triples_no_triples_possible():
    # n < 3 cannot have any triples
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_all_same_remainder():
    # This is impossible given the formula i^2 - i + 1, 
    # but we test the logic for small n where only one remainder type dominates.
    # n=4: count0=1, count1=3. Only C(3,3) possible.
    assert get_max_triples(4) == 1