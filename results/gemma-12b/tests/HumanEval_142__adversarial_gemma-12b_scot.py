


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
    total_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total_sum += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += num ** 3
        else:
            total_sum += num
    return total_sum

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_basic_list(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36  # 3 + 4^3 = 64

    def test_list_with_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == (-1)**2 + (-5)**2 + 2 + (-1)**2 + (-5)**2 == 1 + 25 + 2 + 1 + 25 == 54

    def test_list_with_mixed_numbers(self):
        assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + (-2)**2 + 3 + (-4)**3 + 5 + (-6)**2 == 1 + 4 + 3 + -64 + 5 + 36 == -15

    def test_list_with_multiples_of_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 9 + 100 + 11 + 144 == 889

    def test_list_with_only_multiples_of_3(self):
        assert sum_squares([3, 6, 9, 12]) == 9 + 36 + 81 + 144 == 270

    def test_list_with_only_multiples_of_4(self):
        assert sum_squares([4, 8, 12, 16]) == 16 + 512 + 144 + 4096 == 4672

    def test_list_with_no_multiples_of_3_or_4(self):
        assert sum_squares([1, 2, 5, 7, 10]) == 1 + 2 + 5 + 7 + 10 == 25

    def test_large_list(self):
        large_list = list(range(1, 21))
        expected_sum = sum(sum_squares([x]) for x in large_list)
        assert sum_squares(large_list) == expected_sum