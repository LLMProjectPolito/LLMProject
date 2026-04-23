
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

# Note: The 'eat' function is assumed to be imported or defined above this.

def test_eat_provided_examples():
    """
    Requirement: Tests the specific examples provided in the documentation.
    This ensures that the core requirements are met exactly as described.
    """
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # --- Case: Need is zero (No eating required) ---
    (5, 0, 10, [5, 10]),
    (0, 0, 5, [0, 5]),
    (10, 0, 0, [10, 0]),
    (1000, 0, 1000, [1000, 1000]),
    
    # --- Case: Sufficient stock (remaining > need) ---
    (10, 5, 20, [15, 15]),
    (0, 5, 10, [5, 5]),
    (100, 50, 200, [150, 150]),
    (1000, 1, 1000, [1001, 999]),
    
    # --- Case: Exact stock (remaining == need) ---
    (5, 5, 5, [10, 0]),
    (0, 10, 10, [10, 0]),
    (0, 1000, 1000, [1000, 0]),
    
    # --- Case: Insufficient stock (remaining < need) ---
    (5, 10, 2, [7, 0]),
    (0, 10, 5, [5, 0]),
    (10, 10, 9, [19, 0]),
    (0, 100, 1, [1, 0]),
    (500, 600, 500, [1000, 0]),
    
    # --- Case: Zero stock available ---
    (5, 5, 0, [5, 0]),
    (5, 10, 0, [5, 0]),
    (1000, 1000, 0, [1000, 0]),
    
    # --- Case: Boundary / Extreme Constraints ---
    (1000, 1000, 1000, [2000, 0]), # Max values
    (0, 0, 0, [0, 0]),             # All zeros
    (10, 20, 5, [15, 0]),          # Small values
], ids=[
    "zero_need_standard", "zero_need_zero_start", "zero_need_zero_stock", "zero_need_max_vals",
    "sufficient_stock_standard", "sufficient_stock_zero_start", "sufficient_stock_large", "sufficient_stock_min_need",
    "exact_stock_standard", "exact_stock_zero_start", "exact_stock_max_need",
    "insufficient_stock_standard", "insufficient_stock_zero_start", "insufficient_stock_near_exact", "insufficient_stock_large_gap", "insufficient_stock_max_constraints",
    "zero_stock_available", "zero_stock_need_match", "zero_stock_need_exceed",
    "max_constraints_all", "all_zeros", "small_values"
])
def test_eat_scenarios(number, need, remaining, expected):
    """
    Comprehensive testing of various scenarios using parametrization.
    The 'ids' parameter makes it easy to identify which category failed in the test report.
    """
    assert eat(number, need, remaining) == expected

def test_eat_invariants():
    """
    Property-based testing: Checks mathematical truths that must ALWAYS hold,
    regardless of the specific input values.
    """
    test_cases = [
        (10, 500, 50),   # High need, low stock
        (10, 5, 500),    # Low need, high stock
        (0, 100, 0),     # Zero start, high need, zero stock
        (50, 25, 25),    # Exact match
    ]
    
    for number, need, remaining in test_cases:
        res = eat(number, need, remaining)
        eaten, leftover = res
        
        # Invariant 1: Leftover carrots can never be negative
        assert leftover >= 0, f"Leftover carrots negative: {leftover}"
        
        # Invariant 2: Total eaten cannot exceed the total available (initial + stock)
        assert eaten <= (number + remaining), f"Eaten {eaten} exceeds total available {number + remaining}"
        
        # Invariant 3: Total carrots (eaten + leftover) must equal initial total (number + remaining)
        # Note: This assumes 'eaten' is defined as (number + actual_amount_taken_from_stock)
        assert (eaten + leftover) == (number + remaining), "Conservation of carrots failed"