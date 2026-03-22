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
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_matching_numbers(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_example_1(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_example_2(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_positive_and_negative_numbers(self):
        assert specialFilter([15, -73, 14, -15, 35, -91]) == 3

    def test_numbers_with_multiple_digits(self):
        assert specialFilter([123, 357, 519, 735, 911]) == 5

    def test_numbers_with_zero(self):
        assert specialFilter([10, 30, 50, 70, 90]) == 0

    def test_mixed_numbers(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 15

    def test_large_numbers(self):
        assert specialFilter([111, 333, 555, 777, 999, 1000, 2000]) == 5

    def test_negative_large_numbers(self):
        assert specialFilter([-111, -333, -555, -777, -999]) == 5

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 12, 13, 14, 15]) == 1

    def test_numbers_less_than_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_edge_case_1(self):
        assert specialFilter([11, 111, 1111, 11111]) == 4

    def test_edge_case_2(self):
        assert specialFilter([33, 333, 3333, 33333]) == 4