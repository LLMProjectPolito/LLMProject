import unittest
import re

def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to handle case-insensitive comparison
    lower_case_string = string.lower()
    
    # Remove any non-alphabet characters from the string
    cleaned_string = re.sub('[^a-zA-Z]', '', lower_case_string)
    
    # Use a set to store unique characters
    unique_characters = set(cleaned_string)
    
    # Return the size of the set, which represents the number of distinct characters
    return len(unique_characters)

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_string_with_all_characters_the_same(self):
        self.assertEqual(count_distinct_characters("aaaa"), 1)

    def test_string_with_all_characters_distinct(self):
        self.assertEqual(count_distinct_characters("abc"), 3)

    def test_string_with_mixed_cases(self):
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_string_with_spaces(self):
        self.assertEqual(count_distinct_characters("abc def"), 4)

    def test_string_with_punctuation(self):
        self.assertEqual(count_distinct_characters("abc, def"), 4)

    def test_string_with_single_character(self):
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_string_with_case_sensitive_characters(self):
        self.assertEqual(count_distinct_characters("abcABC"), 3)

    def test_string_with_non_english_characters(self):
        self.assertEqual(count_distinct_characters("áéíóúÁÉÍÓÚ"), 6)

    def test_string_with_duplicate_characters(self):
        self.assertEqual(count_distinct_characters("aaaBBB"), 2)

    def test_string_with_long_distinct_characters(self):
        self.assertEqual(count_distinct_characters("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 52)

    def test_string_with_special_characters(self):
        self.assertEqual(count_distinct_characters("!@#$%^&*()"), 12)

    def test_string_with_whitespace_characters(self):
        self.assertEqual(count_distinct_characters("   "), 1)

    def test_string_with_newline_characters(self):
        self.assertEqual(count_distinct_characters("\n"), 1)

    def test_string_with_tab_characters(self):
        self.assertEqual(count_distinct_characters("\t"), 1)

if __name__ == '__main__':
    unittest.main()