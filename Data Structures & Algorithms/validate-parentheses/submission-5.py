class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in valids:
                if stack and stack[-1] == valids[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False