
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

@pytest.mark.parametrize("words, expected", [
    # Provided examples
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # Tie-breaking: Lexicographical order
    (["abc", "cba", "bac"], "abc"),
    (["apple", "pear"], "apple"), # apple (a,p,l,e)=4, pear (p,e,a,r)=4. 'apple' < 'pear'
    (["zebra", "apple"], "zebra"), # zebra=5, apple=4
    
    # Unique character counts
    (["a", "ab", "abc"], "abc"),
    (["abc", "ab", "a"], "abc"),
    (["aaaaa", "bbbbb", "ccccc"], "aaaaa"),
    
    # Mixed lengths and unique counts
    (["abcdef", "abcde"], "abcdef"),
    (["abcdef", "abcdefg"], "abcdefg"),
    (["test", "testing"], "testing"),
    
    # Case sensitivity (assuming standard string comparison)
    (["Apple", "apple"], "Apple"), # 'A' < 'a'
    
    # Single element
    (["hello"], "hello"),
    
    # Empty strings in list
    (["", "a"], "a"),
    (["", ""], ""),
])
def test_find_max_standard_cases(words, expected):
    assert find_max(words) == expected

def test_find_max_empty_list():
    # Depending on implementation, this might return None or raise an error.
    # Assuming it returns None or handles it gracefully.
    with pytest.raises(Exception): 
        # If the function doesn't handle empty lists, it will likely raise a ValueError (max() arg is an empty sequence)
        find_max([])

def test_find_max_special_characters():
    # Testing with numbers and symbols
    assert find_max(["123", "112", "!!!"]) == "123"
    assert find_max(["@#$", "$#@"], "@#$")

def test_find_max_large_strings():
    # Testing strings with many repeating characters vs few unique
    word1 = "a" * 1000
    word2 = "abcdefghij"
    assert find_max([word1, word2]) == word2