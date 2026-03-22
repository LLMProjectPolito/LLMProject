import pytest

# Assume the function is imported from the module where it is defined.
# from my_module import sorted_list_sum


@pytest.mark.parametrize(
    "input_list, expected",
    [
        # Empty list
        ([], []),

        # All strings have odd length → result should be empty
        (["a", "abc", "xyz"], []),

        # All strings have even length, already sorted correctly
        (["ab", "cd", "ef"], ["ab", "cd", "ef"]),

        # Mixed odd/even lengths, simple case
        (["aa", "a", "aaa"], ["aa"]),

        # Mixed with multiple even-length strings, alphabetical tie‑break
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),

        # Duplicates should be preserved after filtering
        (["ab", "cd", "ab", "ef"], ["ab", "ab", "cd", "ef"]),

        # Same length strings, need alphabetical ordering
        (["dog", "cat", "bat", "ant"], ["ant", "bat", "cat", "dog"]),

        # Mixed lengths, ensure sorting by length first then alphabetically
        (["a", "bb", "ccc", "dd", "eeee", "ff"], ["bb", "dd", "ff", "eeee"]),

        # Case sensitivity: uppercase letters come before lowercase in ASCII
        (["Ab", "ab", "Aa", "aa"], ["Aa", "Ab", "aa", "ab"]),
    ],
)
def test_sorted_list_sum_various_cases(input_list, expected):
    # Make a copy to verify the function does not mutate the original list
    original_copy = list(input_list)

    result = sorted_list_sum(input_list)

    assert result == expected, f"Expected {expected}, got {result}"
    # Ensure the original list is unchanged
    assert input_list == original_copy


def test_sorted_list_sum_large_input():
    # Generate a large list with a pattern of even and odd length strings
    base_even = ["ab", "cd", "ef", "gh"]
    base_odd = ["a", "bcd", "efg"]
    large_input = (base_even + base_odd) * 250  # 250 * 7 = 1750 elements

    expected = sorted([s for s in large_input if len(s) % 2 == 0],
                      key=lambda w: (len(w), w))

    result = sorted_list_sum(large_input)

    assert result == expected
    # Verify that the function handled the large input efficiently (no exceptions)


def test_sorted_list_sum_invalid_types():
    # The function is documented to accept a list of strings.
    # Supplying non‑string elements should raise a TypeError (or similar).
    with pytest.raises(Exception):
        sorted_list_sum([1, "ab", None])