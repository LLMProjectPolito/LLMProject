
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
    generate_integers(10, 14) => [10, 12, 14]
    """
    start = max(a, b)
    end = min(a, b)
    even_numbers = []
    for i in range(start, end + 1):
        if i > 0 and i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

class TestGenerateIntegers:

    def test_basic_case(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_reverse_order(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == [10, 12, 14]

    def test_single_number(self):
        assert generate_integers(4, 4) == [4]

    def test_large_numbers(self):
        assert generate_integers(100, 106) == [100, 102, 104, 106]

    def test_negative_numbers(self):
        assert generate_integers(-2, 8) == [2, 4, 6, 8]

    def test_float_numbers(self):
        with pytest.raises(TypeError):
            generate_integers(2.5, 8)

    def test_a_greater_than_b(self):
        assert generate_integers(10, 5) == [10, 8, 6, 4, 2]

    def test_a_equals_b(self):
        assert generate_integers(2, 2) == [2]

    def test_empty_range(self):
        assert generate_integers(1, 0) == []

    def test_large_range(self):
        assert generate_integers(1000, 1010) == [1000, 1002, 1004, 1006, 1008, 1010]