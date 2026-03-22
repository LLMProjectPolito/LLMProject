def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_empty():
    assert find_max([]) == ""

def test_find_max_same_unique():
    assert find_max(["abc", "def"]) == "abc"

def test_find_max_one_unique():
    assert find_max(["abc", "ab"]) == "abc"

def test_find_max_complex():
    assert find_max(["apple", "banana", "orange"]) == "banana"

def test_find_max_duplicate_unique():
    assert find_max(["abc", "ab", "ac"]) == "abc"