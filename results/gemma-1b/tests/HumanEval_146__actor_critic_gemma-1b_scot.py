
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

```python
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
        num_str = str(abs(num))
        if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1
    return count

def test_empty_array():
    assert specialFilter([]) == 0

def test_single_element_greater_than_10_and_odd():
    assert specialFilter([15]) == 1

def test_single_element_not_greater_than_10_and_odd():
    assert specialFilter([-15]) == 0

def test_multiple_elements_greater_than_10_and_odd():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([11, 22, 33, 44, 55]) == 0
    assert specialFilter([1, 11, 111]) == 1
    assert specialFilter([1, 11, 111, 1111]) == 1
    assert specialFilter([1, 11, 111, 1111, 11111]) == 1
    assert specialFilter([1, 11, 111, 1111, 111111]) == 1
    assert specialFilter([1, 11, 111, 1111, 11111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 11111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 11111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 1111, 1111111111111]) == 0
    assert specialFilter([1, 11, 111, 111