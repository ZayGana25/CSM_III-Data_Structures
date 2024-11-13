# Isaiah Lugo
# CSM III - Week 9 
# Stack Implementation

from collections import deque

def is_balanced(s):
    # Create a stack using deque
    stack = deque()
    
    # Dictionary to match opening and closing brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():  # if it's an opening bracket
            stack.append(char)
        elif char in bracket_map:  # if it's a closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack

# Tests
print(is_balanced("()"))        # True
print(is_balanced("({[]})"))    # True
print(is_balanced("({[)]}"))    # False
print(is_balanced("((()))"))    # True
print(is_balanced("({)}"))      # False
print(is_balanced(""))          # True
print(is_balanced("[(])"))      # False
