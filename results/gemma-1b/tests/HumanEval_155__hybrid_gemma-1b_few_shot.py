
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

```python
import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def merge_suites():
    """Merges the two pytest suites into a single suite."""

    # Combine the tests from both suites
    combined_tests = [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    # Combine the tests from the first suite
    combined_tests.extend(get_max([1, 2, 3]))
    combined_tests.extend(even_odd_count(-12))

    # Combine the tests from the second suite
    combined_tests.extend(get_max([1, 2, 3]))
    combined_tests.extend(even_odd_count(123))

    return combined_tests

# Run the merged suite
merged_suite = merge_suites()

# Run the tests
def test_merged_suite():
    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        get_max([1, 2, 3]),
        even_odd_count(-12),
        get_max([1, 2, 3])
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        get_max([1, 2, 3]),
        even_odd_count(-12),
        get_max([1, 2, 3])
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome('')
    ]

    assert merged_suite == [
        is_palindrome('radar'),
        is_palindrome('hello'),
        is_palindrome