class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        seen = []
        for c in s:
            if c in valids:
                if seen and seen[-1] == valids[c]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(c)
        return True if not seen else False
