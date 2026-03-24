import pytest

def compare(game, guess):
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(guess - game[i]))
    return result

def test_compare_example1():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_example2():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_empty():
    assert compare([], []) == []

def test_compare_same_scores():
    assert compare([1,1,1,1,1],[1,1,1,1,1]) == [0,0,0,0,0]