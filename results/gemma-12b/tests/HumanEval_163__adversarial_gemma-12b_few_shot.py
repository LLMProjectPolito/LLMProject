
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
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

class TestGenerateIntegers:

    def test_basic(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_reverse_order(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        assert generate_integers(4, 4) == [4]

    def test_start_with_odd(self):
        assert generate_integers(3, 7) == [4, 6]

    def test_end_with_odd(self):
        assert generate_integers(3, 9) == [4, 6, 8]

    def test_a_equals_b_even(self):
        assert generate_integers(6, 6) == [6]

    def test_a_equals_b_odd(self):
        assert generate_integers(5, 5) == []

    def test_large_range(self):
        assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    def test_negative_input(self):
        with pytest.raises(TypeError):
            generate_integers(-2, 8)

    def test_non_integer_input(self):
        with pytest.raises(TypeError):
            generate_integers(2.5, 8)

    def test_mixed_input(self):
        with pytest.raises(TypeError):
            generate_integers(2, "8")