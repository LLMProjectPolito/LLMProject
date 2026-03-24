


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

import pytest

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total += num ** 3
        else:
            total += num
    return total

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_basic_list(self):
        assert sum_squares([1, 2, 3]) == 14

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_numbers(self):
        assert sum_squares([1, -2, 3, -4, 5, -6]) == -11

    def test_list_with_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 46

    def test_list_with_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 530

    def test_list_with_multiples_of_both_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 426

    def test_list_with_zero(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 30

    def test_large_list(self):
        large_list = list(range(1, 21))
        expected_sum = 0
        for i, num in enumerate(large_list):
            if (i + 1) % 3 == 0:
                expected_sum += num**2
            elif (i + 1) % 4 == 0:
                expected_sum += num**3
            else:
                expected_sum += num
        assert sum_squares(large_list) == expected_sum

    def test_list_with_floats(self):
        assert sum_squares([1.0, 2.0, 3.0]) == 14.0

    def test_list_with_repeated_numbers(self):
        assert sum_squares([2, 2, 2, 2]) == 4 + 4 + 4 + 64

    def test_list_with_one_element(self):
        assert sum_squares([5]) == 5

    def test_list_with_one_element_multiple_of_3(self):
        assert sum_squares([3]) == 9

    def test_list_with_one_element_multiple_of_4(self):
        assert sum_squares([4]) == 64

    def test_list_with_multiple_of_both_3_and_4(self):
        assert sum_squares([12]) == 144

    def test_list_with_negative_and_positive(self):
        assert sum_squares([-2, 3, -4, 5]) == -2 + 9 - 64 + 5