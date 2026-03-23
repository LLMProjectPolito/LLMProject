import pytest
import math

results = []
    for i in range(len(game)):
        guess = guess[i]
        score = game[i]
        if guess == score:
            results.append(0)
        else:
            results.append(abs(guess - score))
    return results

results = []
    for i in range(len(guess)):
        if guess[i] == i+1:
            results.append(0)
        else:
            results.append(abs(guess[i] - i+1))
    return results

results = []
    for i in range(len(game)):
        guess = guess[i]
        score = game[i]
        if guess != score:
            results.append(abs(guess - score))
        else:
            results.append(0)
    return results