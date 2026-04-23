
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

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
        assert specialFilter([-73]) == 1
        assert specialFilter([109]) == 1

    def test_multiple_special_numbers(self):
        assert specialFilter([15, -73, 14, -15]) == 1
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_mixed_numbers(self):
        assert specialFilter([12, 35, 57, 78, 91]) == 2
        assert specialFilter([21, 43, 65, 87, 101]) == 2

    def test_negative_numbers(self):
        assert specialFilter([-13, -35, -57, -79, -91]) == 5
        assert specialFilter([-12, -34, -56, -78, -90]) == 0
        assert specialFilter([-15, -33, -51, -79, -97]) == 5

    def test_large_numbers(self):
        assert specialFilter([100001, 123455, 987659]) == 2
        assert specialFilter([200002, 456788, 876540]) == 0

    def test_numbers_close_to_10(self):
        assert specialFilter([11, 13, 15, 17, 19]) == 5
        assert specialFilter([9, 10, 11, 12, 13]) == 2

    def test_zero_and_negative_numbers(self):
        assert specialFilter([0, -1, -11, -13, -15]) == 1
        assert specialFilter([0, 11, 12, 13, 14]) == 2

    def test_edge_case_11(self):
        assert specialFilter([11]) == 1

    def test_edge_case_99(self):
        assert specialFilter([99]) == 1

    def test_edge_case_10(self):
        assert specialFilter([10]) == 0

    def test_all_even_digits(self):
        assert specialFilter([22, 44, 66, 88]) == 0

    def test_mixed_positive_negative(self):
        assert specialFilter([15, -33, 57, -79, 91, -11]) == 5

    @pytest.mark.parametrize("nums, expected", [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([], 0),
        ([2, 4, 6, 8, 10], 0),
        ([11, 33, 55, 77, 99], 5),
        ([-13, -35, -57, -79, -91], 5),
        ([100001, 123455, 987659], 2),
        ([11, 13, 15, 17, 19], 5),
        ([0, -1, -11, -13, -15], 1),
        ([11], 1),
        ([99], 1),
        ([10], 0),
        ([22, 44, 66, 88], 0),
        ([15, -33, 57, -79, 91, -11], 5)
    ])
    def test_parameterized(self, nums, expected):
        assert specialFilter(nums) == expected

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
        assert specialFilter([101, 123, 155, 177, 199]) == 5

    def test_numbers_with_even_digits(self):
        assert specialFilter([12, 34, 56, 78, 90]) == 0

    def test_numbers_close_to_10(self):
        assert specialFilter([11, 13, 99, 101]) == 3

    def test_mixed_positive_and_negative(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_zero(self):
        assert specialFilter([0]) == 0

    def test_one_digit_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_two_digit_numbers(self):
        assert specialFilter([11, 12, 13, 14, 15]) == 2

    def test_edge_case_11(self):
        assert specialFilter([11]) == 1

    def test_edge_case_99(self):
        assert specialFilter([99]) == 1

    def test_edge_case_10(self):
        assert specialFilter([10]) == 0

    def test_large_list(self):
        nums = [i for i in range(1, 101)]
        assert specialFilter(nums) == 5

    def test_all_negative(self):
        assert specialFilter([-11, -13, -15, -17, -19, -20]) == 5