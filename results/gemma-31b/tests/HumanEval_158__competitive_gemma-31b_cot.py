
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest

def test_provided_examples():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_breaker():
    # Both have 3 unique characters, 'abc' < 'def'
    assert find_max(["def", "abc"]) == "abc"
    # Both have 2 unique characters, 'apple' (a,p,l,e=4) vs 'banana' (b,a,n=3)
    # This is not a tie, but testing logic
    assert find_max(["banana", "apple"]) == "apple"
    # Tie: 'cat' (3) and 'bat' (3), 'bat' < 'cat'
    assert find_max(["cat", "bat"]) == "bat"

def test_single_element():
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_empty_list():
    # Depending on implementation, this might return None or raise an error.
    # Assuming it returns None or handles it gracefully.
    with pytest.raises(Exception):
        # Most implementations of max() on empty sequence raise ValueError
        # If the function handles it internally, adjust this test.
        find_max([])

def test_empty_strings_in_list():
    assert find_max(["", "a"]) == "a"
    assert find_max(["", ""]) == ""

def test_all_same_unique_count():
    # All have 1 unique character
    assert find_max(["zzzz", "yyyy", "xxxx"]) == "xxxx"

def test_different_lengths_same_unique_count():
    # "aaaaa" has 1 unique, "b" has 1 unique. "aaaaa" < "b"
    assert find_max(["aaaaa", "b"]) == "aaaaa"
    # "abc" has 3 unique, "abcde" has 5 unique.
    assert find_max(["abc", "abcde"]) == "abcde"

def test_case_sensitivity():
    # 'A' and 'a' are typically treated as different unique characters
    # "Aa" (2 unique) vs "a" (1 unique)
    assert find_max(["Aa", "a"]) == "Aa"
    # "A" (1 unique) vs "a" (1 unique). "A" < "a" in ASCII
    assert find_max(["a", "A"]) == "A"

def test_special_characters():
    # "123" (3 unique) vs "!!!" (1 unique)
    assert find_max(["!!!", "123"]) == "123"
    # " @ " (2 unique: space, @) vs " # " (2 unique: space, #)
    # " # " < " @ "
    assert find_max([" @ ", " # "]) == " # "