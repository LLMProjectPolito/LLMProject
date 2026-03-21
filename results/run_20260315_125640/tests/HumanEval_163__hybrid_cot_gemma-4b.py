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
    result = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if not result or int(digit) != result[-1]:
                    result.append(int(digit))
    result.sort()
    return result

class TestGenerateIntegers:
    def test_empty_range(self):
        assert generate_integers(5, 2) == []

    def test_identical_numbers(self):
        assert generate_integers(5, 5) == []

    def test_single_digit_range_even(self):
        assert generate_integers(2, 2) == [2]

    def test_single_digit_range_odd(self):
        assert generate_integers(1, 3) == []

    def test_range_no_even_digits(self):
        assert generate_integers(1, 3) == []
        assert generate_integers(3, 5) == []

    def test_range_only_even_digits(self):
        assert generate_integers(2, 4) == [2, 4]
        assert generate_integers(8, 10) == [8, 10]

    def test_range_mixed_even_odd(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]
        assert generate_integers(10, 14) == []
        assert generate_integers(1, 9) == [2, 4, 6, 8]
        assert generate_integers(4, 6) == [4, 6]
        assert generate_integers(12, 15) == [12, 14]

    def test_large_numbers(self):
        assert generate_integers(100, 102) == [100, 102]
        assert generate_integers(200, 205) == [200, 202, 204]

    def test_zero_input(self):
        assert generate_integers(0, 5) == [0, 2, 4]

    def test_negative_input(self):
        assert generate_integers(-5, 5) == [0, 2, 4]