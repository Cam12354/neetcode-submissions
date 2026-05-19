class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenmap = {")":"(", "]":"[","}":"{"}

        for c in s:
            if c in parenmap:
                if stack and stack[-1] == parenmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        
        