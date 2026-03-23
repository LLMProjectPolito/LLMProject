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
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

class TestGenerateIntegers:
    def test_basic_case(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_a_greater_than_b(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_a_and_b_same_even(self):
        assert generate_integers(4, 4) == [4]

    def test_a_and_b_same_odd(self):
        assert generate_integers(5, 5) == []

    def test_a_even_b_odd(self):
        assert generate_integers(2, 5) == [2, 4]

    def test_a_odd_b_even(self):
        assert generate_integers(3, 6) == [4, 6]

    def test_a_equals_1_b_equals_1(self):
        assert generate_integers(1, 1) == []

    def test_a_equals_1_b_equals_2(self):
        assert generate_integers(1, 2) == [2]

    def test_a_equals_2_b_equals_1(self):
        assert generate_integers(2, 1) == [2]