


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

    def test_example_1(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_example_2(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_list_with_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1**2 + 2 + 3**2 + 4 + 5 + 6 == 1 + 2 + 9 + 4 + 5 + 6 == 27

    def test_list_with_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 4**3 + 5 + 6 + 7 + 8 == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 8 == 96

    def test_list_with_multiples_of_both_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1**2 + 2 + 3 + 4**3 + 5 + 6**2 + 7 + 8 + 9**2 + 10 + 11 + 12 == 1 + 2 + 3 + 64 + 5 + 36 + 7 + 8 + 81 + 10 + 11 + 12 == 230

    def test_list_with_negative_numbers(self):
        assert sum_squares([-1, -2, -3, -4, -5]) == (-1)**2 + (-2) + (-3)**2 + (-4)**3 + (-5) == 1 - 2 + 9 - 64 - 5 == -61

    def test_list_with_zeros(self):
        assert sum_squares([0, 0, 0, 0, 0]) == 0

    def test_list_with_mixed_numbers(self):
        assert sum_squares([1, -2, 3, -4, 5, -6]) == 1**2 + (-2) + 3**2 + (-4)**3 + 5 + (-6)**2 == 1 - 2 + 9 - 64 + 5 + 36 == -15

    def test_large_list(self):
        lst = list(range(1, 21))
        expected_sum = 0
        for i, num in enumerate(lst):
            if i % 3 == 0:
                expected_sum += num ** 2
            elif i % 4 == 0 and i % 3 != 0:
                expected_sum += num ** 3
            else:
                expected_sum += num
        assert sum_squares(lst) == expected_sum