
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
    if a < 0 or b < 0:
        raise TypeError("Inputs must be positive integers.")

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

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        assert generate_integers(2, 2) == [2]

    def test_adjacent_even_numbers(self):
        assert generate_integers(4, 6) == [4, 6]

    def test_start_at_zero(self):
        assert generate_integers(0, 4) == [0, 2, 4]

    def test_zero_as_second_argument(self):
        assert generate_integers(2, 0) == [0, 2]

    @pytest.mark.parametrize("input_type", [float, str, list, dict])
    def test_invalid_input_type(self, input_type):
        with pytest.raises(TypeError):
            generate_integers(2, input_type("4"))

    def test_large_numbers(self):
        assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

    @pytest.mark.parametrize("a, b, expected", [
        (4, 4, [4]),
        (5, 5, [])
    ])
    def test_same_number(self, a, b, expected):
        assert generate_integers(a, b) == expected

    def test_same_odd_number(self):
        assert generate_integers(5, 5) == []

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, [2]),
        (3, 4, [4])
    ])
    def test_one_even_one_odd(self, a, b, expected):
        assert generate_integers(a, b) == expected