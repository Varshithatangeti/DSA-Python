def is_valid_parentheses(s):
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Dictionary to map closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    # Iterate over each character in the input string
    for char in s:
        # If it's an opening bracket, push it onto the stack
        if char in mapping.values():
            stack.append(char)

        # If it's a closing bracket
        elif char in mapping:
            # Check if the stack is not empty
            if stack:
                # Get the top element from the stack
                top = stack[-1]
                # If the top matches the corresponding opening bracket, pop it
                if top == mapping[char]:
                    stack.pop()
                else:
                    # Mismatched brackets
                    return False
            else:
                # Closing bracket found but no opening bracket available
                return False

        else:
            # If the character is not a bracket, ignore it (optional)
            continue

    # If the stack is empty, all brackets matched correctly
    return not stack

# Example usage
input_string = "({[]})"
print(is_valid_parentheses(input_string))  # Output: True
