import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_special_numbers(self):
        assert specialFilter([2, 4, 6, 8, 10]) == 0

    def test_single_special_number(self):
        assert specialFilter([15]) == 1

    def test_multiple_special_numbers(self):
        assert specialFilter([15, 33, 57, 79, 91]) == 5

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_negative_numbers(self):
        assert specialFilter([-11, -13, -15, -17, -19]) == 5

    def test_large_numbers(self):
        assert specialFilter([1001, 12345, 98765, 11111]) == 2

    def test_numbers_close_to_10(self):
        assert specialFilter([11, 13, 99, 101]) == 3

    def test_numbers_with_even_digits(self):
        assert specialFilter([12, 14, 16, 18, 21]) == 0

    def test_numbers_with_zero(self):
        assert specialFilter([10, 20, 30, 110, 101]) == 1

    def test_example_1(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_example_2(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_all_negative(self):
        assert specialFilter([-11, -13, -15, -2, -4]) == 3

    def test_mixed_positive_negative(self):
        assert specialFilter([11, -13, 15, -17, 21, -23]) == 4

    def test_edge_case_11(self):
        assert specialFilter([11]) == 1

    def test_edge_case_99(self):
        assert specialFilter([99]) == 1

    def test_large_negative_number(self):
        assert specialFilter([-123456789]) == 0

    def test_large_positive_number(self):
        assert specialFilter([123456789]) == 0

    def test_numbers_with_leading_zeros_string(self):
        assert specialFilter([101, 111, 131, 151]) == 4

    def test_zero_and_positive(self):
        assert specialFilter([0, 11, 13, 15]) == 3

    def test_large_negative_number_2(self):
        assert specialFilter([-12345]) == 0

    def test_large_positive_number_2(self):
        assert specialFilter([12345]) == 0

    def test_edge_case_10(self):
        assert specialFilter([10]) == 0

    def test_edge_case_100(self):
        assert specialFilter([100]) == 0