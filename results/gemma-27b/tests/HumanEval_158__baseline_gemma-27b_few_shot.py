
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_max():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_with_duplicates():
    assert find_max(["apple", "banana", "orange"]) == "orange"

def test_find_max_mixed_lengths():
    assert find_max(["a", "aa", "aaa", "aaaa"]) == "aaaa"

def test_find_max_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@#"