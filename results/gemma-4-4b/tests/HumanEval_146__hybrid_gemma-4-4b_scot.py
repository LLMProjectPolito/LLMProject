
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

# STEP 1: REASONING
# The problem asks to merge two pytest suites that both define the same function 'specialFilter'.
# The function takes a list of numbers as input and returns the count of numbers greater than 10 where both the first and last digits (when considering the absolute value) are odd.
# The core logic of the function is identical in both suites. Therefore, we can simply combine the test functions from both suites into a single suite.
# We need to ensure that the combined suite covers all the test cases present in both original suites.

# STEP 2: PLAN
# The plan is to combine the test functions from both suites into a single pytest suite.
# The test functions will be named in a way that clearly indicates the test case being covered.
# We will include the example test cases provided in the problem description.
# We will also add some additional test cases to ensure the function works correctly for various inputs, including edge cases (e.g., empty list, list with only numbers <= 10).

# Test cases:
# 1. Basic cases from the problem description:
#    - specialFilter([15, -73, 14, -15]) == 1
#    - specialFilter([33, -2, -3, 45, 21, 109]) == 2
# 2. Empty list: specialFilter([]) == 0
# 3. List with only numbers <= 10: specialFilter([1, 2, 3, 4, 5]) == 0
# 4. List with numbers greater than 10 but first/last digit not odd: specialFilter([22, 44, 66]) == 0
# 5. List with numbers greater than 10 and first/last digit odd: specialFilter([11, 33, 55, 77, 99]) == 5
# 6. List with mixed numbers: specialFilter([15, 22, 33, 44, 55, 66, 77, 88, 99]) == 5

# STEP 3: CODE
import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([], 0),
        ([1, 2, 3, 4, 5], 0),
        ([22, 44, 66], 0),
        ([11, 33, 55, 77, 99], 5),
        ([15, 22, 33, 44, 55, 66, 77, 88, 99], 5),
        ([-15, -33, -55, -77, -99], 5),
        ([1, 11, 111, 1111], 0),
        ([13, 31, 133, 313], 4),
    ],
)
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected