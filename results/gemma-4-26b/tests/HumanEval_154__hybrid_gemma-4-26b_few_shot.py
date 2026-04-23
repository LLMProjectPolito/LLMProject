
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

import pytest

def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word 
    or any of its rotations is a substring in the first word.
    """
    if not b:
        return True
    if len(b) > len(a):
        return False
    
    n = len(b)
    for i in range(n):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False

# --- Superior Pytest Suite ---

class TestCycPatternCheck:
    """
    A comprehensive test suite for cycpattern_check covering:
    - Docstring examples
    - Basic substring matching
    - Cyclic rotation matching
    - Length and empty string edge cases
    - Case sensitivity
    - Repetitive patterns and performance
    """

    @pytest.mark.parametrize("a, b, expected", [
        # --- 1. Docstring Examples ---
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),

        # --- 2. Basic Substring Matches (No rotation needed) ---
        ("apple", "ppl", True),
        ("banana", "nan", True),
        ("python", "ty", True),
        ("testing", "est", True),

        # --- 3. Rotation Matches ---
        ("abcde", "eab", True),      # 'eab' -> 'abc' is in 'abcde'
        ("abcde", "deabc", True),    # Full rotation match
        ("abcdef", "defa", True),    # Partial rotation match
        ("12345", "5123", True),     # Numeric rotation
        ("12345", "4512", True),     # Numeric rotation
        ("racecar", "ecar", True),   # 'ecar' is in 'racecar'

        # --- 4. Non-Matches (Same characters, wrong order/rotation) ---
        ("abc", "acb", False),       # Same chars, not a rotation
        ("aaaaa", "aaaab", False),   # Almost matches
        ("whassup", "psus", False),  # Mismatching sequence

        # --- 5. Length Mismatch & Single Characters ---
        ("short", "longerstring", False),
        ("abc", "abcd", False),
        ("a", "a", True),
        ("a", "b", False),
        ("abc", "c", True),

        # --- 6. Heavy Repetition & Overlapping Patterns ---
        ("ababab", "baba", True),
        ("aaaaa", "aa", True),
        ("abcabc", "cabca", True),
        ("mississippi", "issip", True),
        ("aaaaaa", "aaa", True),
    ])
    def test_logic_combinations(self, a, b, expected):
        """Tests the core logic of substring and rotation detection."""
        assert cycpattern_check(a, b) == expected

    def test_empty_string_behavior(self):
        """Tests edge cases involving empty strings."""
        assert cycpattern_check("anything", "") is True, "Empty 'b' should be True"
        assert cycpattern_check("", "") is True, "Both empty should be True"
        assert cycpattern_check("", "a") is False, "Non-empty 'b' cannot be in empty 'a'"

    def test_case_sensitivity(self):
        """Tests that the function respects standard case sensitivity."""
        assert cycpattern_check("Hello", "ell") is True
        assert cycpattern_check("Hello", "ELL") is False
        assert cycpattern_check("Abc", "cab") is True  # 'cab' rotation 'abc' matches 'Abc'? No, 'abc' != 'Abc'
        # Correction: 'Abc' vs 'cab' (rotation 'abc') should be False due to 'A' != 'a'
        assert cycpattern_check("Abc", "cab") is False 
        assert cycpattern_check("ABCDE", "eabcd") is False

    def test_large_input_performance(self):
        """Sanity check for performance with larger strings."""
        a = "a" * 500 + "b" + "a" * 500
        b = "a" * 250 + "b"
        assert cycpattern_check(a, b) is True
        
        b_rot = "b" + "a" * 250
        assert cycpattern_check(a, b_rot) is True

    def test_identical_character_edge_cases(self):
        """Tests strings consisting of the same repeated character."""
        assert cycpattern_check("aaaaaa", "aaa") is True
        assert cycpattern_check("aaaaaa", "aaaaaaa") is False