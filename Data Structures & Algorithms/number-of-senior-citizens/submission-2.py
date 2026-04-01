class Solution:
    def countSeniors(self, details: List[str]) -> int:
        out = 0
        for d in details:
            age = int(d[-4:-2])
            if age > 60:
                out += 1
        return out