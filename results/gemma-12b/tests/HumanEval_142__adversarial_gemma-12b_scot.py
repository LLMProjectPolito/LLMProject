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
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 56

    def test_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 126

    def test_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 172

    def test_multiples_of_both(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 172

    def test_no_multiples(self):
        assert sum_squares([1, 2, 5, 7, 11]) == 26

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_numbers(self):
        assert sum_squares([-1, 5, 2, -4, 0]) == 10

    def test_large_list(self):
        large_list = list(range(1, 21))
        assert sum_squares(large_list) == 616

    def test_list_with_zeros(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 10