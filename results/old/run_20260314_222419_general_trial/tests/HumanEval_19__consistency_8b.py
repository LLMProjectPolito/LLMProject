import unittest

class TestSortNumbersFunction(unittest.TestCase):
    def custom_sort_key(self, num: str) -> int:
        num_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        return num_map[num]

    def test_empty_string(self):
        self.assertEqual(sort_numbers(""), "")

    def test_single_number(self):
        self.assertEqual(sort_numbers("three"), "three")

    def test_duplicate_numbers(self):
        self.assertEqual(sort_numbers("three three five one"), "one three five")

    def test_numbers_with_leading_zeros(self):
        self.assertEqual(sort_numbers("zero zero five"), "five zero")

    def test_numbers_in_mixed_case(self):
        self.assertEqual(sort_numbers("ThReE oNe FiVe"), "five one three")

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            sort_numbers("one two three four five six seven eight nine ten")

    def test_numbers_not_in_specified_range(self):
        with self.assertRaises(ValueError):
            sort_numbers("ten twelve thirteen")

    def test_single_invalid_input(self):
        with self.assertRaises(ValueError):
            sort_numbers("ten")

    def test_multiple_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort_numbers("ten eleven twelve")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            sort_numbers(12345)

    def test_duplicates(self):
        self.assertEqual(sort_numbers("three three one"), "one three three")

    def test_all_numbers(self):
        self.assertEqual(sort_numbers("one two three four five six seven eight nine"), "one two three four five six seven eight nine")

if __name__ == '__main__':
    unittest.main()