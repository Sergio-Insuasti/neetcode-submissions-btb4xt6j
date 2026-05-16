class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minbuy = prices[0]

        for p in prices:
            maxProf = max(p - minbuy, maxProf)
            minbuy = min(p, minbuy)
        return maxProf

