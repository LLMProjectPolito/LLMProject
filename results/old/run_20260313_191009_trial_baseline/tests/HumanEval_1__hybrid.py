import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
    ('(( )) (( )( ))', ['(())', '(()())']),
    ('()', ['()']),
    ('(())', ['(())']),
    ('(()())', ['(()())']),
    ('( )( )', ['()', '()']),
    ('', []),
    ('( ) (( ))', ['()', '(())']),
    ('(()) (())', ['(())', '(())']),
    ('((()))', ['((()))']),
    ('()()()', ['()', '()', '()']),
])
def test_separate_paren_groups(input_string, expected_output):
    assert separate_paren_groups(input_string.replace(' ', '')) == expected_output

def test_separate_paren_groups_empty():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( ))') == ['()', '(())']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('(( ))') == ['(())']

def test_separate_paren_groups_non_nested_groups():
    assert separate_paren_groups('( )( )') == ['()', '()']

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_only_spaces():
    assert separate_paren_groups("   ") == []

def test_separate_paren_groups_unbalanced():
    with pytest.raises(ValueError):
        separate_paren_groups("((())")

def test_separate_paren_groups_nested():
    assert separate_paren_groups("(())") == ['(())']