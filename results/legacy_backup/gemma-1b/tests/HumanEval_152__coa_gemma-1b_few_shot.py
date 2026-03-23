import pytest
import math


# Focus: Boundary Values
def compare(game,guess):
    result = []
    for i in range(len(game)):
        if game[i] == guess:
            result.append(0)
        else:
            result.append(abs(game[i] - guess))
    return result

# Focus: Type Scenarios
def compare(game,guess):
    result = []
    for i in range(len(game)):
        if game[i] == guess:
            result.append(0)
        else:
            result.append(abs(game[i] - guess))
    return result

# Focus: Logic Branches
def compare(game,guess):
    result = []
    for i in range(len(game)):
        if game[i] == guess:
            result.append(0)
        else:
            result.append(abs(game[i] - guess))
    return result