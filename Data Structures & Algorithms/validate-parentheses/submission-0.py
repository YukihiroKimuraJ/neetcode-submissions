class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {")":"(","}":"{","]":"["}
        for c in s:
            if c in "({[":
                stack.append(c)
            else:                        
                if not stack: return False
                if stack.pop() != ref[c]: return False
        return not stack              