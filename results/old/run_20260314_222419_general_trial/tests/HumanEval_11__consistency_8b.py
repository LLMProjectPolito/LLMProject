import unittest

class TestStringXOR(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(string_xor('', '110'), '110')
        self.assertEqual(string_xor('110', ''), '110')

    def test_single_character_strings(self):
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('1', '1'), '0')

    def test_strings_with_different_lengths(self):
        self.assertEqual(string_xor('110', '1101'), '0000')
        self.assertEqual(string_xor('1101', '110'), '0000')

    def test_unequal_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_strings_of_different_length(self):
        with self.assertRaises(IndexError):
            string_xor('101', '1010')

    def test_strings_with_invalid_characters(self):
        with self.assertRaises(ValueError):
            string_xor('110a', '1101')

    def test_equal_strings(self):
        self.assertEqual(string_xor('101', '101'), '000')

    def test_strings_of_same_length(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_same_length(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_strings_with_only_ones_and_zeros(self):
        self.assertEqual(string_xor('111', '000'), '111')

    def test_empty_string(self):
        self.assertEqual(string_xor('110', ''), '110')

    def test_xor_with_itself(self):
        self.assertEqual(string_xor('010', '010'), '000')

    def test_zero_length(self):
        self.assertEqual(string_xor('', ''), '')

    def test_very_long_strings(self):
        long_string = '1' * 1000
        self.assertEqual(string_xor(long_string, long_string), '0' * 1000)

if __name__ == '__main__':
    unittest.main()