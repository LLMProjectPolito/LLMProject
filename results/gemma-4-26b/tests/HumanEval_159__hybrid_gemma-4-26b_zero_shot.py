
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
    Implementation of the rabbit eating carrots logic.
    Returns a list: [total_eaten, remaining_stock]
    """
    eat_amount = min(need, remaining)
    total_eaten = number + eat_amount
    left_over = remaining - eat_amount
    return [total_eaten, left_over]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # --- Provided Examples ---
    (5, 6, 10, [11, 4]),    # Sufficient stock
    (4, 8, 9, [12, 1]),     # Sufficient stock
    (1, 10, 10, [11, 0]),   # Exact stock
    (2, 11, 5, [7, 0]),     # Insufficient stock

    # --- Boundary Cases: Zeroes ---
    (0, 0, 0, [0, 0]),      # All zeros
    (0, 5, 5, [5, 0]),      # Starting with zero eaten, exact stock
    (5, 0, 10, [5, 10]),    # Need zero more
    (5, 10, 0, [5, 0]),     # Zero remaining in stock
    (0, 10, 0, [0, 0]),     # Zero eaten, need more, but zero stock

    # --- Boundary Cases: Equality & Proximity ---
    (5, 5, 5, [10, 0]),     # need == remaining
    (5, 4, 5, [9, 1]),      # need < remaining
    (5, 6, 5, [10, 0]),     # need > remaining

    # --- Constraint Limits (Max 1000) ---
    (1000, 1000, 1000, [2000, 0]), # Maxed out everything
    (1000, 0, 1000, [1000, 1000]), # Max number, zero need
    (0, 1000, 1000, [1000, 0]),    # Zero number, max need and remaining
    (1000, 1000, 0, [1000, 0]),    # Max eaten, max need, zero stock
    (1000, 1, 1000, [1001, 999]),  # Max constraints with minimal need
    (1, 1000, 1, [2, 0]),          # Minimal number/remaining, max need

    # --- Insufficient Stock Variations ---
    (10, 100, 50, [60, 0]),  # Need much more than available
    (10, 100, 99, [109, 0]), # Need 1 more than available
    (10, 100, 1, [11, 0]),   # Only 1 available
])
def test_eat_logic(number, need, remaining, expected):
    """Tests the core logic across various scenarios including examples, zeroes, equality, and max constraints."""
    assert eat(number, need, remaining) == expected

def test_eat_output_format():
    """Ensures the function returns a list of exactly two integers."""
    result = eat(5, 5, 5)
    assert isinstance(result, list), "Output should be a list"
    assert len(result) == 2, "Output list should have exactly 2 elements"
    assert all(isinstance(x, int) for x in result), "All elements in the list must be integers"

def test_immutability_of_inputs():
    """Ensures that the function does not mutate the input arguments."""
    n, ne, r = 5, 5, 10
    eat(n, ne, r)
    assert n == 5
    assert ne == 5
    assert r == 10

def test_large_scale_consistency():
    """Verifies that the logic holds for a large number of iterations to check arithmetic integrity."""
    for i in range(1001):
        res = eat(i, i, i)
        # Mathematically: total = i + i = 2i, left = i - i = 0
        assert res == [2 * i, 0]

if __name__ == "__main__":
    pytest.main([__file__])