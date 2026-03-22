import pytest

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    total_eaten = number
    remaining_after_meals = remaining
    
    if number < need:
        remaining_after_meals = 0
        total_eaten -= need
    
    return [total_eaten, remaining_after_meals]

import unittest

class TestEat(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_example_2(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_example_3(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_example_4(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_no_need(self):
        self.assertEqual(eat(5, 0, 10), [11, 0])

    def test_no_remaining(self):
        self.assertEqual(eat(5, 10, 0), [11, 0])

    def test_large_number(self):
        self.assertEqual(eat(1000, 5, 5), [1050, 0])

    def test_large_need(self):
        self.assertEqual(eat(5, 1000, 5), [1100, 0])

    def test_large_remaining(self):
        self.assertEqual(eat(5, 1000, 1000), [1050, 0])

    def test_zero_remaining(self):
        self.assertEqual(eat(5, 6, 0), [11, 0])

    def test_zero_need(self):
        self.assertEqual(eat(5, 0, 0), [11, 0])

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            eat(-1, 5, 10)

    def test_negative_need(self):
        with self.assertRaises(ValueError):
            eat(5, -1, 10)

    def test_negative_remaining(self):
        with self.assertRaises(ValueError):
            eat(5, 5, -10)

if __name__ == '__main__':
    unittest.main()