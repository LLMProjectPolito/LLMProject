import pytest
from typing import List

def test_separate_paren_groups_empty_string():
    with pytest.raises(ValueError):
        separate_paren_groups("")
    assert separate_paren_groups("") is None


def test_separate_paren_groups_single_group():
    assert separate_paren_groups("( )") == ["()"]


def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]


def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups("( ( ) )") == ["( ( ) )"]


def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (")


def test_separate_paren_groups_unbalanced_groups_2():
    with pytest.raises(ValueError):
        separate_paren_groups(") (")


def test_separate_paren_groups_unbalanced_groups_3():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) )")


def test_separate_paren_groups_with_spaces():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]


def test_separate_paren_groups_with_consecutive_spaces():
    assert separate_paren_groups("( )  (( ))  (( )( ))") == ["()", "(())", "(()())"]


def test_separate_paren_groups_with_leading_trailing_spaces():
    assert separate_paren_groups("   ( ) (( )) (( )( ))  ") == ["()", "(())", "(()())"]


def test_separate_paren_groups_starting_with_parenthesis():
    with pytest.raises(ValueError):
        separate_paren_groups("(( )) (( )( ))")
    assert separate_paren_groups("(( )) (( )( ))") is None


def test_separate_paren_groups_ending_with_parenthesis():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( ))(")
    assert separate_paren_groups("( ) (( )) (( )( ))(") is None


def test_separate_paren_groups_consecutive_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( ))((")
    assert separate_paren_groups("( ) (( )) (( )( ))((") is None


def test_separate_paren_groups_not_properly_closed():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( ")
    assert separate_paren_groups("( ) (( )) (( )( ") is None


def test_separate_paren_groups_not_properly_opened():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( ) )")
    assert separate_paren_groups("( ) (( )) (( ) )") is None


def test_separate_paren_groups_not_properly_nested():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( ))( (")


def test_separate_paren_groups_not_properly_closed_at_start():
    with pytest.raises(ValueError):
        separate_paren_groups(") ( ) (( )) (( )( ))")
    assert separate_paren_groups(") ( ) (( )) (( )( ))") is None


def test_separate_paren_groups_not_properly_opened_at_start():
    with pytest.raises(ValueError):
        separate_paren_groups("( ( ) (( )) (( )( ))")


def test_separate_paren_groups_not_properly_nested_at_start():
    with pytest.raises(ValueError):
        separate_paren_groups("( ( ) (( )) (( )( ))(")


def test_separate_paren_groups_not_properly_closed_at_end():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( )) )")


def test_separate_paren_groups_not_properly_opened_at_end():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( ))(")


def test_separate_paren_groups_not_properly_nested_at_end():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (( )) (( )( ))( ")