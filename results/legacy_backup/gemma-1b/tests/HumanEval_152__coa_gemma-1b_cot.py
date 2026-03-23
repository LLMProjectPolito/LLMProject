import pytest
import math


# Focus: Boundary Values
def compare(game, guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess:
            results.append(0)
        else:
            results.append(abs(game[i] - guess))
    return results

# Focus: Type Scenarios
def compare(game, guess):
    results = []
    for i in range(len(game)):
        score = 0
        if game[i] == guess:
            score = 0
        results.append(abs(score - game[i]))
    return results

# Focus: Logic Branches
def compare(game, guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess:
            results.append(0)
        else:
            results.append(abs(guess - game[i]))
    return results