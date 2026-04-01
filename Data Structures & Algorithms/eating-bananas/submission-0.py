class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, k):
            total = sum([math.ceil(x/k) for x in piles])
            return total <= h
        i = 1
        j = max(piles)
        while i <= j:
            m = (i + j) // 2
            if canEat(piles, m):
                j = m - 1
            else:
                i = m + 1
        return i