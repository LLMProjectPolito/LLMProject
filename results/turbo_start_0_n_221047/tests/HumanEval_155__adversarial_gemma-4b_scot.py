import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num = abs(num)
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

STEP 1: REASONING -
The function `even_odd_count` takes an integer as input and returns a tuple containing the count of even and odd digits in the integer. The function handles negative numbers by taking the absolute value. The test cases should cover positive, negative, zero, single-digit, multi-digit, and edge cases. We need to test the core logic of counting even and odd digits.

STEP 2: PLAN -
Test functions:
1.  `test_positive_even_odd()`: Tests a positive number with both even and odd digits.
2.  `test_positive_only_even()`: Tests a positive number with only even digits.
3.  `test_positive_only_odd()`: Tests a positive number with only odd digits.
4.  `test_negative_even_odd()`: Tests a negative number with both even and odd digits.
5.  `test_negative_only_even()`: Tests a negative number with only even digits.
6.  `test_negative_only_odd()`: Tests a negative number with only odd digits.
7.  `test_zero()`: Tests the input as zero.
8.  `test_single_digit_even()`: Tests a single digit even number.
9.  `test_single_digit_odd()`: Tests a single digit odd number.

STEP 3: CODE -