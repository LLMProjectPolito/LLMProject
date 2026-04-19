
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    """
    # Condition: The file's name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into the part before and after the dot
    name, ext = file_name.split('.')
    
    # Condition: The substring before the dot should not be empty, 
    # and it starts with a letter from the latin alphabet ('a'-'z' and 'A'-'Z').
    if not name or not (('a' <= name[0] <= 'z') or ('A' <= name[0] <= 'Z')):
        return 'No'
    
    # Condition: The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Condition: There should not be more than three digits ('0'-'9') in the file's name.
    digit_count = sum(1 for char in file_name if '0' <= char <= '9')
    if digit_count > 3:
        return 'No'
    
    return 'Yes'