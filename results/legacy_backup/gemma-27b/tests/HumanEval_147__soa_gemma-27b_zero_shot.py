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
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_get_max_triples_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_4():
    assert get_max_triples(4) == 0

def test_get_max_triples_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_6():
    assert get_max_triples(6) == 3

def test_get_max_triples_7():
    assert get_max_triples(7) == 6

def test_get_max_triples_8():
    assert get_max_triples(8) == 10

def test_get_max_triples_9():
    assert get_max_triples(9) == 16

def test_get_max_triples_10():
    assert get_max_triples(10) == 22

def test_get_max_triples_11():
    assert get_max_triples(11) == 30

def test_get_max_triples_12():
    assert get_max_triples(12) == 39

def test_get_max_triples_13():
    assert get_max_triples(13) == 50

def test_get_max_triples_14():
    assert get_max_triples(14) == 63

def test_get_max_triples_15():
    assert get_max_triples(15) == 78

def test_get_max_triples_20():
    assert get_max_triples(20) == 220

def test_get_max_triples_30():
    assert get_max_triples(30) == 495