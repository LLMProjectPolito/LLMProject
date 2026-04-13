
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

# STEP 1: REASONING
# The function `generate_integers(a, b)` aims to return a list of even integers between two given integers 'a' and 'b', sorted in ascending order.
# The function should handle cases where a > b, and cases where there are no even numbers between a and b.
# The function should only return even numbers.
# The function should return an empty list if no even numbers are found.

# STEP 2: PLAN
# Test functions:
# - test_ascending_order: Checks if the returned list is in ascending order when a < b.
# - test_descending_order: Checks if the returned list is in ascending order when a > b.
# - test_no_even_numbers: Checks if an empty list is returned when there are no even numbers between a and b.
# - test_single_even_number: Checks if a list containing a single even number is returned when there is only one even number between a and b.
# - test_multiple_even_numbers: Checks if a list containing multiple even numbers is returned when there are multiple even numbers between a and b.
# - test_a_is_even: Checks if the function correctly includes 'a' when 'a' is even.
# - test_b_is_even: Checks if the function correctly includes 'b' when 'b' is even.
# - test_a_and_b_are_even: Checks if the function correctly includes both 'a' and 'b' when both are even.
# - test_negative_input: Checks if the function handles negative inputs gracefully (although the prompt specifies positive integers, it's good to check).

# STEP 3: CODE
import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

class TestGenerateIntegers:
    def test_ascending_order(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_descending_order(self):
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        assert generate_integers(2, 3) == [2]

    def test_multiple_even_numbers(self):
        assert generate_integers(4, 10) == [4, 6, 8, 10]

    def test_a_is_even(self):
        assert generate_integers(4, 8) == [4, 6, 8]

    def test_b_is_even(self):
        assert generate_integers(2, 6) == [2, 4, 6]

    def test_a_and_b_are_even(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_negative_input(self):
        assert generate_integers(-2, 2) == [0, 2]