
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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_get_max_triples():
    assert get_max_triples(5) == 1
    assert get_max_triples(10) == 2
    assert get_max_triples(15) == 3
    assert get_max_triples(20) == 4
    assert get_max_triples(25) == 5
    assert get_max_triples(30) == 6
    assert get_max_triples(35) == 7
    assert get_max_triples(40) == 8
    assert get_max_triples(45) == 9
    assert get_max_triples(50) == 10
    assert get_max_triples(55) == 11
    assert get_max_triples(60) == 12
    assert get_max_triples(65) == 13
    assert get_max_triples(70) == 14
    assert get_max_triples(75) == 15
    assert get_max_triples(80) == 16
    assert get_max_triples(85) == 17
    assert get_max_triples(90) == 18
    assert get_max_triples(95) == 19
    assert get_max_triples(100) == 20
    assert get_max_triples(105) == 21
    assert get_max_triples(110) == 22
    assert get_max_triples(115) == 23
    assert get_max_triples(120) == 24
    assert get_max_triples(125) == 25
    assert get_max_triples(130) == 26
    assert get_max_triples(135) == 27
    assert get_max_triples(140) == 28
    assert get_max_triples(145) == 29
    assert get_max_triples(150) == 30
    print("All tests passed!")