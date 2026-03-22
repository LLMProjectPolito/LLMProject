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

    def test_start_at_zero(self):
        assert generate_integers(0, 4) == [0, 2, 4]

    def test_start_at_negative(self):
        with pytest.raises(TypeError):
            generate_integers(-2, 4)

    def test_end_at_negative(self):
        with pytest.raises(TypeError):
            generate_integers(2, -4)

    def test_large_numbers(self):
        assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

    def test_same_number(self):
        assert generate_integers(5, 5) == []

    def test_a_equals_b_even(self):
        assert generate_integers(4, 4) == [4]

    def test_a_equals_b_odd(self):
        assert generate_integers(5, 5) == []

    def test_a_and_b_are_zero(self):
        assert generate_integers(0, 0) == [0]

    def test_a_is_zero_b_is_positive(self):
        assert generate_integers(0, 6) == [0, 2, 4, 6]

    def test_a_is_positive_b_is_zero(self):
        with pytest.raises(TypeError):
            generate_integers(6, 0)