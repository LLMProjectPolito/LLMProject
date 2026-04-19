


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

def test_sum_squares_provided_examples():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    # Index 0 is a multiple of 3 (0 % 3 == 0), so it should be squared
    assert sum_squares([5]) == 25
    assert sum_squares([-2]) == 4

def test_sum_squares_multiple_of_3():
    # Index 0: 2^2 = 4
    # Index 1: 1
    # Index 2: 1
    # Index 3: 2^2 = 4
    # Sum: 4 + 1 + 1 + 4 = 10
    assert sum_squares([2, 1, 1, 2]) == 10

def test_sum_squares_multiple_of_4():
    # Index 0: 2^2 = 4 (multiple of 3)
    # Index 1: 1
    # Index 2: 1
    # Index 3: 1^2 = 1 (multiple of 3)
    # Index 4: 2^3 = 8 (multiple of 4, not 3)
    # Sum: 4 + 1 + 1 + 1 + 8 = 15
    assert sum_squares([2, 1, 1, 1, 2]) == 15

def test_sum_squares_both_3_and_4():
    # Index 12 is a multiple of both 3 and 4.
    # According to rules: square if multiple of 3. 
    # Cube only if multiple of 4 AND NOT multiple of 3.
    # Therefore, index 12 must be squared.
    lst = [0] * 13
    lst[12] = 3
    # Index 0: 0^2 = 0
    # Index 3: 0^2 = 0
    # Index 4: 0^3 = 0
    # Index 6: 0^2 = 0
    # Index 8: 0^3 = 0
    # Index 9: 0^2 = 0
    # Index 12: 3^2 = 9
    assert sum_squares(lst) == 9

def test_sum_squares_no_multiples():
    # Indices 1, 2, 5 are not multiples of 3 or 4
    # We use a slice or specific indices to ensure we only hit non-multiples
    # However, index 0 is always a multiple of 3.
    # Let's test a list where only indices 1 and 2 have values.
    assert sum_squares([0, 10, 20]) == 30 # 0^2 + 10 + 20