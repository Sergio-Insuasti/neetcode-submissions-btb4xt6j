class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        l = 0
        r = x
        while l < r:
            m = (l + r)//2
            if m ==0:
                l = l + 1
                continue
            div = int(float(x)/m)
            if div == m:
                return m
            if div < m:
                r = m
            else:
                l = m + 1
        return l - 1