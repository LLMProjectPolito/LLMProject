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

    def test_positive_numbers(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_negative_numbers(self):
        assert specialFilter([-11, -33, -55, -77, -99]) == 0

    def test_mixed_positive_and_negative(self):
        assert specialFilter([11, -33, 55, -77, 99]) == 1

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 5

    def test_numbers_less_than_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_zero_and_ten(self):
        assert specialFilter([0, 10, 20, 30]) == 0

    def test_large_numbers(self):
        assert specialFilter([111, 333, 555, 777, 999]) == 5

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([101, 303, 505, 707, 909]) == 0

    def test_single_digit_odd_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_mixed_cases(self):
        assert specialFilter([11, 33, 55, 77, 99, 10, 20, 30, 0]) == 5

    def test_all_numbers_same(self):
        assert specialFilter([33, 33, 33, 33, 33]) == 5

    def test_large_list(self):
        nums = list(range(1, 101))
        assert specialFilter(nums) == 25