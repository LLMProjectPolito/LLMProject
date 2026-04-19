
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

def test_find_max_provided_examples():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_empty_strings():
    # Both have 0 unique characters, "" is lexicographically first
    assert find_max(["", ""]) == ""
    # "a" has 1 unique, "" has 0
    assert find_max(["", "a"]) == "a"

def test_find_max_lexicographical_tie():
    # "apple" has {a, p, l, e} (4)
    # "apply" has {a, p, l, y} (4)
    # "apple" comes before "apply" lexicographically
    assert find_max(["apple", "apply"]) == "apple"
    
    # "banana" has {b, a, n} (3)
    # "cherry" has {c, h, e, r, y} (5)
    assert find_max(["banana", "cherry"]) == "cherry"

def test_find_max_case_sensitivity():
    # Assuming case sensitivity: 'A' and 'a' are different unique characters
    # "Aa" has 2 unique characters, "aa" has 1
    assert find_max(["Aa", "aa"]) == "Aa"

def test_find_max_all_same_unique_count():
    # All have 1 unique character, "a" is lexicographically first
    assert find_max(["c", "b", "a"]) == "a"
    # All have 1 unique character, "aaaa" is lexicographically first
    assert find_max(["bbb", "aaa", "ccc"]) == "aaa"