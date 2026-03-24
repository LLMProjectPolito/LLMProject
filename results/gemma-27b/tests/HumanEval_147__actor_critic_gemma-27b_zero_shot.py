
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
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# Test Cases
class TestGetMaxTriples:

    def test_get_max_triples_example(self):
        assert get_max_triples(5) == 1

    @pytest.mark.parametrize("n", [1, 2, 3, 4])
    def test_get_max_triples_small_inputs(self, n):
        assert get_max_triples(n) == 0

    def test_get_max_triples_key_values(self):
        assert get_max_triples(6) == 20
        assert get_max_triples(10) == 120
        assert get_max_triples(15) == 455

    def test_get_max_triples_larger_input(self):
        assert get_max_triples(20) == 1140
        assert get_max_triples(30) == 4060

    def test_get_max_triples_edge_case(self):
        assert get_max_triples(0) == 0

    def test_get_max_triples_negative_input(self):
        with pytest.raises(TypeError):
            get_max_triples(-1)

    def test_get_max_triples_large_input(self):
        assert get_max_triples(50) == 19600
        assert get_max_triples(100) == 161700

    def test_get_max_triples_remainder_pattern(self):
        # Test case where a has a predictable distribution of remainders when divided by 3
        # n = 9 results in a = [1, 3, 7, 13, 21, 31, 43, 57, 73]
        # Remainders mod 3: [1, 0, 1, 1, 0, 1, 1, 0, 1]
        assert get_max_triples(9) == 84