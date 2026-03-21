import unittest
from statistics import mean

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_duplicate_elements(self):
        self.assertEqual(mean_absolute_deviation([1.0, 1.0, 1.0]), 0.0)

    def test_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0]), 1.0)

    def test_zero(self):
        self.assertEqual(mean_absolute_deviation([0.0, 0.0, 0.0]), 0.0)

    def test_mixed_numbers(self):
        self.assertEqual(round(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1), 1.0)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation([1, 2, 'a', 4])

    def test_negative_numbers_with_zero(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0]), 0.5)

    def test_large_numbers(self):
        self.assertEqual(mean_absolute_deviation([1000000.0, 2000000.0, 3000000.0, 4000000.0]), 1000000.0)

    def test_large_random_numbers(self):
        import random
        numbers = [random.random() for _ in range(1000)]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), mean(abs(x - mean(numbers)) for x in numbers))

if __name__ == '__main__':
    unittest.main()