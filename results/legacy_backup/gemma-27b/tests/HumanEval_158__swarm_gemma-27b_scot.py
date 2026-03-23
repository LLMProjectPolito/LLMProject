import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""

    max_unique_chars = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word

    return max_word

def test_empty_list():
    assert find_max([]) == ""

def test_all_words_same_unique_count_lexicographical():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_list_with_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_edge_case_long_string_with_few_unique():
    assert find_max(["aaaaaaaaaa", "abcdefgh"]) == "abcdefgh"

def test_edge_case_mix_of_long_and_short_with_same_unique():
    assert find_max(["abcde", "fghij", "klmno"]) == "abcde"

def test_edge_case_long_string_with_all_unique_vs_short_with_all_unique():
    assert find_max(["abcdefg", "xyz"]) == "abcdefg"

def test_edge_case_long_string_with_few_unique_vs_short_with_all_unique():
    assert find_max(["aaaaaaaaaa", "xyz"]) == "xyz"

def test_edge_case_special_characters():
    assert find_max(["!@#$", "abc"]) == "!@#$"

def test_edge_case_numbers_and_letters():
    assert find_max(["12345", "abcde"]) == "12345"

def test_edge_case_unicode_characters():
    assert find_max(["你好世界", "abc"]) == "你好世界"

def test_edge_case_mixed_unicode_and_ascii():
    assert find_max(["你好abc", "abc"]) == "你好abc"

def test_edge_case_long_string_with_repeated_unicode():
    assert find_max(["你好你好你好", "abc"]) == "你好你好你好"

def test_edge_case_long_string_with_repeated_ascii():
    assert find_max(["aaaaaaaaaa", "abc"]) == "aaaaaaaaaa"

def test_edge_case_all_same_character_string():
    assert find_max(["aaaaa", "bbbbb", "ccccc"]) == "aaaaa"

def test_edge_case_empty_string_and_all_same_character_string():
    assert find_max(["", "aaaaa"]) == "aaaaa"

def test_edge_case_all_same_character_string_and_unique_string():
    assert find_max(["aaaaa", "abc"]) == "abc"

def test_edge_case_long_string_with_many_repeats_and_unique():
    assert find_max(["aaaaaaaaaabbbbbbbbbbcccccccccdddddddddd", "abc"]) == "aaaaaaaaaabbbbbbbbbbcccccccccdddddddddd"

def test_edge_case_long_string_with_many_repeats_and_unique_lexicographical():
    assert find_max(["aaaaaaaaaabbbbbbbbbbcccccccccdddddddddd", "abcdefgh"]) == "abcdefgh"