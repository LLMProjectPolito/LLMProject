def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_element_list():
    assert find_max(["hello"]) == "hello"

def test_find_max_varying_lengths():
    assert find_max(["a", "ab", "abc", "abcd"]) == "abcd"

def test_find_max_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_find_max_varying_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_same_unique_chars():
    assert find_max(["aaaaa", "aa", "aaa"]) == "aaaaa"

def test_find_max_first_string_max_unique_chars():
    assert find_max(["name", "of", "string"]) == "name"

def test_find_max_not_first_string_max_unique_chars():
    assert find_max(["enam", "name", "of"]) == "enam"

def test_find_max_last_string_max_unique_chars():
    assert find_max(["of", "name", "enam"]) == "enam"

def test_find_max_multiple_words_same_length():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_multiple_words_different_lengths():
    assert find_max(["abc", "def", "h", "g"]) == "abc"

def test_find_max_no_unique_characters():
    assert find_max(["aaaa", "bb", "cc"]) == ""

def test_find_max_all_unique_characters():
    assert find_max(["abc", "def", "hgf"]) == "abc"

def test_find_max_duplicate_characters():
    assert find_max(["aabb", "cc"]) == "aabb"

def test_find_max_non_alphabetical_characters():
    assert find_max(["abc!", "def@", "hgf#"]) == "abc!"

def test_find_max_non_ascii_characters():
    assert find_max(["abcü", "defö", "hgfä"]) == "abcü"

def test_find_max_max_unique_characters():
    assert find_max(["abc", "ace", "ada"]) == "ace"

def test_find_max_multiple_max_unique_characters():
    assert find_max(["abc", "ace", "ada", "xyz"]) == "abc"