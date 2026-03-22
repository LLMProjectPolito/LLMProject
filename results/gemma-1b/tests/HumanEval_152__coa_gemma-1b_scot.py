import pytest
import math


# Focus: Boundary Values
import pytest

def compare(game, guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess:
            results.append(0)
        else:
            results.append(abs(guess - game[i]))
    return results

# Focus: Type Scenarios
import pytest

def compare(game, guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess:
            results.append(0)
        else:
            results.append(abs(game[i] - guess))
    return results

# Focus: Logic Branches
import pytest

def compare(game, guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess:
            results.append(0)
        else:
            results.append(abs(guess - game[i]))
    return results