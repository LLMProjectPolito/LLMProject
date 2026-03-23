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
    
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining_carrots = remaining - eaten
    
    return [total_eaten, remaining_carrots]

class TestEat:
    def test_example_cases(self):
        assert eat(5, 6, 10) == [11, 4]
        assert eat(4, 8, 9) == [12, 1]
        assert eat(1, 10, 10) == [11, 0]
        assert eat(2, 11, 5) == [7, 0]

    def test_enough_carrots(self):
        assert eat(10, 5, 10) == [15, 0]
        assert eat(0, 10, 20) == [10, 10]
        assert eat(50, 50, 100) == [100, 0]

    def test_not_enough_carrots(self):
        assert eat(10, 20, 5) == [15, 0]
        assert eat(0, 10, 5) == [5, 0]
        assert eat(50, 100, 20) == [70, 0]

    def test_zero_need(self):
        assert eat(5, 0, 10) == [5, 10]
        assert eat(0, 0, 0) == [0, 0]
        assert eat(100, 0, 50) == [100, 50]

    def test_zero_remaining(self):
        assert eat(5, 6, 0) == [5, 0]
        assert eat(0, 10, 0) == [0, 0]
        assert eat(100, 50, 0) == [100, 0]

    def test_edge_cases(self):
        assert eat(0, 0, 0) == [0, 0]
        assert eat(1000, 1000, 1000) == [2000, 0]
        assert eat(1000, 1000, 0) == [1000, 0]
        assert eat(0, 1000, 1000) == [1000, 0]
        assert eat(0, 1000, 0) == [0, 0]

    def test_large_numbers(self):
        assert eat(500, 500, 500) == [1000, 0]
        assert eat(999, 1, 1) == [1000, 0]
        assert eat(1, 999, 1) == [2, 0]

    def test_constraints(self):
        # Test that the function doesn't crash with valid inputs at the constraints boundaries
        assert eat(0, 0, 0) == [0, 0]
        assert eat(1000, 1000, 1000) == [2000, 0]

    def test_need_less_than_remaining(self):
        assert eat(3, 2, 5) == [5, 3]

    def test_need_equal_to_remaining(self):
        assert eat(7, 3, 3) == [10, 0]

    def test_no_remaining_carrots(self):
        assert eat(1, 5, 0) == [1, 0]

    def test_zero_initial_eaten(self):
        assert eat(0, 5, 5) == [5, 0]

    def test_large_numbers_not_enough_remaining(self):
        assert eat(500, 600, 100) == [600, 0]

    def test_edge_case_number_1000(self):
        assert eat(1000, 1, 1) == [1001, 0]

    def test_edge_case_need_1000(self):
        assert eat(1, 1000, 1000) == [1001, 0]

    def test_edge_case_remaining_1000(self):
        assert eat(1, 1, 1000) == [2, 999]

    def test_all_zeros(self):
        assert eat(0, 0, 0) == [0, 0]

    def test_need_greater_than_remaining_and_initial_eaten(self):
        assert eat(5, 10, 2) == [7, 0]

    def test_remaining_equals_need(self):
        assert eat(2, 3, 3) == [5, 0]

    def test_remaining_less_than_need(self):
        assert eat(1, 5, 2) == [3, 0]

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        (3, 2, 5, [5, 3]),
        (7, 3, 3, [10, 0]),
        (1, 5, 0, [1, 0]),
        (0, 5, 5, [5, 0]),
        (5, 0, 10, [5, 10]),
        (5, 6, 0, [5, 0]),
        (500, 500, 1000, [1000, 500]),
        (500, 600, 100, [600, 0]),
        (1000, 1, 1, [1001, 0]),
        (1, 1000, 1000, [1001, 0]),
        (1, 1, 1000, [2, 999]),
        (0, 0, 0, [0, 0]),
        (5, 10, 2, [7, 0]),
        (2, 3, 3, [5, 0]),
        (1, 5, 2, [3, 0])
    ])
    def test_parameterized(self, number, need, remaining, expected):
        assert eat(number, need, remaining) == expected