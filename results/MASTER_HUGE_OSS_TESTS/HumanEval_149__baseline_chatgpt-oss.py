import copy
import pytest

# The implementation is expected to be in a module that lives in the same
# directory as this test file.  Adjust the import statement if the module
# name is different (e.g. `from my_solution import sorted_list_sum`).
from sorted_list_sum import sorted_list_sum


@pytest.mark.parametrize(
    "input_list, expected",
    [
        # Basic examples from the doc‑string
        (["aa", "a", "aaa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        # Empty input → empty output
        ([], []),
        # All strings have odd length → empty output
        (["a", "abc", "xyz"], []),
        # All strings have even length, already sorted
        (["aa", "bb", "cccc"], ["aa", "bb", "cccc"]),
        # Mixed lengths, need sorting by length then alphabetically
        (["zzzz", "aa", "bbbb", "c", "dd"], ["aa", "dd", "bbbb", "zzzz"]),
        # Duplicates should be kept and sorted
        (["ab", "ab", "cd", "cd", "ef"], ["ab", "ab", "cd", "cd", "ef"]),
        # Same length strings – alphabetical order matters
        (["dog", "cat", "bat", "ant"], ["ant", "bat", "cat", "dog"]),
        # Case‑sensitivity: uppercase letters come before lowercase in ASCII
        (["Apple", "banana", "Cherry", "date"], ["Apple", "Cherry", "banana", "date"]),
        # Long list to check stability of sorting
        (
            ["zz", "aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii"],
            ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "zz"],
        ),
    ],
)
def test_sorted_list_sum_various_cases(input_list, expected):
    """
    Verify that `sorted_list_sum` returns the correct list for a variety of
    inputs, handling removal of odd‑length strings, sorting by length,
    alphabetical tie‑breaks, duplicates, and case sensitivity.
    """
    # Keep a copy to ensure the function does not mutate the original list
    original_copy = copy.deepcopy(input_list)

    result = sorted_list_sum(input_list)

    assert result == expected, f"Expected {expected}, got {result}"
    # The original list must stay unchanged
    assert input_list == original_copy, "Function mutated the input list"


def test_no_side_effects_on_nested_lists():
    """
    The function should treat the list as a flat collection of strings.
    Passing a list that contains the same string object multiple times must
    not cause accidental in‑place modifications of those objects.
    """
    s = "even"
    input_list = [s, s, "odd", "oddodd"]
    expected = ["even", "even", "oddodd"]  # "odd" (len 3) is removed

    result = sorted_list_sum(input_list)

    # Ensure the returned list contains the original string objects (identity)
    assert result[0] is s and result[1] is s
    assert result == expected


def test_large_input_performance():
    """
    Generate a relatively large list (10 000 elements) containing a mix of
    even‑ and odd‑length strings.  The test checks that the function returns
    the correct number of elements and finishes quickly (under 1 second).
    """
    import time

    # Build the list: even‑length strings are "ab", odd‑length strings are "a"
    large_input = ["ab" if i % 2 == 0 else "a" for i in range(10_000)]

    start = time.perf_counter()
    result = sorted_list_sum(large_input)
    duration = time.perf_counter() - start

    # All odd‑length strings ("a") should be removed → half the list remains
    assert len(result) == 5_000
    # All remaining strings are "ab", so the result should be a list of that value
    assert all(item == "ab" for item in result)
    # Ensure the function is reasonably fast
    assert duration < 1.0, f"Function took too long: {duration:.3f}s"