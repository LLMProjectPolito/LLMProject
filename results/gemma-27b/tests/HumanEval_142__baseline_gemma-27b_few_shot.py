


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

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 140

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 35

def test_sum_squares_large_list():
    lst = list(range(20))
    expected_sum = sum(lst)
    for i in range(len(lst)):
        if i % 3 == 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**3
    assert sum_squares(lst) == expected_sum

def test_sum_squares_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 3**2 + 6**2 + 9**2

def test_sum_squares_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 4**3 + 8**3 + 12**3