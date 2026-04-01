class Solution:
    def countSeniors(self, details: List[str]) -> int:
        out = 0
        for d in details:
            ageSeat = d[-4:]
            print(ageSeat)
            age = int(ageSeat[:2])
            if age > 60:
                out += 1
        return out