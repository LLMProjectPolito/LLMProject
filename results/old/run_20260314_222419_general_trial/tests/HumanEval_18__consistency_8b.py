import unittest

def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0
    if len(substring) > len(string):
        return 0
    
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    
    return count

def test_how_many_times():
    # Test case 1: Empty string
    assert how_many_times('', 'a') == 0

    # Test case 2: Empty substring
    assert how_many_times('aaa', '') == 0

    # Test case 3: Non-overlapping occurrences
    assert how_many_times('aaa', 'a') == 3

    # Test case 4: Overlapping occurrences
    assert how_many_times('aaaa', 'aa') == 3

    # Test case 5: No occurrences
    assert how_many_times('abc', 'def') == 0

    # Test case 6: Edge case: Substring is longer than the string
    assert how_many_times('a', 'abc') == 0

    # Test case 7: Edge case: String is empty, but substring is not
    assert how_many_times('', 'abc') == 0

    # Test case 8: Edge case: Substring and string are the same
    assert how_many_times('aaaa', 'aaaa') == 4

    # Test case 9: Edge case: Substring empty
    assert how_many_times('abc', '') == float('inf')

    # Test case 10: Multiple occurrences
    assert how_many_times('abcabc', 'abc') == 2

class TestHowManyTimesFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abc', 'd'), 0)

    def test_overlapping_cases(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_substring_longer_than_original_string(self):
        self.assertEqual(how_many_times('a', 'abc'), 0)

    def test_substring_empty(self):
        self.assertEqual(how_many_times('abc', ''), float('inf'))

    def test_original_string_empty_substring_not_empty(self):
        self.assertEqual(how_many_times('abc', 'a'), 3)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_single_occurrence(self):
        self.assertEqual(how_many_times('abcabc', 'abc'), 2)

if __name__ == '__main__':
    test_how_many_times()
    unittest.main()