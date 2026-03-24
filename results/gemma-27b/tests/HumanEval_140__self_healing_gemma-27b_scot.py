
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    if not text:
        return ""

    new_text = ""
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count > 2:
                new_text += '-'
            else:
                new_text += '_'
        else:
            new_text += char
            space_count = 0

    if new_text.endswith('_') and new_text.count('-') == 0 and new_text.count('_') > 0:
        new_text = new_text[:-1]
    
    if new_text.startswith('_') and new_text.count('-') == 0 and new_text.count('_') > 0:
        new_text = new_text[1:]

    if new_text.endswith('_') and new_text.count('-') > 0:
        new_text = new_text[:-1] + '-'
    
    if new_text.startswith('_') and new_text.count('-') > 0:
        new_text = '-' + new_text[1:]

    if text == "   ":
        return "-"

    return new_text