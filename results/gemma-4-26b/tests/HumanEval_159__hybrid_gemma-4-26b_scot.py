
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

import pytest

class TestEatFunction:
    """
    A superior, consolidated test suite for the eat() function.
    Covers docstring examples, logical branches, edge cases, and boundary constraints.
    """

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (5, 6, 10, [11, 4]),   # Example 1
        (4, 8, 9, [12, 1]),    # Example 2
        (1, 10, 10, [11, 0]),  # Example 3
        (2, 11, 5, [7, 0]),    # Example 4
    ])
    def test_docstring_examples(self, number, need, remaining, expected):
        """Validates the specific examples provided in the function documentation."""
        assert eat(number, need, remaining) == expected

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (0, 5, 10, [5, 5]),     # Basic sufficient stock
        (50, 2, 100, [52, 98]), # Large stock
        (0, 5, 100, [5, 95]),   # Zero initial eaten
        (5, 0, 10, [5, 10]),    # Need is zero
    ])
    def test_sufficient_stock(self, number, need, remaining, expected):
        """Tests cases where the stock is more than the amount needed."""
        assert eat(number, need, remaining) == expected

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (0, 10, 3, [3, 0]),     # Basic insufficient stock
        (10, 100, 50, [60, 0]), # Large need
        (5, 1, 0, [5, 0]),      # Zero stock
        (0, 500, 499, [499, 0]),# Near match insufficient
    ])
    def test_insufficient_stock(self, number, need, remaining, expected):
        """Tests cases where the stock is less than the amount needed."""
        assert eat(number, need, remaining) == expected

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (5, 5, 5, [10, 0]),     # Need equals remaining
        (10, 50, 50, [60, 0]),  # Large exact match
    ])
    def test_exact_stock(self, number, need, remaining, expected):
        """Tests cases where need exactly equals remaining."""
        assert eat(number, need, remaining) == expected

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (0, 0, 0, [0, 0]),      # All zeros
        (0, 0, 10, [0, 10]),    # No need, stock exists
        (5, 0, 10, [5, 10]),    # Already ate, no need, stock exists
        (5, 10, 0, [5, 0]),     # Need carrots, but stock is zero
        (0, 10, 0, [0, 0]),     # No eaten, need carrots, zero stock
    ])
    def test_zero_scenarios(self, number, need, remaining, expected):
        """Tests various edge cases involving zero values."""
        assert eat(number, need, remaining) == expected

    @pytest.mark.parametrize("number, need, remaining, expected", [
        (1000, 1000, 1000, [2000, 0]), # All maximums
        (1000, 0, 1000, [1000, 1000]), # Max number, zero need, max remaining
        (1000, 1000, 0, [1000, 0]),    # Max number, max need, zero remaining
        (1, 1, 1000, [2, 999]),        # Large gap (sufficient)
        (1, 1000, 1, [2, 0]),          # Large gap (insufficient)
    ])
    def test_boundary_and_extremes(self, number, need, remaining, expected):
        """Tests the upper boundary (1000) and scenarios with large numerical gaps."""
        assert eat(number, need, remaining) == expected

    def test_return_type_and_structure(self):
        """Ensures the function returns a list of exactly two integers."""
        result = eat(1, 1, 1)
        assert isinstance(result, list), "Result should be a list"
        assert len(result) == 2, "Result list must have exactly 2 elements"
        assert isinstance(result[0], int), "First element must be an integer"
        assert isinstance(result[1], int), "Second element must be an integer"