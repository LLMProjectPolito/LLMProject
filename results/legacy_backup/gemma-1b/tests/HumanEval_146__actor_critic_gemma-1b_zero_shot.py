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
    assert pytest.number(0)

def test_single_element():
    assert pytest.number(1)

def test_example_1():
    assert pytest.number(1)

def test_example_2():
    assert pytest.number(2)

def test_example_3():
    assert pytest.number(1)

def test_example_4():
    assert pytest.number(1)

def test_example_5():
    assert pytest.number(1)

def test_example_6():
    assert pytest.number(1)

def test_example_7():
    assert pytest.number(1)

def test_example_8():
    assert pytest.number(1)

def test_example_9():
    assert pytest.number(1)

def test_example_10():
    assert pytest.number(1)

def test_example_11():
    assert pytest.number(1)

def test_example_12():
    assert pytest.number(1)

def test_example_13():
    assert pytest.number(1)

def test_example_14():
    assert pytest.number(1)

def test_example_15():
    assert pytest.number(1)

def test_example_16():
    assert pytest.number(1)

def test_example_17():
    assert pytest.number(1)

def test_example_18():
    assert pytest.number(1)

def test_example_19():
    assert pytest.number(1)

def test_example_20():
    assert pytest.number(1)