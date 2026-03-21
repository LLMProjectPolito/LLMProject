import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
    ('( () ) ( () () )', ['(())', '(())']),
    ('()', ['()']),
    ('((()))', ['((()))']),
    ('(())()(())', ['(())', '()', '(())']),
    ('', []),
    ('   ', []),
    ('((', ['((', '()']),
    (')(', ['()', ')']),
    ('() ()', ['()', '()']),
    ('(()) (())', ['(())', '(())']),
    ('((())) ()', ['((()))', '()']),
    ('() ((()) () (()))', ['()', '(())', '()', '(()())']),
    ('(()) () ()', ['(())', '()', '()'])
])
def test_separate_paren_groups(input_string, expected_output):
    assert separate_paren_groups(input_string.replace(' ', '')) == expected_output

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('()') == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_ignores_spaces():
    assert separate_paren_groups(' ( ) (( )) (( )( )) ') == ['()', '(())', '(()())']

def test_unbalanced_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('( ()')

def test_nested_parentheses():
    assert separate_paren_groups('(())') == ['(())']

def test_no_parentheses():
    assert separate_paren_groups('abc') == []