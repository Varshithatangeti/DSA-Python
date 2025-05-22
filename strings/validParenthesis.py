class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if stack:
                    top = stack[-1]
                    if top == mapping[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack
sol = Solution()
print(sol.isValid("(){}[]"))     # True
print(sol.isValid("([)]"))       # False
print(sol.isValid("{[]}"))       # True
