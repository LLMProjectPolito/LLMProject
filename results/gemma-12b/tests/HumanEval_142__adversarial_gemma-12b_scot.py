


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
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            lst[i] = lst[i] ** 3
        total_sum += lst[i]
    return total_sum

class TestSumSquares:
    def test_empty_list(self):
        lst = []
        expected = 0
        assert sum_squares(lst) == expected

    def test_basic_list(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = (1**2) + 2 + (3**2) + (4**3) + 5 + (6**2) + 7 + (8**3) + 9 + (10**2)
        assert sum_squares(lst) == expected

    def test_list_with_multiples_of_3(self):
        lst = [1, 2, 3, 4, 5, 6]
        expected = (1**2) + 2 + (3**2) + 4 + 5 + (6**2)
        assert sum_squares(lst) == expected

    def test_list_with_multiples_of_4(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = 1 + 2 + 3 + (4**3) + 5 + 6 + 7 + (8**3)
        assert sum_squares(lst) == expected

    def test_list_with_multiples_of_both_3_and_4(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        expected = (1**2) + 2 + (3**2) + 4 + 5 + (6**2) + 7 + 8 + 9 + (10**2) + 11 + (12**2)
        assert sum_squares(lst) == expected

    def test_list_with_negative_numbers(self):
        lst = [-1, -5, 2, -1, -5]
        expected = (-1**2) + (-5) + 2 + (-1**2) + (-5**3)
        assert sum_squares(lst) == -126

    def test_list_with_mixed_numbers(self):
        lst = [-1, 5, -2, 1, -5]
        expected = (-1**2) + (5**3) + (-2) + 1 + (-5)
        assert sum_squares(lst) == 121

    def test_list_with_zero(self):
        lst = [0, 1, 2, 3, 4]
        expected = (0**2) + 1 + 2 + (3**2) + (4**3)
        assert sum_squares(lst) == 72

    def test_large_list(self):
        lst = list(range(1, 21))
        expected = sum(
            [x**2 if i % 3 == 0 else (x**3 if i % 4 == 0 and i % 3 != 0 else x)
             for i, x in enumerate(lst)]
        )
        assert sum_squares(lst) == expected

    def test_list_with_duplicate_indices(self):
        # This test is technically not needed given the problem description,
        # but included for completeness.  The function will process each index once.
        lst = [1, 2, 3, 4, 5]
        assert sum_squares(lst) == (1**2) + 2 + (3**2) + (4**3) + 5