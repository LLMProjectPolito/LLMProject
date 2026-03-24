
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
    result = ""
    space_count = 0
    for char in text:
        if char == ' ':
            if space_count > 0:
                result += '-'
                space_count -= 1
            else:
                result += char
        else:
            result += char
            space_count += 1
    return result