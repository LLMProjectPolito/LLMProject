
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
    
    # Lexicographical tie-breaking
    (["apple", "pear"], "apple"),  # Both have 4 unique chars, 'apple' < 'pear'
    (["abc", "abd"], "abc"),       # Both have 3 unique chars, 'abc' < 'abd'
    (["zebra", "apple"], "zebra"), # zebra (5) > apple (4)
    
    # Single element lists
    (["hello"], "hello"),
    (["a"], "a"),
    
    # All words have same unique count
    (["cat", "dog", "bat"], "bat"), # All 3 unique, 'bat' is smallest lexicographically
    
    # Words with varying lengths but same unique counts
    (["aaaaa", "bb", "c"], "aaaaa"), # All 1 unique, 'aaaaa' < 'bb' < 'c'
    (["abcde", "abcde"], "abcde"),
    
    # Case sensitivity (Python strings are case-sensitive)
    (["Apple", "apple"], "Apple"), # 'A' < 'a'
    
    # Special characters and numbers
    (["123", "abc", "!!!"], "!!!"), # All 3 unique (or 1 for !!!), '!!!' < '123' < 'abc'
    (["a1", "b2", "c3"], "a1"),
])
def test_find_max(words, expected):
    assert find_max(words) == expected

def test_find_max_empty():
    # Testing behavior for empty list; depending on implementation 
    # it might return None or raise an error. 
    # Assuming it returns None or handles gracefully.
    with pytest.raises((ValueError, IndexError)):
        # If the function uses max() without a default, it raises ValueError
        find_max([])

def test_find_max_large_input():
    # Test with a larger set of strings
    words = ["alphabet", "beta", "gamma", "delta", "epsilon"]
    # alphabet: a,l,p,h,b,e,t (7)
    # beta: b,e,t,a (4)
    # gamma: g,a,m (3)
    # delta: d,e,l,t,a (5)
    # epsilon: e,p,s,i,l,o,n (7)
    # Tie between alphabet and epsilon. 'alphabet' < 'epsilon'.
    assert find_max(words) == "alphabet"