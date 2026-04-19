
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

# The function 'eat' is assumed to be defined in the environment as per instructions.

@pytest.mark.parametrize("number, need, remaining, expected", [
    # --- Provided Examples ---
    (5, 6, 10, [11, 4]),   # Sufficient stock
    (4, 8, 9, [12, 1]),    # Sufficient stock
    (1, 10, 10, [11, 0]),  # Exact stock
    (2, 11, 5, [7, 0]),    # Insufficient stock
    
    # --- Edge Cases: Zeroes ---
    (0, 5, 10, [5, 5]),    # Zero already eaten, sufficient stock
    (10, 0, 10, [10, 10]), # Zero need, stock remains untouched
    (10, 5, 0, [10, 0]),    # Zero remaining, cannot eat more
    (0, 0, 0, [0, 0]),     # All zeros
    
    # --- Edge Cases: Boundaries ---
    (1000, 1000, 1000, [2000, 0]), # Max constraints, exact stock
    (1000, 1000, 0, [1000, 0]),    # Max constraints, no stock
    (0, 1000, 1000, [1000, 0]),    # Max need, max stock
    (1000, 0, 1000, [1000, 1000]), # Max initial, no need
    
    # --- Logic Stress Tests ---
    (10, 1, 1, [11, 0]),   # Minimal need and stock (Equal)
    (10, 2, 1, [11, 0]),   # Minimal need and stock (Insufficient)
    (10, 1, 2, [11, 1]),   # Minimal need and stock (Sufficient)
])
def test_eat_logic(number, need, remaining, expected):
    """
    Tests the eat function against various scenarios including 
    sufficient, exact, and insufficient carrot stocks.
    """
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """
    Ensure the function returns a list of two integers.
    """
    result = eat(5, 5, 5)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)

def test_eat_immutability():
    """
    Ensure the function does not modify input variables (though integers are immutable in Python,
    this is a sanity check for the logic).
    """
    num, nd, rem = 5, 5, 5
    eat(num, nd, rem)
    assert num == 5
    assert nd == 5
    assert rem == 5