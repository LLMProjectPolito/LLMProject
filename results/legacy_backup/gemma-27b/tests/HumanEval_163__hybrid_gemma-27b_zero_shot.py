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
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

class TestGenerateIntegers:
    def test_basic_case(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_reversed_input(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_digits(self):
        assert generate_integers(10, 14) == []

    def test_single_digit_range(self):
        assert generate_integers(1, 1) == []
        assert generate_integers(2, 2) == [2]

    def test_range_with_one_even(self):
        assert generate_integers(1, 3) == [2]
        assert generate_integers(3, 5) == [4]

    def test_range_with_multiple_even(self):
        assert generate_integers(1, 6) == [2, 4, 6]
        assert generate_integers(5, 9) == [6, 8]

    def test_edge_cases(self):
        assert generate_integers(0, 1) == []
        assert generate_integers(0, 2) == [2]
        assert generate_integers(1, 0) == []
        assert generate_integers(2, 0) == [2]

    def test_larger_range(self):
        assert generate_integers(1, 10) == [2, 4, 6, 8]
        assert generate_integers(11, 19) == []

    def test_negative_inputs(self):
        assert generate_integers(-2, -1) == []
        assert generate_integers(-1, 2) == [2]
        assert generate_integers(-2, 2) == [2]

    def test_mixed_inputs(self):
        assert generate_integers(-1, 1) == []
        assert generate_integers(-1, 3) == [2]

    def test_empty_range(self):
        assert generate_integers(5, 5) == []

    def test_large_numbers(self):
        assert generate_integers(100, 101) == []
        assert generate_integers(101, 102) == []
        assert generate_integers(102, 104) == []

    def test_zero_in_range(self):
        assert generate_integers(0, 3) == [2]
        assert generate_integers(2, 0) == [2]

    def test_generate_integers_ascending(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_generate_integers_descending(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_generate_integers_no_even_digits(self):
        assert generate_integers(10, 14) == []

    def test_generate_integers_single_digit_range(self):
        assert generate_integers(1, 3) == [2]

    def test_generate_integers_same_number(self):
        assert generate_integers(4, 4) == [4]

    def test_generate_integers_start_odd(self):
        assert generate_integers(1, 5) == [2, 4]

    def test_generate_integers_end_odd(self):
        assert generate_integers(3, 7) == [4, 6]

    def test_generate_integers_large_range(self):
        assert generate_integers(1, 9) == [2, 4, 6, 8]

    def test_generate_integers_zero_to_one(self):
        assert generate_integers(0, 1) == []

    def test_generate_integers_zero_to_two(self):
        assert generate_integers(0, 2) == [2]

    def test_generate_integers_edge_case_1(self):
        assert generate_integers(9, 10) == []

    def test_generate_integers_edge_case_2(self):
        assert generate_integers(0, 0) == []

    def test_generate_integers_negative_inputs(self):
        with pytest.raises(TypeError):
            generate_integers(-2, 4)

    def test_generate_integers_float_inputs(self):
        with pytest.raises(TypeError):
            generate_integers(2.5, 4)

    def test_generate_integers_string_inputs(self):
        with pytest.raises(TypeError):
            generate_integers("2", "4")

    def test_generate_integers_empty_range(self):
        assert generate_integers(5, 1) == [2, 4]