
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
    Implementation provided for testing purposes.
    """
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

class TestEatFunction:
    """
    Blue Team QA Suite for the eat() function.
    Focuses on boundary values, docstring examples, and logic branches.
    """

    @pytest.mark.parametrize("number, need, remaining, expected", [
        # Docstring Examples
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        
        # Boundary: Minimum constraints (0)
        (0, 0, 0, [0, 0]),
        (0, 10, 0, [0, 0]),
        (0, 0, 10, [0, 0]),
        (10, 0, 0, [10, 0]),
        
        # Boundary: Maximum constraints (1000)
        (1000, 1000, 1000, [2000, 0]),
        (1000, 0, 1000, [1000, 1000]),
        (0, 1000, 1000, [1000, 0]),
        (1000, 1000, 0, [1000, 0]),
        
        # Logic: Sufficient stock (need < remaining)
        (10, 5, 20, [15, 15]),
        
        # Logic: Exactly enough stock (need == remaining)
        (10, 5, 5, [15, 0]),
        
        # Logic: Insufficient stock (need > remaining)
        (10, 100, 50, [60, 0]),
        
        # Logic: Need is zero, but stock exists
        (5, 0, 10, [5, 10]),
        
        # Logic: Need is zero, stock is zero
        (5, 0, 0, [5, 0]),
    ])
    def test_eat_scenarios(self, number, need, remaining, expected):
        """Tests various combinations of inputs including boundaries and logic branches."""
        assert eat(number, need, remaining) == expected

    def test_return_type(self):
        """Ensures the function returns a list of exactly two integers."""
        result = eat(5, 5, 5)
        assert isinstance(result, list), "Output must be a list"
        assert len(result) == 2, "Output list must contain exactly two elements"
        assert isinstance(result[0], int), "First element must be an integer"
        assert isinstance(result[1], int), "Second element must be an integer"

    @pytest.mark.parametrize("number, need, remaining", [
        (-1, 5, 10),
        (5, -1, 10),
        (5, 5, -1),
    ])
    def test_negative_inputs(self, number, need, remaining):
        """
        QA Note: While constraints specify 0 <= x <= 1000, 
        a robust function should ideally handle or define behavior for negatives.
        This test documents current behavior if negatives are passed.
        """
        # This is a placeholder for deciding if the function should raise ValueError 
        # or handle it. Given the current implementation, we check if it runs without crashing.
        try:
            eat(number, need, remaining)
        except Exception as e:
            pytest.fail(f"Function crashed on negative input: {e}")