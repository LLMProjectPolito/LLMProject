
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
    def test_ascending_order(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_descending_order(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        assert generate_integers(2, 2) == [2]

    def test_start_and_end_even(self):
        assert generate_integers(4, 8) == [4, 6, 8]

    def test_start_odd_end_even(self):
        assert generate_integers(1, 6) == [2, 4, 6]

    def test_start_even_end_odd(self):
        assert generate_integers(6, 7) == [6]

    def test_large_range(self):
        assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    def test_same_number_odd(self):
        assert generate_integers(1, 1) == []

    def test_same_number_even(self):
        assert generate_integers(2, 2) == [2]

    def test_negative_input_raises_error(self):
        with pytest.raises(TypeError):
            generate_integers(-2, 8)

    def test_non_integer_input_raises_error(self):
        with pytest.raises(TypeError):
            generate_integers(2.5, 8)

    def test_mixed_input_raises_error(self):
        with pytest.raises(TypeError):
            generate_integers(2, 8.5)