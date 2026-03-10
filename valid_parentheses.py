# Valid Parentheses
# Check whether the given bracket string is valid

def is_valid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# Example usage
s = "{[()]}"
print("Valid" if is_valid(s) else "Invalid")
