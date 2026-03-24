
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
from math import sqrt

def compare(list1, list2):
    """
    Compares two lists element by element.

    Args:
        list1: The first list.
        list2: The second list.

    Returns:
        A list of integers, where each element is the result of comparing
        the corresponding elements of list1 and list2.
    """
    result = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            result.append(i)
        else:
            result.append(0)
    return result

def test_compare_positive():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_positive():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_positive():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_negative():
    assert compare([1, 2, 3, 4, 5, 1], [-1, -2, -3, -4, -2, -5]) == [0, 0, 0, 0, 3, 3]

def test_compare_negative():
    assert compare([1, 2, 3, 4, 5, 1], [-1, -2, -3, -4, -2, -5]) == [0, 0, 0, 0, 3, 3]

def test_compare_negative():
    assert compare([0, 5, 0, 0, 0, 4], [-1, -2, -3, -4, -2, -5]) == [4, 4, 1, 0, 0, 6]