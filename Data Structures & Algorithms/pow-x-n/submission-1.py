class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            t = x
            for _ in range(1, n):
                t *= x
        elif n == 0: return 1
        else:
            n = abs(n)
            t = x
            for _ in range(1, n + 2):
                t /= x
        
        return t