class Solution:
    def isHappy(self, n: int) -> bool:
        def getNumSum(n):
            res = 0
            while n:
                tail = n % 10
                res += tail**2
                n = n // 10
            return res
        
        visit = set()

        while n not in visit:
            visit.add(n)
            n = getNumSum(n)
            if n == 1:
                return True
        return False