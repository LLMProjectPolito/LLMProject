
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

import pytest

@pytest.mark.parametrize("game, guess, expected", [
    # --- Docstring Examples ---
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),

    # --- Edge Cases: Empty and Single Element ---
    ([], [], []),                                       # Empty lists
    ([10], [10], [0]),                                  # Single element: Perfect match
    ([10], [5], [5]),                                   # Single element: Difference
    ([10], [15], [5]),                                  # Single element: Difference (other side)
    ([-5], [5], [10]),                                  # Single element: Mixed signs

    # --- Standard Scenarios ---
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),            # Perfect match
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),                  # All different
    ([10, 20, 30], [15, 25, 35], [5, 5, 5]),            # Uniform difference
    ([1, 2, 3], [3, 2, 1], [2, 0, 2]),                  # Reversed order
    ([1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]),         # All ones vs zeros

    # --- Signage and Zeros ---
    ([1, -1, 0], [-1, 1, 0], [2, 2, 0]),                # Mixed signs
    ([-5, -10, -15], [-2, -12, -15], [3, 2, 0]),        # All negatives
    ([-5, -5, 5], [-2, 5, -5], [3, 10, 10]),            # Complex negative/positive mix
    ([0, 0, 0], [0, 5, -5], [0, 5, 5]),                 # Zeros present

    # --- Magnitude and Large Integers ---
    ([100, 200], [0, 300], [100, 100]),                 # Large jumps
    ([10**12], [0], [10**12]),                          # Very large integers
    ([10**12], [-10**12], [2 * 10**12]),                # Large integer sign flip
    ([10**9, 0], [10**9 + 7, -7], [7, 7]),              # Large integer offsets
])
def test_compare_integers(game, guess, expected):
    """
    Tests various integer scenarios including empty lists, single elements,
    perfect matches, mismatches, negatives, zeros, and large integers.
    """
    assert compare(game, guess) == expected


def test_compare_floats():
    """
    Tests the function with floating point numbers using pytest.approx
    to handle potential precision issues.
    """
    game = [1.5, 2.5, 3.0]
    guess = [1.0, 3.0, 3.0]
    expected = [0.5, 0.5, 0.0]
    assert compare(game, guess) == pytest.approx(expected)