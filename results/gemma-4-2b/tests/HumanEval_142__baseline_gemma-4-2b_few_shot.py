


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
            total += num * num
        elif i % 4 == 0 and i % 3 != 0:
            total += num * num * num
        else:
            total += num
    return total

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple():
    assert sum_squares([1, 2, 3, 4]) == 1 + 4 + 27 == 32

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 - 5 + 2 - 1 - 5 == -10

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 4 + 27 + 16 + 25 + 36 + 49 + 64 == 242

def test_sum_squares_all_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 9 + 3^3 + 9^3 == 9 + 27 + 729 == 765

def test_sum_squares_all_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 4^2 + 8^2 + 12^2 == 16 + 64 + 144 == 224