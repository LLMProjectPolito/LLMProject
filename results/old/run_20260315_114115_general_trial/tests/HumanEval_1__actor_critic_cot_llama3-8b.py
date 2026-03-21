def test_separate_paren_groups_happy_path():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_separate_paren_groups_no_parentheses():
    assert separate_paren_groups('hello world') == []

def test_separate_paren_groups_invalid_input():
    with pytest.raises(ValueError):
        separate_paren_groups(123)

def test_separate_paren_groups_invalid_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('(((')

def test_separate_paren_groups_single_open_parenthesis():
    with pytest.raises(ValueError):
        separate_paren_groups('(')

def test_separate_paren_groups_single_close_parenthesis():
    with pytest.raises(ValueError):
        separate_paren_groups(')')

def test_separate_paren_groups_large_input():
    large_input = ''
    for i in range(100):
        large_input += '(()())'
    assert separate_paren_groups(large_input) == ['(()())'] * 100

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('() () ()') == ['()', '()', '()']

def test_separate_paren_groups_invalid_type():
    with pytest.raises(ValueError):
        separate_paren_groups(123.45)

def test_separate_paren_groups_non_string():
    with pytest.raises(ValueError):
        separate_paren_groups(None)

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('(()()) (()())') == ['(()())', '(()())']

def test_separate_paren_groups_unbalanced_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('(()')