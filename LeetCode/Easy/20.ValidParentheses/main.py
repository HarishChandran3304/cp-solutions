class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for b in s:
            if not stack and b in ")}]":
                return False
            elif b in "({[":
                stack.append(b)
            else:
                if b != d[stack.pop()]:
                    return False
        return False if stack else True