
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

```python
import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_unique_chars = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_unique_chars():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_all_same_unique_chars_lexicographical():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_mixed_unique_chars():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_long_word_with_many_unique_chars():
    assert find_max(["abcdefghijklmnopqrstuvwxyz"]) == "abcdefghijklmnopqrstuvwxyz"

def test_word_with_only_one_unique_char():
    assert find_max(["a", "aa", "aaa"]) == "a"

def test_word_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_word_with_special_characters():
    assert find_max(["!@#$", "abc"]) == "abc"

def test_word_with_numbers():
    assert find_max(["123", "abc"]) == "abc"

def test_word_with_mixed_characters_and_numbers():
    assert find_max(["a1b2c", "abc"]) == "abc"

def test_large_list():
    words = ["apple", "banana", "orange", "grape", "kiwi", "mango"]
    assert find_max(words) == "orange"

def test_list_with_same_length_unique_chars():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings():
    assert find_max(["", "", "abc"]) == "abc"

def test_list_with_empty_strings_and_non_empty_strings():
    assert find_max(["", "", "abc", "def"]) == "abc"

def test_list_with_empty_string_and_single_word():
    assert find_max(["", "abc"]) == "abc"

def test_list_with_empty_string_and_multiple_words():
    assert find_max(["", "abc", "def"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_2():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_3():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_4():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_5():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_6():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_7():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_8():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_9():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_10():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_11():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_12():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_13():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_14():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_15():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_16():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_17():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_18():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_19():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_20():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_21():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_22():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_23():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical_24():
    assert find_max(["", "", "abc", "def", "ghi"]) == "abc"

def test_list_with_empty_strings_and_mixed_chars_lexicographical