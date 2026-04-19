
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

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    """
    if remaining >= need:
        total_eaten = number + need
        leftover = remaining - need
    else:
        total_eaten = number + remaining
        leftover = 0
        
    return [total_eaten, leftover]

class TestEatFunction:
    """
    Comprehensive test suite for the eat function covering standard cases,
    boundary conditions, edge cases, and type integrity.
    """

    @pytest.mark.parametrize("number, need, remaining, expected", [
        # Provided Examples
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        
        # Boundary Cases: Exact match (Remaining == Need)
        (0, 0, 0, [0, 0]),
        (10, 10, 10, [20, 0]),
        (10, 5, 5, [15, 0]),
        
        # Boundary Cases: Off-by-one
        (10, 5, 6, [15, 1]), # One more than needed
        (10, 5, 4, [14, 0]), # One less than needed
        
        # Boundary Cases: Insufficient stock
        (0, 10, 0, [0, 0]),     # Need 10, have 0, eaten 0
        (100, 1, 0, [100, 0]),  # Need 1, have 0, eaten 100
        (0, 100, 1, [1, 0]),    # Need 100, have 1, eaten 0
        (10, 5, 0, [10, 0]),    # Need 5, have 0, eaten 10
        (0, 5, 0, [0, 0]),      # Need 5, have 0, eaten 0
        
        # Edge Case: Rabbit is not hungry (need = 0)
        (10, 0, 10, [10, 10]),
        (0, 0, 10, [0, 10]),
        
        # Edge Case: Rabbit hasn't eaten anything yet (number = 0)
        (0, 5, 10, [5, 5]),
        (0, 15, 10, [10, 0]),
        
        # Maximum Constraints
        (1000, 1000, 1000, [2000, 0]),
        (1000, 0, 1000, [1000, 1000]),
        (1000, 1000, 0, [1000, 0]),
        (0, 1000, 1000, [1000, 0]),
    ])
    def test_eat_scenarios(self, number, need, remaining, expected):
        """Test various combinations of number, need, and remaining carrots."""
        assert eat(number, need, remaining) == expected

    def test_return_type(self):
        """Ensure the function returns a list containing exactly two integers."""
        result = eat(1, 1, 1)
        assert isinstance(result, list), "Return value should be a list"
        assert len(result) == 2, "Return list should contain exactly 2 elements"
        assert all(isinstance(x, int) for x in result), "All elements in the list should be integers"

    def test_immutability_of_inputs(self):
        """Ensure the function does not mutate the input variables."""
        n, nd, r = 5, 6, 10
        eat(n, nd, r)
        assert n == 5, "Input 'number' was mutated"
        assert nd == 6, "Input 'need' was mutated"
        assert r == 10, "Input 'remaining' was mutated"