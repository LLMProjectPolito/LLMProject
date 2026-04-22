


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
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
        else:
            total += num
    return total

class TestSumSquares:

    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_simple_list(self):
        assert sum_squares([1, 2, 3]) == 1 + 4 + 3

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_numbers(self):
        assert sum_squares([1, -2, 3, -4, 5]) == 1 + 4 + 9 + (-64) + 5

    def test_only_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 5 + 36

    def test_only_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 8]) == 1 + 2 + 3 + 16 + 5 + 6 + 512

    def test_zero_in_list(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 4 + 9 + 0

    def test_large_numbers(self):
        assert sum_squares([100, 200, 300, 400]) == 100 + 40000 + 90000 + 16000000

    def test_alternating_multiples(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1 + 4 + 9 + 16 + 5 + 36 + 7 + 64 + 81

    def test_all_same_number(self):
        assert sum_squares([5, 5, 5, 5, 5]) == 5 + 125 + 5 + 125 + 5

    def test_complex_list(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 4 + 9 + 16 + 5 + 36 + 7 + 64 + 81 + 100 + 11 + 144

    def test_list_with_only_multiples_of_4_and_3(self):
      assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 20, 24]) == 1 + 4 + 9 + 16 + 5 + 36 + 7 + 64 + 81 + 100 + 11 + 144 + 256 + 400 + 576