
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
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")

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

    def test_reverse_order(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_empty_range(self):
        assert generate_integers(5, 1) == []

    def test_single_even_number(self):
        assert generate_integers(4, 4) == [4]

    def test_start_at_zero(self):
        assert generate_integers(0, 4) == [0, 2, 4]

    def test_zero_handling(self):
        assert generate_integers(0, 0) == [0]
        assert generate_integers(0, 6) == [0, 2, 4, 6]
        assert generate_integers(6, 0) == [0, 2, 4, 6]

    def test_negative_inputs(self):
        with pytest.raises(TypeError):
            generate_integers(-2, 4)
        with pytest.raises(TypeError):
            generate_integers(2, -4)
        with pytest.raises(TypeError):
            generate_integers(-2, -4)

    def test_large_numbers(self):
        assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

    def test_very_large_range(self):
        assert generate_integers(1000, 1020) == [1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018, 1020]

    def test_same_number_odd(self):
        assert generate_integers(1, 1) == []

    def test_a_equals_b_even(self):
        assert generate_integers(2, 2) == [2]

    def test_a_is_even_b_is_odd(self):
        assert generate_integers(2, 3) == [2]

    def test_float_input_a(self):
        with pytest.raises(TypeError):
            generate_integers(2.5, 4)

    def test_float_input_b(self):
        with pytest.raises(TypeError):
            generate_integers(2, 4.5)

    def test_string_input(self):
        with pytest.raises(TypeError):
            generate_integers("a", 2)