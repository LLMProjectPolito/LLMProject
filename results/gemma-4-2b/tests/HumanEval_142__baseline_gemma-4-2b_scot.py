


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

# STEP 1: REASONING
# The function `sum_squares` takes a list of integers as input.
# It modifies the list by squaring elements at indices divisible by 3 and cubing elements at indices divisible by 4, but not divisible by 3.
# The function then calculates the sum of all elements in the modified list and returns the sum.
# We need to create a pytest suite to test various scenarios, including empty lists, lists with only multiples of 3, lists with only multiples of 4, lists with mixed multiples of 3 and 4, and lists with no multiples of 3 or 4.
# We need to test the edge cases like empty list and lists containing negative numbers.

# STEP 2: PLAN
# Test cases:
# 1. Empty list: [] - Expected sum is 0.
# 2. List with only multiples of 3: [3, 6, 9] - Expected sum is 27.
# 3. List with only multiples of 4: [4, 8, 12] - Expected sum is 288.
# 4. List with mixed multiples of 3 and 4: [1, 2, 3, 4, 5, 6] - Expected sum is 24.
# 5. List with no multiples of 3 or 4: [1, 2, 3, 4, 5, 6] - Expected sum is 21.
# 6. List with negative numbers: [-1, -5, 2, -1, -5] - Expected sum is -126.
# 7. List with zero: [0, 0, 0] - Expected sum is 0.
# 8. List with a mix of positive and negative numbers and multiples of 3 and 4: [1, 2, 3, 4, -5, 6] - Expected sum is 12.

# STEP 3: CODE
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
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num * num
        elif i % 4 == 0 and i % 3 != 0:
            result += num * num * num
        else:
            result += num
    return result

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3], 6),
        ([], 0),
        ([-1, -5, 2, -1, -5], -126),
        ([1, 2, 3, 4, 5, 6], 24),
        ([1, 2, 3, 4, 5, 6], 21),
        ([0, 0, 0], 0),
        ([1, 2, 3, 4, -5, 6], 12),
    ],
)
def test_sum_squares(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([3, 6, 9], 27),
        ([4, 8, 12], 288),
    ],
)
def test_multiples_of_3(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([4, 8, 12], 288),
    ],
)
def test_multiples_of_4(lst, expected):
    assert sum_squares(lst) == expected