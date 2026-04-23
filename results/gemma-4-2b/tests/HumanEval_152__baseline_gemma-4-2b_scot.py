
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """

```python
import pytest
from your_module import compare  # Assuming the function is in your_module.py

# STEP 1: REASONING
# The `compare` function takes two lists, `game` and `guess`, of equal length.
# It calculates the difference between each element in `guess` and the corresponding element in `game`.
# If the guess matches the game, the difference is 0. Otherwise, the difference is the absolute difference.
# We need to write a pytest suite to test various scenarios, including:
# 1. Empty lists
# 2. Lists with all matches
# 3. Lists with no matches
# 4. Lists with some matches and some mismatches
# 5. Lists with different types of mismatches (positive and negative)
# 6. Lists with zero values

# STEP 2: PLAN
# Test functions:
# - test_empty_lists: Checks the behavior with empty lists.
# - test_all_matches: Checks the behavior when all guesses match the game.
# - test_no_matches: Checks the behavior when all guesses are different from the game.
# - test_mixed_matches: Checks the behavior with a mix of matches and mismatches.
# - test_positive_mismatches: Checks the behavior with positive differences.
# - test_negative_mismatches: Checks the behavior with negative differences.
# - test_zero_values: Checks the behavior with zero values in the lists.

# STEP 3: CODE
@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        ([], [], []),
        ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
        ([1, 2, 3], [4, 5, 6], [1, 1, 1]),
        ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 4], [0, 0, 1]),
        ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
        ([0, 0, 0], [1, 1, 1], [1, 1, 1]),
        ([1, 1, 1], [0, 0, 0], [1, 1, 1]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 1, 1], [1,