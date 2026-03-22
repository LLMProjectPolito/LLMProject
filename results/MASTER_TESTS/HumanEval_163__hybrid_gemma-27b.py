import pytest

def generate_integers(a, b):
    """
    Given two integers a and b, return the even digits between a
    and b, in ascending order.  Only single digit even numbers are returned.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

class TestGenerateIntegers:

    def test_basic_ascending(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_basic_descending(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_digits(self):
        assert generate_integers(10, 14) == []

    def test_single_digit_range(self):
        assert generate_integers(1, 1) == []
        assert generate_integers(2, 2) == [2]
        assert generate_integers(3, 3) == []

    def test_range_with_one_even(self):
        assert generate_integers(1, 2) == [2]
        assert generate_integers(2, 3) == [2]

    def test_range_with_multiple_even(self):
        assert generate_integers(1, 6) == [2, 4, 6]
        assert generate_integers(4, 9) == [4, 6, 8]

    def test_larger_range(self):
        assert generate_integers(1, 10) == [2, 4, 6, 8]
        assert generate_integers(5, 15) == [6, 8]

    def test_edge_cases(self):
        assert generate_integers(0, 1) == []
        assert generate_integers(0, 2) == [2]
        assert generate_integers(1, 0) == []
        assert generate_integers(2, 0) == [2]

    def test_negative_inputs(self):
        assert generate_integers(-2, -1) == []
        assert generate_integers(-1, 2) == [2]
        assert generate_integers(2, -1) == [2]

    def test_mixed_positive_negative(self):
        assert generate_integers(-5, 5) == [2, 4]

    def test_large_numbers(self):
        assert generate_integers(100, 105) == []
        assert generate_integers(101, 108) == [102, 104, 106, 108]

    def test_same_number(self):
        assert generate_integers(5, 5) == []
        assert generate_integers(6, 6) == [6]

    def test_empty_range(self):
        assert generate_integers(5, 4) == [4, 5]

    def test_zero_to_zero(self):
        assert generate_integers(0, 0) == []