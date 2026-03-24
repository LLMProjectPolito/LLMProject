import pytest
import math


# Focus: Boundary Values
import pytest

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
    result = []
    for i in range(len(game)):
        result.append(abs(guess[i] - game[i]))
    return result

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `compare` calculates the absolute difference between the game scores and the guesses.
### Boundary values to test include:
###   - Empty game and guess arrays (length 0).
###   - Game and guess arrays with a single element.
###   - Game and guess arrays with multiple elements, including cases where guesses are exactly correct, significantly off, or have negative values.

### STEP 2: PLAN - List test functions names and scenarios.
### test_compare_empty_arrays
### test_compare_single_element
### test_compare_multiple_elements_correct
### test_compare_multiple_elements_incorrect

### STEP 3: CODE - Write the high-quality pytest suite.
def test_compare_empty_arrays():
    assert compare([], []) == []

def test_compare_single_element():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]

def test_compare_multiple_elements_correct():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_compare_multiple_elements_incorrect():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

# Focus: Type Scenarios
import pytest

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
    result = []
    for i in range(len(game)):
        result.append(abs(guess[i] - game[i]))
    return result

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each corresponding element in the two lists and returns a new list containing these differences. The goal is to test different scenarios related to the type of input data (e.g., all correct, some correct, all incorrect).
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_all_correct: Checks if the function returns [0, 0, ..., 0] when all guesses are correct.
### - test_some_correct: Checks if the function returns a list with some 0s and some non-zero differences when some guesses are correct.
### - test_all_incorrect: Checks if the function returns a list with all non-zero differences when all guesses are incorrect.
### STEP 3: CODE - Write the high-quality pytest suite.
### TEST CASES
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each corresponding element in the two lists and returns a new list containing these differences. The goal is to test different scenarios related to the type of input data (e.g., all correct, some correct, all incorrect).
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_all_correct: Checks if the function returns [0, 0, ..., 0] when all guesses are correct.
### - test_some_correct: Checks if the function returns a list with some 0s and some non-zero differences when some guesses are correct.
### - test_all_incorrect: Checks if the function returns a list with all non-zero differences when all guesses are incorrect.
### STEP 3: CODE - Write the high-quality pytest suite.
### TEST CASES
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each corresponding element in the two lists and returns a new list containing these differences. The goal is to test different scenarios related to the type of input data (e.g., all correct, some correct, all incorrect).
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_all_correct: Checks if the function returns [0, 0, ..., 0] when all guesses are correct.
### - test_some_correct: Checks if the function returns a list with some 0s and some non-zero differences when some guesses are correct.
### - test_all_incorrect: Checks if the function returns a list with all non-zero differences when all guesses are incorrect.
### STEP 3: CODE - Write the high-quality pytest suite.
### TEST CASES
@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_all_correct(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, 1], [0, 0, 0, 0, 2, 0]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_some_correct(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, 2], [0, 0, 0, 0, 2, 2]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_all_incorrect(game, guess, expected):
    assert compare(game, guess) == expected

# Focus: Logic Branches
import pytest

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
    result = []
    for i in range(len(game)):
        result.append(abs(guess[i] - game[i]))
    return result

def test_correct_guess():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_incorrect_guess():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_all_correct():
    assert compare([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]