class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif c in "([{":
                stack.append(c)
            else:
                return False
        if not stack:
            return True
        else:
            return False
