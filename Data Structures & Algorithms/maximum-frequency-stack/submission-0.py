class FreqStack:

    def __init__(self):
        self.c = Counter()
        self.s = []


    def push(self, val: int) -> None:
        self.s.append(val)
        self.c[val] += 1

    def pop(self) -> int:
        maxC = max(self.c.values())
        i = len(self.s) - 1
        while self.c[self.s[i]] != maxC:
            i -= 1 
        self.c[self.s[i]] -= 1
        return self.s.pop(i)
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()