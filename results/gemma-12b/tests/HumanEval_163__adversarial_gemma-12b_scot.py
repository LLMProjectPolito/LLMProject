
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

class TestGenerateIntegers:
    def test_ascending_order(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_descending_order(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        assert generate_integers(1, 3) == []
        assert generate_integers(2, 3) == [2]

    def test_multiple_even_numbers(self):
        assert generate_integers(2, 6) == [2, 4, 6]

    def test_a_equals_b_even(self):
        assert generate_integers(2, 2) == [2]

    def test_a_equals_b_odd(self):
        assert generate_integers(1, 1) == []

    def test_edge_case_1(self):
        assert generate_integers(1, 3) == []

    def test_edge_case_2(self):
        assert generate_integers(2, 2) == [2]

    def test_large_range(self):
        assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]