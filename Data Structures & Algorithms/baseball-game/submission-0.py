class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for o in operations:
            if o == "C":
                res.pop()
            elif o == "+":
                res.append(res[-1] + res[-2])
            elif o == "D":
                res.append(res[-1] * 2)
            else:
                res.append(int(o))
        return sum(res)
        