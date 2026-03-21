import pytest
import math


# Focus: Boundary Values
def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('(())') == ['(())']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_single_open_paren():
    assert separate_paren_groups('(') == ['(']

def test_separate_paren_groups_single_close_paren():
    assert separate_paren_groups(')') == [')']

def test_separate_paren_groups_only_spaces():
    assert separate_paren_groups('   ') == []

# Focus: Empty and Single Group Scenarios
def test_empty_string():
    assert separate_paren_groups('') == []

def test_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_single_group_with_spaces():
    assert separate_paren_groups('( ) ') == ['()']

# Focus: Nested and Unbalanced Parentheses Scenarios
def test_separate_paren_groups_nested_and_unbalanced():
    assert separate_paren_groups('(( )) (( )( ))') == ['(())', '(()())']
    assert separate_paren_groups('(( )) (( )( )) ( )') == ['(())', '(()())', '( )']

def test_separate_paren_groups_unbalanced():
    assert separate_paren_groups('( ( )') == ['( ( )']
    assert separate_paren_groups(') ( )') == [') ( )']

def test_separate_paren_groups_nested_and_unbalanced_with_trailing_paren():
    assert separate_paren_groups('(( )) (( )( )) (') == ['(())', '(()())', '(']
    assert separate_paren_groups('(( )) (( )( )) )') == ['(())', '(()())', ')']