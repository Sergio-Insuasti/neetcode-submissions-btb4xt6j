class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for t in tokens:
            if t == "+":
                res.append(res.pop() + res.pop())
            elif t == "-":
                b = res.pop()
                a = res.pop()
                res.append(a - b)
            elif t == "*":
                res.append(res.pop() * res.pop())
            elif t == "/":
                b = res.pop()
                a = res.pop()
                res.append(int(float(a / b)))
            else:
                res.append(int(t))
        return res[0]
