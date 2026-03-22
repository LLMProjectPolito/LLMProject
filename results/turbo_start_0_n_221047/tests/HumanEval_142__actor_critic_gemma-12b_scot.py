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

    def test_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 4 + 25 + 36

    def test_multiples_of_4_not_3(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_sum = 1 + 2 + 3 + 64 + 5 + 6 + 7 + 8
        assert sum_squares(lst) == expected_sum

    def test_mixed_indices(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        expected_sum = (1**2) + 2 + (3**2) + (4**3) + 5 + (6**2) + 7 + (8**3) + (9**2) + 10 + (12**2)
        assert sum_squares(lst) == expected_sum

    def test_no_multiples(self):
        assert sum_squares([1, 2, 5, 7, 10]) == 1 + 2 + 5 + 7 + 10

    def test_negative_numbers(self):
        assert sum_squares([-1, -2, -3, -4, -5]) == (-1)**2 + (-2) + (-3)**2 + (-4)**3 + (-5)
        assert sum_squares([-1,-5,2,-1,-5]) == -126

    def test_zero(self):
        assert sum_squares([0, 1, 2, 3, 4]) == (0**2) + 1 + 2 + (3**2) + (4**3)

    def test_large_list(self):
        lst = list(range(1, 21))
        expected_sum = 0
        for i in range(len(lst)):
            if i % 3 == 0:
                expected_sum += lst[i]**2
            elif i % 4 == 0 and i % 3 != 0:
                expected_sum += lst[i]**3
            else:
                expected_sum += lst[i]
        assert sum_squares(lst) == expected_sum

    def test_index_0_both_multiples(self):
        assert sum_squares([1, 2, 3, 4, 12]) == 1 + 2 + 3 + 64 + 144