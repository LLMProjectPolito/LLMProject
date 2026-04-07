


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
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            sum += lst[i]**3
        else:
            sum += lst[i]
    return sum

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_multiple_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

    def test_multiple_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

    def test_multiple_of_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 81 + 10 + 11 + 144

    def test_neither_multiple(self):
        assert sum_squares([1, 2, 5, 7, 10]) == 25

    def test_negative_numbers(self):
        assert sum_squares([-1, -2, -3, -4, -5]) == 1 - 4 + 9 - 64 - 125

    def test_mixed_numbers(self):
        assert sum_squares([-1, 2, -3, 4, -5]) == 1 + 4 - 9 + 64 - 125

    def test_zero(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 4 + 9 + 16

    def test_large_list(self):
        lst = list(range(1, 21))
        expected_sum = sum(lst[i]**2 if i % 3 == 0 else lst[i]**3 if i % 4 == 0 and i % 3 != 0 else lst[i] for i in range(len(lst)))
        assert sum_squares(lst) == expected_sum

    def test_only_multiples_of_3(self):
        assert sum_squares([3, 6, 9, 12]) == 9 + 36 + 81 + 144

    def test_only_multiples_of_4(self):
        assert sum_squares([4, 8, 12, 16]) == 64 + 512 + 144 + 256

    def test_mixed_multiples_of_3_and_4(self):
        assert sum_squares([3, 4, 6, 8, 9, 12, 16]) == 9 + 64 + 36 + 512 + 81 + 144 + 256