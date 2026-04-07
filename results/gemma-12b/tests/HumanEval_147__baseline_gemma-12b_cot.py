
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
    a = [(i * i - i + 1) for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

class TestGetMaxTriples:
    def test_n_equals_1(self):
        assert get_max_triples(1) == 0

    def test_n_equals_2(self):
        assert get_max_triples(2) == 0

    def test_n_equals_3(self):
        assert get_max_triples(3) == 0

    def test_n_equals_4(self):
        assert get_max_triples(4) == 0

    def test_n_equals_5(self):
        assert get_max_triples(5) == 1

    def test_n_equals_6(self):
        assert get_max_triples(6) == 2

    def test_n_equals_7(self):
        assert get_max_triples(7) == 4

    def test_n_equals_8(self):
        assert get_max_triples(8) == 6

    def test_n_equals_9(self):
        assert get_max_triples(9) == 9

    def test_n_equals_10(self):
        assert get_max_triples(10) == 13

    def test_large_n(self):
        assert get_max_triples(100) == 1683