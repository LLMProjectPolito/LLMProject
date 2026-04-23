
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

import pytest
from your_module import simplify  # Replace your_module

# Suite 1
def test_simplify_positive_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("10/1", "1/1") == True

def test_simplify_fraction_result_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "3/1") == False
    assert simplify("2/5", "4/2") == False
    assert simplify("1/3", "2/2") == False

def test_simplify_equal_fractions():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("5/5", "5/5") == True

def test_simplify_large_numbers():
    assert simplify("1000/1000", "1000/1000") == True
    assert simplify("12345/6789", "6789/12345") == True
    assert simplify("1000000/1000000", "1000000/1000000") == True

def test_simplify_different_denominators():
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("5/7", "7/5") == True

def test_simplify_numerator_equals_denominator():
    assert simplify("2/2", "2/2") == True
    assert simplify("5/5", "5/5") == True
    assert simplify("10/10", "10/10") == True

def test_simplify_simple_case():
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_different_signs():
    assert simplify("-1/2", "2/1") == False
    assert simplify("1/2", "-2/1") == False
    assert simplify("-1/2", "-2/1") == True #Should be True because the fraction is simplified

def test_simplify_fraction_with_decimal_representation():
    assert simplify("1/2", "2/1") == True

def test_simplify_very_large_numbers():
    assert simplify("1000000000000/1000000000000", "1000000000000/1000000000000") == True

def test_simplify_small_numbers():
    assert simplify("1/10", "10/1") == True
    assert simplify("9/10", "10/9") == True



# Suite 2
def test_simplify_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_true_case2():
    assert simplify("2/3", "3/2") == True

def test_simplify_true_case3():
    assert simplify("4/7", "7/4") == True

def test_simplify_true_case4():
    assert simplify("1/2", "2/1") == True

def test_simplify_true_case5():
    assert simplify("3/4", "4/3") == True

def test_simplify_true_case6():
    assert simplify("5/6", "6/5") == True

def test_simplify_true_case7():
    assert simplify("1/1", "1/1") == True

def test_simplify_true_case8():
    assert simplify("10/10", "10/10") == True

def test_simplify_true_case9():
    assert simplify("100/100", "100/100") == True
    
def test_simplify_true_case10():
    assert simplify("1/10", "10/1") == True

def test_simplify_true_case11():
    assert simplify("2/5", "5/2") == True

def test_simplify_true_case12():
    assert simplify("1/3", "3/1") == True

def test_simplify_true_case13():
    assert simplify("7/1", "1/7") == True
    
def test_simplify_true_case14():
    assert simplify("10/1", "1/10") == True
    
def test_simplify_true_case15():
    assert simplify("1/2", "2/2") == True

def test_simplify_true_case16():
    assert simplify("2/2", "2/2") == True

def test_simplify_true_case17():
    assert simplify("1/1", "1/1") == True

def test_simplify_true_case18():
    assert simplify("1/1", "1/1") == True

def test_simplify_true_case19():
    assert simplify("3/3", "3/3") == True

def test_simplify_true_case20():
    assert simplify("1/1", "1/1") == True
    

def test_simplify_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_false_case3():
    assert simplify("1/2", "2/3") == False

def test_simplify_false_case4():
    assert simplify("2/3", "3/4") == False

def test_simplify_false_case5():
    assert simplify("1/3", "3/2") == False

def test_simplify_false_case6():
    assert simplify("1/4", "4/1") == False

def test_simplify_false_case7():
    assert simplify("5/7", "7/5") == False

def test_simplify_false_case8():
    assert simplify("1/5", "5/4") == False

def test_simplify_false_case9():
    assert simplify("1/2", "1/2") == False

def test_simplify_false_case10():
    assert simplify("1/3", "1/3") == False

def test_simplify_false_case11():
    assert simplify("1/4", "1/4") == False

def test_simplify_false_case12():
    assert simplify("2/3", "3/3") == False
    
def test_simplify_false_case13():
    assert simplify("1/1", "2/1") == False

def test_simplify_false_case14():
    assert simplify("1/1", "1/2") == False

def test_simplify_false_case15():
    assert simplify("1/1", "1/1") == False

def test_simplify_false_case16():
    assert simplify("2/1", "1/1") == False

def test_simplify_false_case17():
    assert simplify("1/1", "1/1") == False

def test_simplify_false_case18():
    assert simplify("3/3", "3/3") == False

def test_simplify_false_case19():
    assert simplify("1/1", "1/1") == False

def test_simplify_false_case20():
    assert simplify("1/1", "1/1") == False