
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

def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 1

def test_get_max_triples_n_4():
    assert get_max_triples(4) == 1

def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_6():
    assert get_max_triples(6) == 3

def test_get_max_triples_n_7():
    assert get_max_triples(7) == 6

def test_get_max_triples_n_8():
    assert get_max_triples(8) == 10

def test_get_max_triples_n_9():
    assert get_max_triples(9) == 16

def test_get_max_triples_n_10():
    assert get_max_triples(10) == 22

def test_get_max_triples_n_11():
    assert get_max_triples(11) == 30

def test_get_max_triples_n_12():
    assert get_max_triples(12) == 39

def test_get_max_triples_n_13():
    assert get_max_triples(13) == 50

def test_get_max_triples_n_14():
    assert get_max_triples(14) == 63

def test_get_max_triples_n_15():
    assert get_max_triples(15) == 78

def test_get_max_triples_n_20():
    assert get_max_triples(20) == 190

def test_get_max_triples_n_30():
    assert get_max_triples(30) == 406

def test_get_max_triples_n_50():
    assert get_max_triples(50) == 1225

def test_get_max_triples_n_100():
    assert get_max_triples(100) == 4950

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_two():
    assert get_max_triples(2) == 0

def test_get_max_triples_three():
    assert get_max_triples(3) == 1

def test_get_max_triples_four():
    assert get_max_triples(4) == 1

def test_get_max_triples_five():
    assert get_max_triples(5) == 1

def test_get_max_triples_six():
    assert get_max_triples(6) == 3

def test_get_max_triples_seven():
    assert get_max_triples(7) == 6

def test_get_max_triples_eight():
    assert get_max_triples(8) == 10

def test_get_max_triples_nine():
    assert get_max_triples(9) == 16

def test_get_max_triples_ten():
    assert get_max_triples(10) == 22

def test_get_max_triples_large():
    assert get_max_triples(100) == 161700

def test_get_max_triples_mod_0():
    n = 30
    assert get_max_triples(n) == 4495

def test_get_max_triples_mod_1():
    n = 31
    assert get_max_triples(n) == 4960

def test_get_max_triples_mod_2():
    n = 32
    assert get_max_triples(n) == 5426