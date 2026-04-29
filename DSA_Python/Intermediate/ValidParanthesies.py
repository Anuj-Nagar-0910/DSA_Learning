"""
Check whether a bracket sequence is valid using a stack-based approach.
"""


def isValid(s: str) -> str:
    """
    Validate a string containing brackets and return "true" or "false".

    A string is valid if:
    1. Every opening bracket has a matching closing bracket of the same type.
    2. Brackets are closed in the correct order.
    """
    # Use a dictionary to map closing brackets to their open counterparts
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map:
            # It's a closing bracket
            # Pop the top element if stack isn't empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element matches the mapping
            if bracket_map[char] != top_element:
                return "false"
        else:
            # It's an opening bracket, push to stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return "true" if not stack else "false"

if __name__ == '__main__':
	s = input().strip()
	result = isValid(s)
	print(result)
